from itertools import product


def consumer():
    i = None
    while True:
        j = yield i
        print("consume j %s" % j)


def producer(c):
    exit('nihao')
    c.__next__()
    for i in range(5):
        print('product %s' % i)
        c.send(i)
    c.close()
    pass


# def main():

c = consumer()
product(c)
pass
