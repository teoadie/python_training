__author__ = 'Teo'
from model.contact_data import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 2
file_path = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        file_path = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return 1 + random.randrange(32)


def random_month():
    return 1 + random.randrange(12)


testdata = [
               Contact(firstname=" ", middlename=" ", lastname=" ", nickname=" ", title=" ", company=" ", address=" ",
                       first_email=" ", second_email=" ", third_email=" ", homepage=" ", home_phone=" ",
                       mobile_phone=" ", work_phone=" ", fax_phone=" ", second_phone=" ",
                       second_address=" ", second_notes=" ", anniversary_year=" ", birthday_year=" ")
           ] + [
               Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nick", 10),
                       title=random_string("title", 10), company=random_string("company", 10),
                       address=random_string("address", 10), first_email=random_string("first_email", 10),
                       second_email=random_string("second_email", 10), third_email=random_string("third_email", 10),
                       homepage=random_string("homepage", 10), home_phone=random_string("home_phone", 10),
                       mobile_phone=random_string("1111", 10), work_phone=random_string("222", 10),
                       fax_phone=random_string("333", 10), second_phone=random_string("4444", 10),
                       second_address=random_string("address", 10), second_notes=random_string("notes", 10),
                       anniversary_year=random_string("2", 10), birthday_year=random_string("1", 10),
                       anniversary_day=random_day(), anniversary_month=random_month(), birthday_day=random_day(),
                       birthday_month=random_month())

               for i in range(5)
               ]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", file_path)

with(open(file_path, "w")) as file:
    jsonpickle.set_encoder_options("json", indent=2)
    file.write(jsonpickle.encode(testdata))
