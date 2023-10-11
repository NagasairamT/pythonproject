from validate import (
    validate_aadhar_number,
    validate_address,
    validate_age,
    validate_city,
    validate_department_name,
    validate_designation,
    validate_dob,
    validate_doj,
    validate_employee_id,
    validate_employee_name,
    validate_gender,
    validate_pancard_number,
validate_salary
)

class Employee:
  EmpDict = {}

  def __init__(self, employee_id, employee_name, salary, age, gender, address,
               city, dob, doj, department_name, designation, pancard_number,
               aadhar_number):
    self.employee_id = employee_id
    self.employee_name = employee_name
    self.salary = salary
    self.age = age
    self.gender = gender
    self.address = address
    self.city = city
    self.dob = dob
    self.doj = doj
    self.department_name = department_name
    self.designation = designation
    self.pancard_number = pancard_number
    self.aadhar_number = aadhar_number
    if self.employee_name in self.EmpDict:
      self.EmpDict[self.employee_name].append(self.employee_name)
    else:
      self.EmpDict[self.employee_name] = [self.employee_name]

  def display(self):
    print(self.employee_id, " ", self.employee_name, " ", self.salary, " ",
          self.age, " ", self.department_name, " ", self.designation, " ",
          self.aadhar_number)

  @classmethod
  def EmployeeDetails(cls):
    for k, v in cls.EmpDict.items():
      print(k, "=", v)

EmployeeList = []
while True:
  print("")
  print("1: Press 1 for Add the record of Employee")
  print("2: Press 2 for Delete the record of Employee")
  print("3: Press 3 for Update Employee Details")
  print("4: Press 4 for Search details of Employee")
  print("5: Press 5 for Employee Details")
  print("6: Press 6 for Display the details of Employee with highest salary")
  print("7: Press 7 for Display the details of Employee with lowest salary:")
  print("8: Press 8 for  Exit:")
  choice = int(input("Enter your choice: "))

  if choice == 1:

    employee_id = input("Enter EmployeeidNumber: ")
    if not validate_employee_id(employee_id):
      print("Invalid input try again employee id")
      continue

    employee_name = input("Enter Employee name: ")
    if not validate_employee_name(employee_name):
      print("Invalid input try again employee name")
      continue

    age = int(input("Enter the age: "))
    if not validate_age(str(age)):
      print("Invalid input try again age")
      continue

    gender = input("Enter the gender: ")
    if not validate_gender(gender):
      print("Invalid input try again with gender")
      continue

    address = input("Enter the address: ")
    if not validate_address(address):
      print("Invalid input try again the address")
      continue

    city = input("Enter the city: ")
    if not validate_city(city):
      print("Invalid input try again the city")
      continue

    dob = input("Enter the dob: ")
    if not validate_dob(dob):
      print("Invalid input try again the dob")
      continue

    doj = input("Enter the doj: ")
    if not validate_doj(doj):
      print("Invalid input try again the doj")
      continue

    department_name = input("Enter the department_name: ")
    if not validate_department_name(department_name):
      print("Invalid input try again the department_name")
      continue

    designation = input(
        "Enter the Designation (IT || HR || Finance || Marketing): ")
    if not validate_designation(designation):
      print("Invalid input try again the designation")
      continue
      
    salary=input("enter the salary")
    if not validate_salary(salary):
      print("Invalid input try again the salary")
      continue

    pancard_number = input("Enter the pancard number: ")
    if not validate_pancard_number(pancard_number):
      print("Invalid input try again the pancard number")
      continue

    aadhar_number = input("Enter the aadhar number: ")
    if not validate_aadhar_number(aadhar_number):
      print("Invalid input try again the aadhar number")
      continue
    obj = Employee(
    employee_id,
    employee_name,
    salary,
    age,
    gender,
    address,
    city,
    dob,
    doj,
    department_name,
    designation,
    pancard_number,
    aadhar_number,
)
    EmployeeList.append(obj)
  elif choice == 5:
    for i in EmployeeList:
      i.display()

  elif choice == 4:
    print("press A:To search by Employee ID")
    print("press B:To Search by Employee Name")
    print("press C:To Search by Department Name")
    ch = input("Enter your choice")
    if ch == "A":
      k = input("enter Employee ID to be searched")
      for i in EmployeeList:
        if i.employee_id == k:
          i.display()
    elif ch == "B":
      m = input("enter Employee name to be searched")
      for i in EmployeeList:
        if i.employee_name == m:
          i.display()
    elif ch == "C":
      n = input("enter Department name to be searched")
      for i in EmployeeList:
        if i.department_name == n:
          i.display()

    else:
      print("Invalid Choice")

  elif choice == 2:
    print("press A:To delete the record by Employee ID")
    print("press B:To delete the record by Employee Name")
    ch = input("enter the choice")
    if ch == "A":
      p = input("enter Employee ID to be Deleted")
      for i in EmployeeList:
        if i.employee_id == p:
          EmployeeList.remove(i)
    elif ch == 'B':
      pass

  elif choice == 8:
    exit()

  elif choice == 3:
    print("Press A: To Update name of Employee")
    print("Press B: To Update address of Employee")
    print("Press C: To Update DOB of Employee")
    print("Press D:To update Salary Of Employee")
    ch = input("Enter your choice: ")
    if ch == "A":
      name = input("Enter new name: ")
      employee_id = input("Enter Employee ID: ")
      for i in EmployeeList:
        if i.employee_id == employee_id:
          i.employee_name = name
          print("Name updated successfully!")
          break
    elif ch == "B":
      address = input("Enter new address: ")
      employee_id = input("Enter Employee ID: ")
      for i in EmployeeList:
        if i.employee_id == employee_id:
          i.address = address
          print("Address updated successfully!")
          break
    elif ch == "C":
      dob = input("Enter new DOB: ")
      employee_id = input("Enter Employee ID: ")
      for i in EmployeeList:
        if i.employee_id == employee_id:
          i.dob = dob
          print("DOB updated successfully!")
          break
    elif ch == "D":
      print("Press A: Update the salary of specific Employee by Employee id.")
      print(
          "Press B: Update the salary of all Employees working in specific department"
      )
      print("Press C: Update the salary of all Employees")
      ch = input("enter the choice")
      if ch == "A":
        salary = input("enter the salary of employee")
        employee_id = input("enter the employee id")
        for i in EmployeeList:
          if i.employee_id == employee_id:
            i.salary = salary
            print("salary got updated sucessfully")
            break
      elif ch == "B":
        salary = input("enter the salary of employee")
        department_name = input("enter the department")
        for i in EmployeeList:
          if i.department_name == department_name:
            i.salary = salary
            print("salary got updated sucessfully by department name")
            break
      elif ch == "C":
        salary = input("enter the salary")
        for emp in EmployeeList:
          emp.salary = salary
          print("salary updated successfully for all employees!!")
          break
      else:
        print("Invalid Choice")
  elif choice ==6:
    max_salary = max(EmployeeList, key=lambda emp: emp.salary)
    max_salary.display()
    break
  elif choice==7:
    min_salary=min(EmployeeList,key=lambda emp:emp.salary)
    min_salary.display()
    break

  else:
    print("Invalid Choice")
