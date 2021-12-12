'''
module for reading email and phone number data from text files
'''
from ast import literal_eval


def eread(name):
    '''
    Returns the stored email id from a
    dictionary for the corresponding name argument
    '''
    eid = {}
    file = open('emails.txt', mode='r')
    con = file.read()
    eid = literal_eval(con)
    file.close()

    return eid.get(name)
    # print(eid)


def num_read(name):
    '''
    Returns the stored phone number from a
    dictionary for the corresponding name argument
    '''
    number = {}
    file = open('numbers.txt', mode='r')
    con = file.read()
    number = literal_eval(con)
    file.close()

    return number.get(name)


# if __name__ == "__main__":
#     print(eread('name'))
#     print(num_read("name1"))
