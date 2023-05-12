from stream import read_list, show_connect
from imapproc import *
from listen import *
from constant import *

def main():
    imap_conf = read_list(CONF_PATH)
    white_list = read_list(WHITE_LIST_PATH)
    imap = init_imap_mail(imap_conf)
    show_connect(imap, exit_on_fail=True)
    listen(imap, int(imap_conf[4]), white_list)
    input("Nhan Enter de thoat chuong trinh.")

if __name__ == '__main__':
    main()


#  alo 