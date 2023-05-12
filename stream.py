import sys

def read_list(path):
    try:
        file = open(path, 'r')
    except IOError:
        return None
    list_data = []
    for line in file:
        list_data.append(line.strip())
    return list_data

def show_connect(imap, exit_on_fail):
    if (imap == None):
        print('Khong the ket noi den may chu!')
        print('Hay kiem tra thong tin trong file imap.ini.')
        if (exit_on_fail == True):
            sys.exit(1)
    else:
        print('Ket noi thanh cong!')