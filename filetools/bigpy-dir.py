import os, glob, sys

if len(sys.argv) == 1:
    dir_name = r'C:\Users\NikiTolLa\AppData\Local\Programs\Python\Python312\Lib'
else:
    dir_name = sys.argv[1]

all_sizes = []
all_py = glob.glob(dir_name + os.sep + '*.py')

for file_name in all_py:
    all_sizes.append((os.path.getsize(file_name), file_name))

all_sizes.sort(reverse=True)
print(all_sizes[:1])
print(all_sizes[-1])
