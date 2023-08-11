'''

'''
#Password Strength Checker
'''


import string
import getpass


def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')


if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)
       
'''

'''
Calculator
-------------------------------------------------------------
'''


import os


def addition():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Addition')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   ans = num_1 + num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans += num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def subtraction():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Subtraction')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   ans = num_1 - num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans -= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def multiplication():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Multiplication')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   ans = num_1 * num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans *= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def division():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Division')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   while num_2 == 0.0:
       print('Please enter a second number > 0')
       num_2 = float(input('Enter another number: '))

   ans = num_1 / num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       while num == 0.0:
           print('Please enter a number > 0')
           num = float(input('Enter another number: '))
       ans /= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def calculator():
   quit = False
   while not quit:
       results = []
       print('Simple Calculator in Python!')
       print('Enter \'A\' for addition')
       print('Enter \'S\' for substraction')
       print('Enter \'M\' for multiplication')
       print('Enter \'D\' for division')
       print('Enter \'Q\' to quit')

       choice = input('Selection: ').upper().strip()

       if choice == 'Q':
           quit = True
           continue

       if choice == 'A':
           results = addition()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'S':
           results = subtraction()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'M':
           results = multiplication()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'D':
           results = division()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       else:
           print('Sorry, invalid character')


if __name__ == '__main__':
   calculator()
   