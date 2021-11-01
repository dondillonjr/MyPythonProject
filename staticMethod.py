#Static Method - Don't have to be instantiated to be use
#defined using decorator @
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def mul5(x):
        return x * 5

    @staticmethod
    def even(x):
        num = x % 2
        if num == 0:
            return "even"
        else:
            return "odd"

    @staticmethod
    def prt():
        print("Finished")

print(Math.add5(5))

print(Math.even(5))

Math.prt()