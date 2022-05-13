# get a valid number
def get_a_valid_number(prompt):
    while True:
        number_input = input(prompt)
        if("$" in number_input):
            valid_number = False
            break
        try:
            valid_number = float(number_input)
            break
        except:
            print("Not a valid number,please enter again")
            continue   
    return valid_number 

# select operand
def select_op(choice):
    inputs = ["+", "-", "*", "/", "^", "%", "$"]
    if(choice == "#"):
        return -1
    elif(choice in inputs): 
        return choice
    else:
        print("Unrecognized operation")
        return "$"   

# print the calculator result
def print_calc_result(first_number, select_op_choice, second_number, result):
    print(str(first_number) + " " + select_op_choice + " " + str(second_number) + " = " + str(result))

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  if("$" in choice):
      print("resetting...")
      continue

  print(choice)

  select_op_choice = select_op(choice)
  if( select_op_choice == -1):
    #program ends here
    print("Done. Terminating")
    exit()

  if( select_op_choice == "$"):
    continue

  first_number = get_a_valid_number("Enter first number: ")
  if(not first_number):
      print("resetting...")
      continue

  second_number = get_a_valid_number("Enter second number: ")
  if(not second_number):
    print("resetting...")
    continue

  if(select_op_choice == "+"):
    result = first_number + second_number
  elif(select_op_choice == "-"):
      result = first_number - second_number
  elif(select_op_choice == "*"):
      result = first_number * second_number
  elif(select_op_choice == "/"):
      if(second_number == 0):
          print("float division by zero")
          result = "None"
      else:
          result = first_number / second_number
  elif(select_op_choice == "^"):
      result = first_number ^ second_number      
  elif(select_op_choice == "%"):
      result = first_number % second_number  
  elif(select_op_choice == "$"):
      continue  
  else:
    continue

  print_calc_result(first_number, select_op_choice, second_number, result)

