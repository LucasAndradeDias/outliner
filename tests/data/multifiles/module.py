from module_2 import final_function

class Dummy:

    def __init__(self):
        self.method1()

    def method1(self):
        return self.method2()
    
    def method2(self):
        return self.method_math()

    def method_math(self):
        return final_function()

def final():
    Dummy()