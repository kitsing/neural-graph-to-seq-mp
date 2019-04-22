import sys


def main():
    line_iterator = open(sys.argv[1], 'rU')
    amrs, id_dict = get_single_line_amrs(line_iterator)

    if len(sys.argv) == 3:
        with open(sys.argv[4] + '.amr', 'w') as amr_fh, open(sys.argv[4] + '.sen', 'w') as sen_fh:
            for line in open(sys.argv[2], 'r'):
                id = line.strip()
                amr, sen = amrs[id_dict[id]]
                amr_fh.write('{}\n'.format(amr))
                sen_fh.write('{}\n'.format(sen))


def get_single_line_amrs(line_iterator):
    ids = []
    id_dict = {}
    amrs = []
    amr_str = ''
    sentence_str = None
    for line in line_iterator:
        if line.startswith('#'):
            if line.startswith('# ::id'):
                id = line.strip().split('# ::id ')[1]
                ids.append(id)
                id_dict[id] = len(ids) - 1
            elif line.startswith('# ::snt '):
                sentence_str = line.strip()[len('# ::snt '):]
            continue
        line = line.strip()
        if line == '':
            if amr_str != '':
                amrs.append((amr_str.strip(), sentence_str))
                amr_str = ''
        else:
            amr_str = amr_str + line + ' '
    if amr_str != '':
        amrs.append((amr_str.strip(), sentence_str))
    return amrs, id_dict


if __name__ == '__main__':
    main()
