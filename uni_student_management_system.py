students = {}

TOTAL_MATRIC = 1100
TOTAL_FSC = 1100


def calculate_percentages(matric, fsc):
    matric_percentage = (matric / TOTAL_MATRIC) * 100
    fsc_percentage = (fsc / TOTAL_FSC) * 100
    average_percentage = (matric_percentage + fsc_percentage) / 2

    if average_percentage >= 70:
        scholarship = "Eligible"
    else:
        scholarship = "Not Eligible"

    return matric_percentage, fsc_percentage, average_percentage, scholarship


def add_student():
    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID : ")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name : ")

    while True:
        age = input("Enter Age : ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid Age.")

    gender = input("Enter Gender : ")
    city = input("Enter City : ")

    while True:
        matric = input("Enter Matric Marks : ")
        if matric.isdigit():
            matric = int(matric)
            if 0 <= matric <= TOTAL_MATRIC:
                break
        print("Invalid Matric Marks.")

    while True:
        fsc = input("Enter FSc Marks : ")
        if fsc.isdigit():
            fsc = int(fsc)
            if 0 <= fsc <= TOTAL_FSC:
                break
        print("Invalid FSc Marks.")

    matric_percentage, fsc_percentage, average_percentage, scholarship = calculate_percentages(matric, fsc)

    students[student_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city,
        "matric": matric,
        "fsc": fsc,
        "matric_percentage": matric_percentage,
        "fsc_percentage": fsc_percentage,
        "average_percentage": average_percentage,
        "scholarship": scholarship
    }

    print("\nStudent Added Successfully.")


def search_student():
    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID : ")

    if student_id in students:
        s = students[student_id]

        print("\n========== Student Found ==========")
        print("Student ID         :", student_id)
        print("Student Name       :", s["name"])
        print("Age                :", s["age"])
        print("Gender             :", s["gender"])
        print("City               :", s["city"])
        print("Matric Marks       :", s["matric"])
        print("FSc Marks          :", s["fsc"])
        print("Matric Percentage  : {:.2f}%".format(s["matric_percentage"]))
        print("FSc Percentage     : {:.2f}%".format(s["fsc_percentage"]))
        print("Average Percentage : {:.2f}%".format(s["average_percentage"]))
        print("Scholarship Status :", s["scholarship"])

    else:
        print("Student Record Not Found.")


def update_student():
    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID : ")

    if student_id not in students:
        print("Student Record Not Found.")
        return

    while True:
        matric = input("Enter New Matric Marks : ")
        if matric.isdigit():
            matric = int(matric)
            if 0 <= matric <= TOTAL_MATRIC:
                break
        print("Invalid Marks.")

    while True:
        fsc = input("Enter New FSc Marks : ")
        if fsc.isdigit():
            fsc = int(fsc)
            if 0 <= fsc <= TOTAL_FSC:
                break
        print("Invalid Marks.")

    matric_percentage, fsc_percentage, average_percentage, scholarship = calculate_percentages(matric, fsc)

    students[student_id]["matric"] = matric
    students[student_id]["fsc"] = fsc
    students[student_id]["matric_percentage"] = matric_percentage
    students[student_id]["fsc_percentage"] = fsc_percentage
    students[student_id]["average_percentage"] = average_percentage
    students[student_id]["scholarship"] = scholarship

    print("Student Record Updated Successfully.")


def delete_student():
    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID : ")

    if student_id in students:

        choice = input("Are you sure you want to delete this student? (Y/N): ")

        if choice.upper() == "Y":
            del students[student_id]
            print("Student Record Deleted Successfully.")
        else:
            print("Delete Cancelled.")

    else:
        print("Student Record Not Found.")


def show_all_students():
    print("\n========== STUDENT LIST ==========")

    if len(students) == 0:
        print("No Student Records Available.")
        return

    for student_id, s in students.items():
        print("----------------------------------------")
        print("ID                 :", student_id)
        print("Name               :", s["name"])
        print("Average Percentage : {:.2f}%".format(s["average_percentage"]))
        print("Scholarship        :", s["scholarship"])

    print("----------------------------------------")


def display_menu():
    print("\n===========================================")
    print(" UNIVERSITY STUDENT MANAGEMENT SYSTEM")
    print("===========================================")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")
    print("===========================================")


def main():
    while True:

        display_menu()

        choice = input("Enter Choice : ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            show_all_students()

        elif choice == "6":
            print("\n===========================================")
            print("Thank You for Using")
            print("University Student Management System")
            print("===========================================")
            break

        else:
            print("Invalid Choice.")


main()