
'''
def outside(x = 5):
    def inside():
        print x

    return inside


# main
myfunc = outside(7)
myfunc()

'''


def add_one(myfunc):
    def adder():
        return myfunc()+1
    return adder


@add_one
def old_func():
    return 3


print old_func()



