class simpleMath:

    def __init__(self, value):
        self.number = value

    # This is a comment
    def getNumber(self):
        '''
        Returns the value from the constructor.
        '''
        return self.number

    def sumNumbers(self, number2):
        '''
        Sum two numbers and return the result.
        '''
        sum = self.number + number2
        return sum

    # Static methods doesn't have a 'self' parameter.
    @staticmethod
    def staticSumNumbers(number1, number2):
        '''
        Sum two numbers and return the result.
        '''
        sum = number1 + number2
        return sum