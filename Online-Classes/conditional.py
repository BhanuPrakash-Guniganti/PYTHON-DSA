marks = int(input("Enter you marks: "))

if marks >= 91 and marks <= 100:
    print("Grade O")
elif marks >= 81 and marks < 91:
    print("Grade A+")
elif marks >= 71 and marks < 81:
    print("Grade A")
elif marks >= 61 and marks < 71:
    print("Grade B")
else:
    print("Fail")

