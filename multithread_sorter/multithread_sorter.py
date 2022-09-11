# многопоточное занесение уникальных значений в БД
# обратите внимание, что названия файлов и переменных не имеют отношения к используемым данным

# запуск производится в едином обработчике исключения 'KeyboardInterrupt', чтобы в случае нажатия Ctrl+C вся предыдущая работа была сохранена в БД без потерь
try: 
    # импорт необходимых библиотек
    import asyncio  # поддержка многопоточности
    import traceback  # вывод полной ошибки необработанного исключения
    import logging  # логгирование программы
    from progress.bar import Bar  # прогресс-бар
    import sqlite3  # поддержка работы с базой данных, в которую, собственно, и вносятся данные

    # список файлов, используемых для работы. Можно указать как пути к файлам, так и их название, при запуске программы в папке с файлами для работы
    files = ['']

    # настройки прогресс-бара. В переменной 'max' указано приблизительное количество строк в обрабатываемых файлах
    bar = Bar('File processing', max = 100, suffix='%(index)d/%(max)d - %(eta)ds ')

    # параметры логгирования программы
    logging.basicConfig(filename = "multithread_worker.log", format = "%(asctime)s - %(levelname)s - %(message)s", level='INFO')

    # подключение БД
    conn = sqlite3.connect('')  # название для файла БД. Если файл не существует - он будет создан под указанным названием
    c = conn.cursor()
    c.executescript("""
                BEGIN TRANSACTION;
                CREATE TABLE IF NOT EXISTS "table_name" (
                    `mail` TEXT UNIQUE,
                    'pass' TEXT 
                );""")  # выполняем скрипт, в ходе которого создается таблица 'table_name' (в случае ее отсутствия) с уникальными полями 'mail' и 'pass'
    conn.commit()  # подтверждаем изменения в БД, занося соответствующие правки в нее

    # 
    printable = '0123456789abcdefghijklmnopqrstuvwxyz!#$%&()*+,-.<=>?@[]^_{|}~' # словарь для поля 2
    mailwords = '0123456789abcdefghijklmnopqrstuvwxyz@.' # словарь для поля 1
    def line_clear(linear, type):
        g = ''
        if type == 'mail': slovar = mailwords
        if type == 'pass': slovar = printable
        for element in linear.lower():
            if element in slovar:
                g += element
        return g

    async def f(filename):
        while True:
            with open(filename, 'r') as file:
                try:
                    while True:
                        try:
                            line = next(file).split(':')
                            if type(line) == list and len(line)==2:
                                toexecute = "INSERT INTO mailpass (mail, pass) VALUES ('{0}', '{1}')".format(line_clear(line[0], 'mail'), line_clear(line[1], 'pass'))
                                c.execute(toexecute)
                                logging.debug('{filename} added {line}'.format(filename=filename, line=line_clear(line[0], 'mail')+':'+line_clear(line[1], 'pass')))
                            else: 
                                logging.debug('{filename} skipped {line}'.format(filename=filename, line=':'.join(line)).replace('\n', ''))
                            await asyncio.sleep(0)
                        except (sqlite3.IntegrityError, sqlite3.OperationalError, UnicodeDecodeError) as e:
                            logging.debug('{filename} skipped_with_continue {excepter} {line}'.format(filename=filename, excepter=e, line=':'.join(line)).replace('\n', ''))
                        except Exception:
                            print(traceback.format_exc())
                            logging.warning(traceback.format_exc())
                        finally:
                            await asyncio.sleep(0)
                except StopIteration:
                    logging.info('{} dead'.format(filename))
                    print('{} dead'.format(filename))
                    break

    async def fcommit():
        k = 0
        while True:
            if k % 50000 == 0:
                conn.commit()
                logging.info('db_updated all:{all}'.format(all=k))
            bar.next()
            k+=1
            await asyncio.sleep(0)

    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(f(files[0])),
        ioloop.create_task(f(files[1])),
        ioloop.create_task(f(files[2])),
        ioloop.create_task(f(files[3])),
        ioloop.create_task(f(files[4])),
        ioloop.create_task(f(files[5])),
        ioloop.create_task(f(files[6])),
        ioloop.create_task(f(files[7])),
        ioloop.create_task(fcommit()),
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()

    c.close()
    conn.close()
except (KeyboardInterrupt, NameError):
    conn.commit()
    c.close()
    conn.close()
