
import sys

def main():
    line_iterator = open(sys.argv[1],'rU')
    amrs, id_dict = get_single_line_amrs(line_iterator)

    if len(sys.argv) == 3:
        for line in open(sys.argv[2],'r'):
            id = line.strip()
            print(amrs[id_dict[id]])


def get_single_line_amrs(line_iterator):
    ids = []
    id_dict = {}
    amrs = []
    amr_str = ''
    for line in line_iterator:
        if line.startswith('#'):
            if line.startswith('# ::id'):
                id = line.strip().split('# ::id ')[1]
                ids.append(id)
                id_dict[id] = len(ids) - 1
            continue
        line = line.strip()
        if line == '':
            if amr_str != '':
                amrs.append(amr_str.strip())
                amr_str = ''
        else:
            amr_str = amr_str + line + ' '
    if amr_str != '':
        amrs.append(amr_str.strip())
    return amrs, id_dict


if __name__ == '__main__':
    main()

