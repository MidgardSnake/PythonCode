#Aufgabe 5.2 
height = int(input('Please enter the "height_value":'))
if height < 1:
    raise ValueError('Incorrect "height_value"!')

width = int(input('Please enter the "width_value":'))
if width < 1:
    raise ValueError('Incorrect "width_value"!')

# * - operator in print: prints the character multiple times

for i in range(height + 2):
    if (i == 0) or (i == (height + 1)):
        print('C'*(width + 2))
    else:
        print('C' + 'A'*width + 'C')