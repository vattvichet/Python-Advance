try:
    x = int(input("Enter an integer:"))
    print(x)
except:
    print("it is not an integer")
else: 
    print("nothing went wrong")
finally:
    print("try except finished")
