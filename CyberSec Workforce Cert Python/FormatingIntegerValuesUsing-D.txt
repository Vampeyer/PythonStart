For integer values, the d presentation type may be used to format values

The presentation types b, o, x or X can be used to format integer output using binary, octal, and hexadecimal number systems

Consider formatting an inventory report:

>>> part = 'Hammer'
>>> quantity = 10
>>> price = 11.5
>>> print(f'{part:10} : {quantity:3d} @ ${price:.2f}')
Hammer     :  10 @ $11.50