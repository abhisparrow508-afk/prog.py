marks = int(input("Enter your marks: "))
if marks >= 100 or marks < 0:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif marks >= 90 and marks <= 100:
    print("You have secured A grade.")
elif marks >= 75 and marks <= 89:
    print("You have secured B grade.")
elif marks >= 60 and marks <= 74:
    print("You have secured C grade.")