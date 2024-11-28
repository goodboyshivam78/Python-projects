while True:
    try:
        age = int(input("Enter your age: "))
    except:
        print("Enter numeric digits for your age.")
        continue
    if age<=0:
        print("Please enter a positive number +_+")
        continue
    break
print(f"Your age is: {age}")
    
