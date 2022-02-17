import  datetime

def my_logger(inp, res):
    with open('log.csv','a') as file:
        file.write(f'{datetime.datetime.now()}, {inp}, {res}, \n')