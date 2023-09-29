class test:
    def __init__(self) -> None:
        self.func1()

    def func1(self):
        self.func2()
        return

    def func2(self):
        return


def test2():
    a = test()
    return
