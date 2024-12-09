manage_employ = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/manage_employee.txt'
try:
    with open(manage_employ, 'r') as file:
        employees = file.readlines()
        if employees:
            print("\nEmployee Accounts:")
            for line in employees:
                employee_name, employee_email, employee_id, employee_password = line.strip().split(', ')
                print(f"Name: {employee_name}, Email: {employee_email}, ID: {employee_id}")
        else:
            print("No employee found")
except FileNotFoundError:
    print("No employee records found.")
