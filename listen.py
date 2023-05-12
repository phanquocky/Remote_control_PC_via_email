from imapproc import get_command
from command import do_command

import time

def listen(imap, cycle, white_list):
    print('Dang nhan lenh tu email... Nhan Ctrl+C de dong ket noi.')
    print('-------------------------------------------------------')
    try:
        while True:
            cmd = get_command(imap)
            for x in cmd:
                if (x[0] in white_list):
                    print('Nhan lenh: "' + x[1] + '" tu: ' + x[0])
                    do_command(x[0], x[1])
                    print('Tiep tuc nhan lenh...')
            time.sleep(cycle)
    except KeyboardInterrupt:
        imap.logout()
        print('Dong ket noi thanh cong.')