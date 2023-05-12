import imaplib, email

def init_imap_mail(conf):
    try:
        mail = imaplib.IMAP4_SSL(conf[0], conf[1], timeout=int(conf[5]))
        mail.login(conf[2], conf[3])
    except imaplib.IMAP4.error:
        return None
    return mail

def get_command(imap):
    imap.list()
    imap.select('inbox')
    result, data = imap.uid('search', None, 'unseen')
    amount = len(data[0].split())
    command = []
    for i in range(amount):
        lastest_email_uid = data[0].split()[i]
        result, email_data = imap.uid('fetch', lastest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
        command.append([email.utils.parseaddr(email_from)[1], subject])
    return command
