name = input("Enter student name: ")
subjects = input("Enter subjects separated by space: ").split()
passing_input = input("Enter passing marks for each subject separated by space: ").split()
passing_marks = tuple(map(int, passing_input))
print("Subjects:", subjects)
choice = input("Enter subject name: ")
marks = int(input("Enter marks obtained: "))
if choice in subjects:
    index = subjects.index(choice)

    if marks >= passing_marks[index]:
        print(name, "has PASSED in", choice)
    elif marks >= passing_marks[index] - 5:
        print(name, "is in RE-TEST category in", choice)
    else:
        print(name, "has FAILED in", choice)
else:
    print("Subject not found.")