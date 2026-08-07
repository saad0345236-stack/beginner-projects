# Practicing Drill:
print("This is a student's gradebook")

while True:
    students = []
    enter_student = input("Enter student name: ").lower()
    students.append(enter_student)
    try:
        final_exam_score = int(input("What's their final exam score out of 50 marks? "))
    except:
        print("Enter an integer.")
        continue
    percentage = (final_exam_score / 50) * 100

    print(f'{enter_student} had a {percentage}% in the final exam.')
    
    checking = input("Do you want to check whether a student is in the list? (y/n): ").lower()
    if checking == 'y':
        ask = input("Who? ")
        print("If the student isn't in the list you'll see 'False' otherwise 'True'...")
        print(ask in students)
    else:
        print("Okay")
        pass
    quit = input("Quit? (y/n): ")
    if quit == 'y':
        break
    else:
        pass