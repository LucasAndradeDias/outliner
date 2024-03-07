from module import Dummy, final



def test4():
    test5()

def test3():
    return test4()

def test2():
    test3()

def test1():
    test2()

def test5():
    final()

#test = Dummy