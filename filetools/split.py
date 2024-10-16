import sys, os

kilobytes = 1024
megabytes = kilobytes * 1000
chunk_size = int(1.4 * megabytes)  # by default: size of one chunk


def split(from_file, to_dir, chunk_size=chunk_size):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    else:
        for f_name in os.listdir(to_dir):
            os.remove(os.path.join(to_dir, f_name))
    part_num = 0
    inp = open(from_file, 'rb')

    while True:
        chunk = inp.read(chunk_size)
        if not chunk:
            break

        part_num += 1
        file_name = os.path.join(to_dir, f'part_{part_num}')
        file_obj = open(file_name, 'wb')
        file_obj.write(chunk)
        file_obj.close()

    inp.close()
    assert part_num <= 9999
    return part_num


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunk-size]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            from_file = input('Enter file you want split: ')
            to_dir = input('Enter Directory to store parts of splited file: ')
        else:
            interactive = False
            from_file, to_dir = sys.argv[1:3]
            if len(sys.argv) == 4: chunk_size = int(sys.argv[3])

        abs_from, abs_to = map(os.path.abspath, [from_file, to_dir])
        print('Splitting', abs_from, 'to', abs_to, 'by', chunk_size)

        try:
            parts = split(from_file, to_dir, chunk_size)
        except:
            print('Error during split')
            print(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        else:
            print('Split finished:', parts, 'parts are in', abs_to)

        if interactive:
            input('Press any button to exit: ')
