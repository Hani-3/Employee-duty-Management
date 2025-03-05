# from flask import Flask, render_template, request

# app = Flask(__name__)

# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.hours = 0

#     def add_hours(self, hours):
#         self.hours += hours

#     def __str__(self):
#         return f"{self.name}: {self.hours} hours"

# # Initialize employees
# employees = [
#     Employee("N.S. Patel"),
#     Employee("A.S. Tiwari"),
#     Employee("D.F. Shah"),
#     Employee("G.D. Arora"),
#     Employee("R.S. Patel"),
#     Employee("H.P. Patel")
# ]

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         # Get selected employees from the form
#         on_leave_index = int(request.form.get("on_leave"))
#         on_duty_index = int(request.form.get("on_duty"))

#         # Validate selection
#         if on_leave_index == on_duty_index:
#             return "Error: The same employee cannot be on leave and duty at the same time.", 400
        
#         # Adjust hours
#         employees[on_leave_index].add_hours(-8)
#         employees[on_duty_index].add_hours(8)

#     # Render the template with updated employee data
#     return render_template("index.html", employees=employees)

# if __name__ == "__main__":
#     app.run(debug=True)













from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

class Employee:
    def __init__(self, name):
        self.name = name
        self.hours = 0

    def add_hours(self, hours):
        self.hours += hours

    def __str__(self):
        return f"{self.name}: {self.hours} hours"

# Initialize employees
employees = [
    Employee("N.S. Patel"),
    Employee("A.S. Tiwari"),
    Employee("D.F. Shah"),
    Employee("G.D. Arora"),
    Employee("R.S. Patel"),
    Employee("H.P. Patel")
]

last_updated = None  # Store the last updated timestamp

@app.route("/", methods=["GET", "POST"])
def index():
    global last_updated  # Use global to update the timestamp

    if request.method == "POST":
        # Get selected employees from the form
        on_leave_index = int(request.form.get("on_leave"))
        on_duty_index = int(request.form.get("on_duty"))

        # Validate selection
        if on_leave_index == on_duty_index:
            return "Error: The same employee cannot be on leave and duty at the same time.", 400
        
        # Adjust hours
        employees[on_leave_index].add_hours(-8)
        employees[on_duty_index].add_hours(8)

        # Update the timestamp
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html", employees=employees, last_updated=last_updated)

if __name__ == "__main__":
    app.run(debug=True)
