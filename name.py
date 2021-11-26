import ast

eid = {}
file = open('emails.txt', mode='r')
con = file.read()
eid = ast.literal_eval(con)
file.close()


def eread(name):
    return eid.get(name)
    # print(eid)


nm = {}
file = open('numbers.txt', mode='r')
con = file.read()
eid = ast.literal_eval(con)
file.close()


def numRead(name):
    return nm.get(name)
# if __name__ == "__main__":
# print(eread('naman'))
