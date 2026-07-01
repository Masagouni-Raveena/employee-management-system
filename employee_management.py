employees = []


def add_employee():
    emp_id = input("Enter Employee ID: ")

    # Check duplicate Employee ID
    for employee in employees:
        if employee["emp_id"] == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employee = {
        "emp_id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee Added Successfully!")


def view_employees():
    if len(employees) == 0:
        print("No employees found.")
    else:
        print("\n========== Employee List ==========")
        for employee in employees:
            print(f"Employee ID : {employee['emp_id']}")
            print(f"Name        : {employee['name']}")
            print(f"Department  : {employee['department']}")
            print(f"Salary      : {employee['salary']}")
            print("-----------------------------------")


def search_employee():
    search_id = input("Enter Employee ID to search: ")

    found = False

    for employee in employees:
        if employee["emp_id"] == search_id:
            print("\nEmployee Found")
            print(f"Employee ID : {employee['emp_id']}")
            print(f"Name        : {employee['name']}")
            print(f"Department  : {employee['department']}")
            print(f"Salary      : {employee['salary']}")
            found = True
            break

    if not found:
        print("Employee not found.")


def update_employee():
    update_id = input("Enter Employee ID to update: ")

    found = False

    for employee in employees:
        if employee["emp_id"] == update_id:
            employee["name"] = input("Enter New Name: ")
            employee["department"] = input("Enter New Department: ")
            employee["salary"] = int(input("Enter New Salary: "))
            print("Employee Updated Successfully!")
            found = True
            break

    if not found:
        print("Employee not found.")


def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")

    found = False

    for employee in employees:
        if employee["emp_id"] == delete_id:
            employees.remove(employee)
            print("Employee Deleted Successfully!")
            found = True
            break

    if not found:
        print("Employee not found.")


while True:

    print("\n===================================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()

        elif choice == 2:
            view_employees()

        elif choice == 3:
            search_employee()

        elif choice == 4:
            update_employee()

        elif choice == 5:
            delete_employee()

        elif choice == 6:
            print("Thank you for using Employee Management System.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")