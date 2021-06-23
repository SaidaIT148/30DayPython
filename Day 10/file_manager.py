

from os import name
import os

email_txt = os.path.join("templates", "email.txt")

this_file_path = os.path.abspath(__file__)  # to get current file exat path
# print(this_file_path)

# to get parent directory of current file
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_PATH = os.path.dirname(BASE_DIR)

#print(BASE_DIR, ENTIRE_PROJECT_PATH)

content = ""

with open(email_txt, "r") as f:
    content = f.read()

print(content.format(name="Saida"))
