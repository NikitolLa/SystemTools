import os, pprint
from sys import argv, exc_info

trace = 0  # 0=выкл., 1=каталоги, 2=+файлы
dirname, extname = os.curdir, '.py'  # по умолчанию файлы .py в cwd

if len(argv) > 1: dirname = argv[1]  # например: C:\, C:\Python31\Lib
if len(argv) > 2: extname = argv[2]  # например: .pyw, .txt
if len(argv) > 3: trace = int(argv[3])  # например: “. .py 2”


def try_print(arg):
    try:
        print(arg)  # непечатаемое имя файла?
    except UnicodeEncodeError:
        print(arg.encode())  # вывести как строку байтов


visited = set()
allsizes = []

for (thisDir, subsHere, filesHere) in os.walk(dirname):

    if trace: try_print(thisDir)
    thisDir = os.path.normpath(thisDir)
    fixname = os.path.normcase(thisDir)

    if fixname in visited:
        if trace:
            try_print('skipping ' + thisDir)
    else:
        visited.add(fixname)

        for filename in filesHere:
            if filename.endswith(extname):
                if trace > 1: try_print('+++' + filename)
                fullname = os.path.join(thisDir, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
