import requests
import sys
from datetime import datetime
from formatting import format_msg


def send(name, website=None):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    print(msg)

    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"


if __name__ == "__main__":
    print(sys.argv)
    name = None
    if len(sys.argv) > 1:
        name = sys.argv[1]

    resonse = send(name)
    print(resonse)
