class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return 0 if node is None else node.height

    def get_balance(self, node):
        return 0 if node is None else self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, employee):
        if not root:
            return Employee(employee.emp_id, employee.name, employee.age, employee.department)

        if employee.emp_id < root.emp_id:
            root.left = self.insert(root.left, employee)
        elif employee.emp_id > root.emp_id:
            root.right = self.insert(root.right, employee)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and employee.emp_id < root.left.emp_id:
            return self.right_rotate(root)
        if balance < -1 and employee.emp_id > root.right.emp_id:
            return self.left_rotate(root)

        return root

    def search(self, root, emp_id):
        if root is None or root.emp_id == emp_id:
            return root
        if emp_id < root.emp_id:
            return self.search(root.left, emp_id)
        return self.search(root.right, emp_id)
