from lxml import etree
from sys import argv


def get_depth(root):
    depth = 0
    for el in root:
        if etree.iselement(el):
            depth = get_depth(el) + 1
    return depth


def main():
    if len(argv) > 1:
        path = argv[1]
    else:
        path = 'f.xml'
    tree = etree.parse(path)
    root = tree.getroot()
    depth = get_depth(root)
    print('Max depth:', depth)


if __name__ == '__main__':
    main()