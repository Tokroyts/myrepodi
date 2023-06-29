print("Hello I am your assistant on the Pyton!")

name = input("What is your name?")

mod = int(input(f"Okay {name},please enter the first coordinate - y:"))
mod1 = int(input(f"Please enter the second coordinate - x:"))

if mod >= 0:
    if mod1 >= 0:
        print("This is the I quarter!")
    else:
        print("This is the IV quarter!")
else:
    if mod1 >= 0:
        print("This is the II quarter!")
    else:
       print("This is the III quarter!")


print("Hello I am your assistant on the Pyton!")

name = int(input("What is your name?"))
lastname = int(input("What is your lastname?"))

score = int(input("What is your score on exam?"))

if score >= 80:
    print(f"Studen {name} {lastname} passed the exam!")
else:
    if score ==0:
        print("Prepare for the  exam better next time!")
    else:
        print(f"The student - {name} {lastname} did not pass the exam and is going to retake it!")
