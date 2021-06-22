def my_print(txt):
    print(txt)


msg_template = """Hello {name},
Thank you for joining {website}, we are very
happy to have you with us.
"""


def format_msg(my_name="Justin", my_website="creditsafe"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # my_print(my_msg)
    return my_msg


"""
    "{}{}".format("abc", 123) #positional arguments
    "{1}{0}".format("abc", 123) #indexbased arguments
    "{name}{number}".format(name = "abc", number = 123) #keyword based arguments
    "{}{name}{number}".format("another", name = "abc", number = 123) #mixed arguments
"""
