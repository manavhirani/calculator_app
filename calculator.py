# Manav Hirani

def add(x:float, y:float) -> float:
  return x + y

def subtract(x:float, y:float) -> float:
  return x - y

def multiply(x:float, y:float) -> float:
  return x*y

def divide(x:float, y:float) -> float:
  return x/y

print("Welcome to my calculator.\n")
while True:
  try:
    x, y = map(float, input("Enter your numbers: ").split())
    ops = {'+':add, '-':subtract, '*':multiply, '/':divide}
    op = input("Enter the operation +, -, *, /: ")
    if op == '/':
      if float(y)== 0:
        raise ValueError
      
    print(ops[op](float(x), float(y)))
  except ValueError:
    print("Invalid inputs")
    pass

  print("Press enter to continue, 0 to quit")
  end = input()
  if end == '0':
    break
