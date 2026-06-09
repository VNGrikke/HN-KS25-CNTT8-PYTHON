employee = {
    "employee_id": "NV001",
    "full_name": "Nguyen Van An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]

full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Ma nhan vien:", employee_id)
print("Ho ten nhan vien:", full_name)
print("Thong tin nhan vien sau xu ly:", employee)