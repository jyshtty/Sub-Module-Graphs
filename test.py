def test():
    # global a
    a = 10
    foo()

def foo():
    print(a)


test()
