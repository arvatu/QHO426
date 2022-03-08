print("Please chodr one of the folowing options:\n\n1-Nice message\n2-Area of Rectanlge\n3-Area of trianlge\n4-Times table")
opt = int(input())

if opt == 1:
  print("You do not smell to bad today!")
elif opt == 2:
  w = float(input("Enter width: "))
  h = float(input("Enter height: "))
  area = w*h
  print("The area is {}".format(area))
elif opt == 3:
   b = float(input("Enter base: "))
   h = float(input("Enter height: "))
   area = 0.5*b*h
   print("The area is {}".format(area)) 
elif opt ==4:
  n = int(input("Enter whole number: "))
  for i in range(1,11):
      print(f"{i}x{n} = {i*n}")
      print("that is all")
