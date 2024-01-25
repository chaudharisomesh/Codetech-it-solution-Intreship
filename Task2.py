print("-----Calculator-----")
num1=float(input("Enter a number here:::"))
num2=float(input("Enter b number here:::"))
print("\n1.Addintion\n2.Substraction\n3.multiplication\n4.Division")

choice=int(input("Enter your choice 1-4\n"))

if choice==1:
    print("Addition==",num1+num2)
elif choice==2:
    print("Substraction",num1-num2)
elif choice==3:
    print("multiplication",num1*num2)
elif choice==4:
    print("Division",num1/num2)
else:
    print("Invalid Input")