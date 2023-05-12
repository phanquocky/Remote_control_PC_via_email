from smtpproc import send_email

# Cach dung ham send_email:
# send_email(arg1, arg2, arg3, arg4)
# trong do: 
# arg1: dia chi email nguoi se nhan duoc email
# arg2: subject email
# arg3: noi dung email
# arg4: danh sach file. vd: ['abc.txt', 'd:/def.doc'], []

def do_command(cmd_sender, cmd):
    # match cmd:
    #     case 'cmd1':
    #         do_cmd1()
    #     case 'cmd2':
    #         do_cmd2()
    print("do cmd")
