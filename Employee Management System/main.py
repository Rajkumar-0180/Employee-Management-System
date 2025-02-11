from employee_operations import Employee, AVLTree

def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Display All Employees")
    print("4. Exit")

avl_tree = AVLTree()
root = None

def main():
    global root

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            employee = Employee(emp_id, name, age, department)
            root = avl_tree.insert(root, employee)
            print(f"Employee {name} added successfully!")

        elif choice == '2':
            emp_id = int(input("Enter Employee ID to search: "))
            employee = avl_tree.search(root, emp_id)
            if employee:
                print(f"Found: {employee.emp_id}: {employee.name}, Age: {employee.age}, Department: {employee.department}")
            else:
                print("Employee not found.")

        elif choice == '3':
            print("Displaying Employees (Tree Traversal Needed)")

        elif choice == '4':
            print("Exiting system.")
            break

if __name__ == "__main__":
    main()
