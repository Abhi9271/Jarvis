import ast


def eread(name):
    eid = {}
    file = open('emails.txt', mode='r')
    con = file.read()
    eid = ast.literal_eval(con)
    file.close()

    return eid.get(name)
    # print(eid)


def num_read(name):
    number = {}
    file = open('numbers.txt', mode='r')
    con = file.read()
    number = ast.literal_eval(con)
    file.close()

    return number.get(name)


# if __name__ == "__main__":
#     print(eread('name'))
#     print(num_read("name1"))
