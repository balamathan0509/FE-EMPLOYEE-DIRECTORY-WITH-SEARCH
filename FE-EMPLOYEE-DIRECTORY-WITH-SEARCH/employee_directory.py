# Employee Directory with Search - Simple Demo
employees = [
    {"emp_id": "E101", "name": "Bala", "department": "CSE", "designation": "Developer"},
    {"emp_id": "E102", "name": "Mathan", "department": "IT", "designation": "Analyst"},
    {"emp_id": "E103", "name": "Kavin", "department": "ECE", "designation": "Designer"},
    {"emp_id": "E104", "name": "Arun", "department": "MECH", "designation": "Tester"}
]

def search_employee(query):
    results = [emp for emp in employees if query.lower() in emp["name"].lower() or query.lower() in emp["department"].lower()]
    return results

print("=== Employee Directory ===")
query = input("Enter name or department to search: ")
results = search_employee(query)

if results:
    for emp in results:
        print(f"ID: {emp['emp_id']}, Name: {emp['name']}, Dept: {emp['department']}, Role: {emp['designation']}")
else:
    print("No matching employee found.")
