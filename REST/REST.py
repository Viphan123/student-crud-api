from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
students = {
    1: {
        "ID": 1,
        "Name": "Alice Johnson",
        "Grade": "A",
        "Email": "alice.johnson@example.com"
    },
    2: {
        "ID": 2,
        "Name": "Bob Smith",
        "Grade": "B+",
        "Email": "bob.smith@example.com"
    },
    3: {
        "ID": 3,
        "Name": "Charlie Brown",
        "Grade": "A-",
        "Email": "charlie.brown@example.com"
    },
    4: {
        "ID": 4,
        "Name": "Diana Prince",
        "Grade": "B",
        "Email": "diana.prince@example.com"
    },
    5: {
        "ID": 5,
        "Name": "Evan Wright",
        "Grade": "C+",
        "Email": "evan.wright@example.com"
    }
}

# Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

# Retrieve a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = students.get(id)
    return jsonify(student) if student else ('Not found', 404)

# Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students[new_student['ID']] = new_student
    return jsonify(new_student), 201

# Update an existing student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    if id in students:
        students[id].update(request.get_json())
        return jsonify(students[id])
    return ('Not found', 404)

# Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id in students:
        del students[id]
        return ('', 204)
    return ('Not found', 404)

if __name__ == '__main__':
    app.run(debug=True)
