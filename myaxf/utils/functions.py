import random

def get_ticket():

    # 先产生随机的字符串， 长度30
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    ticket = ''
    for i in range(30):
        ticket += random.choice(s)
    # ticket = '' + ticket
    return ticket