import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Templates

# environment variables

username = "saida148.python@gmail.com"
password = "Mondayfun@2021"


class Emailer():
    subject = ""
    template_name = None
    context = {}
    template_html = None
    to_emails = []
    from_email = "saida148.python@gmail.com"
    has_html = bool
    test_send = False

    def __init__(self, subject, template_name=None, context={}, template_html=None, to_emails=None, test_send=False):
        if template_name == None and template_html == None:
            raise Exception("You must set a template")

        assert isinstance(to_emails, list)
        self.subject = subject
        self.to_emails = to_emails
        self.template_name = template_name
        self.context = context
        self.test_send = test_send

        if template_html != None:
            self.has_html = True
            self.template_html = template_html

    def format_msg(self):
        msg = MIMEMultipart("alternative")
        msg["From"] = self.from_email
        msg["To"] = ", ".join(self.to_emails)
        msg["Subject"] = self.subject

        if self.template_name != None:
            tmpl_str = Templates(
                template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(), "plain")
            msg.attach(txt_part)

        if self.template_html != None:
            tmpl_str = Templates(
                template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(), "html")
            msg.attach(html_part)

        msg_str = msg.as_string()
        return msg_str

    def send_mail(self):
        assert isinstance(self.to_emails, list)

        msg = self.format_msg()

        did_send = False
        if not self.test_send:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
                server.ehlo()
                server.starttls()
                server.login(username, password)
                try:
                    server.sendmail(self.from_email, self.to_emails, msg)
                    did_send = True
                except:
                    did_send = False
        return did_send
