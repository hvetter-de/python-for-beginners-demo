# Demo how to use a package but with using 'from package import class'

from simplePackage.simpleMath import simpleMath
from simplePackage.dog import dog

# simpleMath
staticSum = simpleMath.staticSumNumbers(5,6)
print(f'StaticSum: {staticSum}')


# dog
dogInstance = dog('Doggo')
dogInstance.add_trick('sit')
dogInstance.add_trick('come')

print('dog tricks:')
for trick in dogInstance.tricks:
    print(trick)