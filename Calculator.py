def calculator(a,b,o):
  if o == '+':
    return a+b
  elif o == '-':
    return a-b
  elif o == '*':
    return a*b
  elif o == '/':
    return a/b
  else:
    return 'Invalid Input'
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
print(calculator(a,b,operator))