import sys, os, pprint

trace = False
dir_name = r'C:\Users\NikiTolLa\AppData\Local\Programs\Python\Python312\Lib'

all_sizes = []

for (this_dir, subs_here, files_here) in os.walk(dir_name):
    if trace: print(this_dir)
    for file_name in files_here:
        if trace: print('...', file_name)
        fullname = os.path.join(this_dir, file_name)
        fullsize = os.path.getsize(fullname)
        all_sizes.append((fullsize, fullname))

all_sizes.sort(reverse=True)
pprint.pprint(all_sizes[0])
pprint.pprint(all_sizes[-1])