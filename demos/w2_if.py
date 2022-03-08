name = input("Enter your name: ")
#len() -function that returns leght of string*
if len(name) > 9:
  print("Your name is way to long to remember. Can i use a niknamle please?")

elif len(name) <= 3:
  print("That is verry short!")
  
elif name == "martha":
  print("Why did you say that name!!!")
  
else:
  print("Oh, your name is pretty short!")

print("Nice to meet you anyway, {}!".format(name)) 