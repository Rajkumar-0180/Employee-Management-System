from flask import Flask, request, jsonify

app = Flask(__name__)

employees = []

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/add', methods=['POST'])
def add_employee():
    data = request.json
    employees.append(f"{data['emp_id']}: {data['name']}, Age: {data['age']}, Department: {data['department']}")
    return jsonify({"message": "Employee added successfully!"})

@app.route('/search/<int:emp_id>', methods=['GET'])
def search_employee(emp_id):
    for emp in employees:
        if emp.startswith(f"{emp_id}:"):
            return jsonify({"employee": emp})
    return jsonify({"message": "Employee not found!"}), 404

@app.route('/delete/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if not emp.startswith(f"{emp_id}:")]
    return jsonify({"message": "Employee deleted successfully!"})

@app.route('/employees', methods=['GET'])
def get_all_employees():
    return jsonify({"employees": employees})

if __name__ == '__main__':
    app.run(debug=True)
