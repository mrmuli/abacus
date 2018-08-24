class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def multiply(self):
        if self.operands is None:
            return
        total  = 1
        for item in self.operands:
            total *= item
        print(total)

    def subtract(self):
        difference = 0
        for item in self.operands:
            difference -= item
        print(difference)
