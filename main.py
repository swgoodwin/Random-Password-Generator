#The passwords generated will be 8 characters long and will have to include the following characters in any order: 
# 2 uppercase letters from A to Z, 
# 2 lowercase letters from a to z, 
# 2 digits from 0 to 9, 
# 2 punctuation signs such as !, ?, ", etc.

import random

def shuffle(s):
    '''Shuffle all the characters of a string'''
    temp_list = list(s)
    random.shuffle(temp_list)
    return ''.join(temp_list)


upper_letter1 = chr(random.randint(65, 90))
upper_letter2 = chr(random.randint(65, 90))
lower_letter1 = chr(random.randint(97, 122))
lower_letter2 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
sign1 = chr(random.randint(33, 43))
sign2 = chr(random.randint(33, 43))

password = upper_letter1 + upper_letter2 + lower_letter1 + lower_letter2 + digit1 + digit2 + sign1 + sign2
#password = list(password)
#random.shuffle(password)
#print(''.join(password))
password = shuffle(password)
print(password)