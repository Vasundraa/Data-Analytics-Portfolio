students = {}

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        dob = input("Enter Date of Birth: ")
        degree = input("Enter Degree: ")
        course_code = input("Enter Course Code: ")
        course = input("Enter Course: ")
        credit = input("Enter Credit: ")
        duration = input("Enter Course Duration (weeks): ")

        students[roll_no] = {
            "Name": name,
            "DOB": dob,
            "Degree": degree,
            "Course Code": course_code,
            "Course": course,
            "Credit": credit,
            "Duration": duration
        }

        print("Student details stored successfully!")

    elif choice == "2":
        roll_no = input("Enter Roll No to search: ")

        if roll_no in students:
            print("\nStudent Details:")
            for key, value in students[roll_no].items():
                print(key, ":", value)
        else:
            print("Student not found.")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")