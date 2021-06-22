from email.mime import text
import requests
import sys
from datetime import datetime
from formatting import format_msg

from send_mail import send_mail


def send(name, website=None, toEmail=None):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)

    try:
        send_mail(text=msg, to_emails=[toEmail])
        Sent = True
    except:
        Sent = False
    return Sent


if __name__ == "__main__":
    print(sys.argv)
    name = None
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]

    resonse = send(name, toEmail=email)
    print(resonse)
