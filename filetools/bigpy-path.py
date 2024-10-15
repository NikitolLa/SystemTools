# Search for biggest and lowest py file in searching path

import sys, os, pprint

trace = 0

visited = {}
all_sizes = []
for srcdir in sys.path:
    for (this_dir, subs_here, files_here) in os.walk(srcdir):

        if trace > 0: print(this_dir)
        this_dir = os.path.normpath(this_dir)
        fix_case = os.path.normcase(this_dir)

        if fix_case in visited:
            continue
        else:
            visited[fix_case] = True

        for file_name in files_here:
            if file_name.endswith('.py'):

                if trace > 1: print('...', file_name)
                pypath = os.path.join(this_dir, file_name)

                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print('Skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    all_sizes.append((pysize, pylines, pypath))

print()
print('By size ...')
all_sizes.sort(reverse=True)
pprint.pprint(all_sizes[:3])
pprint.pprint(all_sizes[-3:])

print()
print('By lines ...')
all_sizes.sort(key=lambda x: x[1], reverse=True)
pprint.pprint(all_sizes[:3])
pprint.pprint(all_sizes[-3:])