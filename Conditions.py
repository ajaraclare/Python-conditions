marks = int(input("Enter your marks : "))

if marks >100 or marks <0 :
    print("Invalid input")

elif marks > 74:
    print("Grade A")

elif marks > 49 :
    print("Grade B")

elif marks > 24 :
    print("Grade C")

else:
    print("Grade D")
