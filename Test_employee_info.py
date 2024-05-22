import employee_info

def test_get_employees_by_age_range():
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    result = []
    result = employee_info.get_employees_by_age_range(22,24)

    assert (result == [{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}])

def test_calculate_average_salary():
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    result = employee_info.calculate_average_salary()

    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    result = []
    result = employee_info.get_employees_by_dept("Engineering")

    assert (result == [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},{"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}])
