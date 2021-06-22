import imaplib
import email
import sys

host = 'imap.gmail.com'
username = "saida148.python@gmail.com"
password = "Mondayfun@2021"

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")


def my_inbox(criteria):
    _, search_data = mail.search(None, criteria)
    my_messages = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, "(RFC822)")
        _, b = data[0]

        email_msg = email.message_from_bytes(b)
        # print(email_msg)

        for header in ["subject", "to", "from", "date"]:
            print("{} : {}".format(header, email_msg[header]))
            email_data[header] = email_msg[header]

        for part in email_msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data["plainbody"] = body.decode()
            if part.get_content_type() == "text/html":
                htmlbody = part.get_payload(decode=True)
                email_data["htmlbody"] = htmlbody.decode()

        my_messages.append(email_data)
    return my_messages


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            inbox = my_inbox(sys.argv[1])
            print(inbox)
        except:
            print("Criteria needs to be correct")
    else:
        print("Criteria should be there")
