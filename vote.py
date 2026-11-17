age = int(input("Enter your age: "))
if age <0:
    print("Invalid age. Please enter a non-negative value.")
elif age < 18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")