import time_dec

@time_dec.timeit(debug=True)
def test():
    tmp = 1
    for i in range(1, 10000000):
        tmp += i
    return tmp

if __name__ == '__main__':
    print test()
