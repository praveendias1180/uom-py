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
  
  def select_op(choice):
    if(choice == "#"):
        return -1
    else:
        return choice
        
  def terminate():
    print("Done. Terminating")
    exit()

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  selected_option = select_op(choice)
  if(selected_option == -1):
    #program ends here
    terminate()
    
  def get_a_number(prompt):
    number = input(prompt)
    print(number)    
    if("$" in number):
        return "$"
    if("#" in number):
        return "#"    
    number = float(number)
    return number
    
  number_1 = get_a_number("Enter first number: ")
  if(number_1 == "$"):
    continue
  if(number_1 == "#"):
    terminate()
  
  number_2 = get_a_number("Enter second number: ")
  if(number_2 == "$"):
    continue
  if(number_2 == "#"):
    terminate()
    
  if(selected_option == "+"):
    result = number_1 + number_2
  elif(selected_option == "/"):
    if(number_2 == 0):
      print("float division by zero")
      result = "None"
    else:
      result = number_1 / number_2
  else:
    continue
    
  print(str(number_1) + " " + selected_option + " " + str(number_2) + " = " + str(result))