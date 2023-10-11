import re

def validate_aadhar_number(aadhar_number):
    pattern = re.compile(r'^\d{12}$')
    return bool(pattern.match(aadhar_number))

def validate_address(address):
    pattern = re.compile(r'^[A-Za-z0-9\s,.\'-]+$')
    return bool(pattern.match(address))

def validate_age(age):
    pattern = re.compile(r'^[0-9][0-9]$')
    return bool(pattern.match(age))

def validate_city(city):
    pattern = re.compile(r'^[A-Za-z\s-]+$')
    return bool(pattern.match(city))

def validate_department_name(department_name):
    pattern = re.compile(r'^[A-Za-z0-9\s,.\'-]+$')
    return bool(pattern.match(department_name))

def validate_designation(designation):
    pattern = re.compile(r'^[A-Za-z0-9\s,.\'-]+$')
    return bool(pattern.match(designation))

def validate_dob(dob):
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(pattern.match(dob))

def validate_doj(doj):
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(pattern.match(doj))

def validate_employee_id(employee_id):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    return bool(pattern.match(employee_id))

def validate_employee_name(employee_name):
    pattern = re.compile(r'^[A-Za-z]+$')
    return bool(pattern.match(employee_name))

def validate_gender(gender):
    pattern = re.compile(r'^(Male|Female|Other)$')
    return bool(pattern.match(gender))

def validate_pancard_number(pancard_number):
    pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
    return bool(pattern.match(pancard_number))

def validate_salary(salary):
    if salary.isdigit():
      return True
    else:
      return False
