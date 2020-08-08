from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("name", 10), description=random_string("description", 10),
                    status=random.choice(["development", "release", "stable", "obsolete"]),
                    view_state=random.choice(["public", "private"]))]
