#4 operation caculator
print("✨ Simple Calculater ✨")
print ("Operations: '+' , '-' , '*' , '/'")
 #TAKING INPUT
a = float(input("Enter the first number: "))
operation = input("OPERTION: ")
b = float(input("Enter the second number: "))

#conditions
if operation == "+":
    print (f"RESULT ✔️: {a+b}")

elif operation == "-":
       print (f"RESULT ✔️: {a-b}") 

elif operation == "*":
      print (f"RESULT ✔️: {a*b}")

elif operation == "/":
    if b != 0:                  #this is called "nesting"
        print (f"RESULT ✔️: {a/b}")
    else:
      print("NUMBER CANNOT BE DIVIDED BY 0! ❌")

else:
     print("Invalid operation ❌! '\n' Please use +, -, *, or /.")      