# Demo how to use Modules (python file in same directory)

import simpleMath

mathInstance = simpleMath.simpleMath(5)
number = mathInstance.getNumber()

print(f'Number: {number}')

sum = mathInstance.sumNumbers(6)

print(f'Sum: {sum}')

staticSum = simpleMath.simpleMath.staticSumNumbers(5,6)

print(f'Static sum: {staticSum}')