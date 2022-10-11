n = int(input("Write a number "))
fact = 1

def factorial():
   for i in range(1,n+1):
        fact = fact * i
        if n == int(n):
            print ("The factorial of", n, "is ", end = "")
            print (fact)
        else:
            print("Enter only number!")
factorial()
