# 1. Write a python script to create a ArithmeticError
"""
firstNum = int(input('Enter the number:'))
scndnUM = int(input('Enter zero to arithmetiic error:'))
print(firstNum/scndnUM)

"""
  
# 2. Write a python script to create a ValueError
"""
firstNum = int(input('Enter the number:'))
scndnUM = input('Enter string to create ValueError:')
print(firstNum/scndnUM)

"""

# 3. Write a python script to handle the ArithmeticError

"""
try:
  firstNum = int(input('Enter the number:'))
  scndnUM = int(input('Enter the second Number::'))
  result=(firstNum/scndnUM)
except ZeroDivisionError:
  print('Cannot divide a number with zero')

"""


# 4. Write a python script to handle a ValueError

"""
try:
  firstNum = int(input('Enter the number:'))
  scndnUM = int(input('Enter a string:'))
  result=(firstNum/scndnUM)
except ValueError:
  print('Cannot divide a string')

"""

# 5. Write a python script to handle multiple Exception in one try\

"""
try:
  firstNum = int(input('Enter the number:'))
  scndnUM = int(input('Enter the second Number::'))
  result = firstNum/scndnUM
except ZeroDivisionError:
  print('Cannot Duvide with Zero')
except ValueError:
  print('Cannot divide with str please enter a correct value')
except ArithmeticError:
  print('Please enter the correct value')
except Exception as msg:
  print(msg)
  
"""


# 6. Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exceptions.



# ""def Calculator():
#   try:
#     print("""Which Operations You Want To perform\n1 - For ADDITION\n2 - For Multiplication\n3 - For Substraction\n4 - For Divison
#     """)
#     print()
#     a = eval(input('Enter the number:'))
#     b = eval(input('Enter the number:'))
#     option = int(input('Enter the Option:'))
#     if option == 1:
#       print('Performing additiin Operation')
#       if type(a) == str or type(b) == str:
#         raise TypeError() or NameError()
#       else:
#         print(a+b)

#     elif option == 2:
#       print('Performing multiplication Operation')
#       if a == 0 or b ==0:
#         raise Exception()
#       else:
#         print(a-b)
        
#   except ArithmeticError:
#     print('num should be diffrent')

#   except TypeError:
#     print("'unsupported operand type(s) for +: 'int' and 'str''")
  
#   except NameError:
#     print('Provide Correct Numbers')
  
#   except Exception as msg:
#     print(msg)


# Calculator("")


# 7. Write a python script to add a finally block for the above script
# def Calculator():
#   try:
#     print("""Which Operations You Want To perform\n1 - For ADDITION\n2 - For Multiplication\n3 - For Substraction\n4 - For Divison
#     """)
#     print()
#     a = eval(input('Enter the number:'))
#     b = eval(input('Enter the number:'))
#     option = int(input('Enter the Option:'))
#     if option == 1:
#       print('Performing additiin Operation')
#       if type(a) == str or type(b) == str:
#         raise TypeError() or NameError()
#       else:
#         print(a+b)

#     elif option == 2:
#       print('Performing multiplication Operation')
#       if a == 0 or b ==0:
#         raise Exception()
#       else:
#         print(a-b)
        
#   except ArithmeticError:
#     print('num should be diffrent')

#   except TypeError:
#     print("'unsupported operand type(s) for +: 'int' and 'str''")
  
#   except NameError:
#     print('Provide Correct Numbers')
  
#   except Exception as msg:
#     print(msg)

#   finally:
#     print('Thank You For Using This Calulator')


# Calculator()

# 8. Write a python script to implement try except and else block for division
# def Calculator():
#   try:
#     print("""Which Operations You Want To perform\n1 - For ADDITION\n2 - For Multiplication\n3 - For Substraction\n4 - For Divison
#     """)
#     print()
#     option = int(input('Enter the Option:'))
#     a = eval(input('Enter the number:'))
#     b = eval(input('Enter the number:'))
#     if option == 1:
#       print('Performing additiin Operation')
#       if type(a) == str or type(b) == str:
#         raise TypeError() or NameError()
#       else:
#         print(a+b)

#     elif option == 2:
#       print('Performing multiplication Operation')
#       if a == 0 or b ==0:
#         raise Exception()
#       else:
#         print(a-b)

#     elif option == 4:
#       print('Performing Division Operation:')
#       if a==0 or b ==0:
#         raise ZeroDivisionError()

#   except ZeroDivisionError:
#     print('Cannot divide the number with Zero')
        
#   except ArithmeticError:
#     print('num should be diffrent')

#   except TypeError:
#     print("'unsupported operand type(s) for +: 'int' and 'str''")
  
#   except NameError:
#     print('Provide Correct Numbers')
  
  
#   except Exception as msg:
#     print(msg)
  
#   else:
#     print(a/b)

#   finally:
#     print('Thank You For Using This Calulator')


# Calculator()
# 9. Write a python script to raise a ValueError.
"""try:
  a = int(input('Enter the value of a:'))
  b = int(input('Enter the value of b:'))
  result = a/b
  print(result)
except ValueError as msg:
  print(msg)"""

# 10. Write a python script to implemented a nested Try Except block
try:
  a = int(input('Enter the value:'))
  b =  int(input('Enter the value of b:'))
  print(a/b)
  try:
    a = eval(input('Enter the value of a:'))
    b = eval(input('Enter the value of b:'))+
    print(a/b)
  except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
  print(msg)
  