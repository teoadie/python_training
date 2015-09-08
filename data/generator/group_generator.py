__author__ = 'Teo'
from model.group_data import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err) # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 2
file_path = "data/groups.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        file_path = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[
             Group(name='Best friends', header='My best friends', footer='Hell yeah'),
             Group(name=" ", header=" ", footer=" "),
             Group("", "", "")
         ] + \
         [Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
          for i in range(n)]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", file_path)


with(open(file_path, "w")) as file:
    jsonpickle.set_encoder_options("json", indent=2)
    file.write(jsonpickle.encode(testdata))
