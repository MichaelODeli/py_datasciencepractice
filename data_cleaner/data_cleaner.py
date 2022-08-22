# import os
# os.system('CLS')

from progress.bar import Bar
bar = Bar('File processing', max = 472484128, suffix='%(progress)d%% - %(index)d/%(max)d - %(eta)ds')
k = 0
with open('name.txt', 'r') as f1, open('other-name.txt', 'w') as f2:
    # while True:
    for line in f1:
        try:
            # line = next(f1).split(':')
            line = line.replace('\n', '').split(':')
            if line[1] == '' or line[1]==line[2]=='':
                continue
            line.pop(-1), line.pop(-1)
            if line[0] == line[2] or line[2]=='':
                line[2] = '0'
            line.pop(0)
            line = ':'.join(line) + '\n'
            line=line.replace(' ', '')
            f2.write(line)
            bar.next()
        except IndexError:
            print(line)
            continue
