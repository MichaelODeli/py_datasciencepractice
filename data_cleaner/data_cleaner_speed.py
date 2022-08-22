import pandas as pd
f = open('output.txt', 'w', encoding="utf-8")
f.close()
from progress.bar import Bar
# ch = 10**6
ch = 10**3
length = 472484128/ch
bar = Bar('File processing', max = length, suffix='%(progress)d%% - %(index)d/%(max)d - %(eta)ds ')
bar.start()
with pd.read_csv('input.txt', sep=":", header=None, on_bad_lines='skip', names=['number', 'email', 'pass', 'hash', 'other_hash'], chunksize = ch) as data:
    for chunk in data:
        chunk.drop(axis='columns', labels=['number', 'hash', 'other_hash'], inplace=True)
        chunk.dropna(inplace=True)
        nparray = chunk.to_numpy(str)
        for element in nparray:
            element = ':'.join(element) + '\n'
            with open('output.txt', 'a', encoding="utf-8") as fl:
                fl.write(element)

        bar.next()
