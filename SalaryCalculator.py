def calculate_salary(basicpay, allowance=5000):
    salary = basicpay + allowance
    return salary
def total_salary(*salary):
    total_salary = 0
    for sal in salary:
        total_salary =  total_salary + sal
    return total_salary
