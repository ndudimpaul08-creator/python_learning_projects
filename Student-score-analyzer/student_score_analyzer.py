# STUDENT SCORE ANALYZER

students = []
subjects = ("Math","English","Science")

while True:
    print("\n===== STUDENT SCORE ANALYZER =====")
    print("1. Add student")
    print("2. View students")
    print("3. Calculate averages")
    print("4. Find highest averages")
    print("5. Show subjects")
    print("6. Search for student")
    print("7. Exit")

    choice = input("Choose an option: ")
    print(f"\n You have successfully chosen option {choice}.")

    #Adding Student
    if choice == "1":
        name = input("Enter your name: ")

        math = float(input("Enter Math's score: "))
        english = float(input("Enter English's score: "))
        science = float(input("Enter Science's score: "))

        student = (name,math,english,science)
        students.append(student)
        print("STUDENT ADDED SUCCESSFULLY")
        continue

    #Viewing students    
    elif choice == "2":
            if len(students) == 0:
                print("No student available")
                continue
            else:
                print("\n ====STUDENTS====")

                for student in students:
                    name,math,english,science = student

                    print(f"\nName: {name}")
                    print(f"Math Score: {math}")
                    print(f"English Score: {english}")
                    print(f"Science Score: {science}")
    # Calculate Average
    elif choice == "3":
        if len(students) == 0:
            print("No Student available")
            continue
        else:
            for student in students:
                name,math,english,science = student

                total = math + english + science
                average = total / 3

                if average >= 70:
                    grade = "A"
                elif average >= 60:
                    grade = "B"
                elif average >= 50:
                    grade = "C"
                elif average >= 45:
                    grade = "D"
                elif average >= 40:
                    grade = "E"
                else:
                    grade = "F"
                
                status = "Pass" if average>= 40 else "Fail"

                print(f"\n{name}")
                print(f"Total: {total}")
                print(f"Average: {average:.2f}")
                print(f"Grade: {grade}")
                print(f"Status: {status}")
    elif choice == "4":
        if len(students) == 0:
            print("No Student available!")
            continue
        else:
            highest_average = 0
            highest_student = ""

            for student in students:
                    name,math,english,science = student
            average = (math + english + science)   / 3

            if average > highest_average:
                highest_average = average
                highest_student = name

            print(f"\n Highest average: {highest_average}")
            print(f"Student: {highest_student}")

    elif choice == "5":
        print("\n----- STUDENTS -----")

        for subject in subjects:
            print(subject)

    elif choice == "6":
        search_name = input("Enter Search name: ")

        found = False

        for student in students:
            name,math,english,science = student
            
            if name.lower() == search_name.lower():
                print(f"\nName: {name}")
                print(f"Math Score: {math}")
                print(f"English Score: {english}")
                print(f"Science Score: {science}")

                found = True
                break
            
            if not found:
                print("Student not found!")
    elif choice == "7":
        print("Goodbye!")
        break            
    else:
        print("Invalid option. please choose 1-7.")
        continue