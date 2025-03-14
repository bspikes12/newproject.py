#CIS261 Course Project Brittany Williams

#CIS261 Course Project Brittany Williams

def GetEmpName():
    empName = input("Enter Employee Name: ")
    return empName

def calculate_payroll(hours_worked, hourly_rate, income_tax_rate):
    """Calculate gross pay, income tax, and net pay."""
    gross_pay = hours_worked * hourly_rate
    income_tax = gross_pay * income_tax_rate / 100
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def main():
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_income_taxes = 0
    total_net_pay = 0
    
    # Example predefined values for testing
    example_employees = [
        {"name": "Alice", "hours_worked": 40, "hourly_rate": 25, "income_tax_rate": 20},
        {"name": "Bob", "hours_worked": 35, "hourly_rate": 30, "income_tax_rate": 22},
        {"name": "Charlie", "hours_worked": 45, "hourly_rate": 20, "income_tax_rate": 18},
    ]
    
    for employee in example_employees:
        employee_name = employee["name"]
        hours_worked = employee["hours_worked"]
        hourly_rate = employee["hourly_rate"]
        income_tax_rate = employee["income_tax_rate"]
        
        # Calculate payroll information
        gross_pay, income_tax, net_pay = calculate_payroll(hours_worked, hourly_rate, income_tax_rate)
        
        # Display payroll information for the employee
        print(f"\nPayroll details for {employee_name}:")
        print(f"Hours Worked: {hours_worked}")
        print(f"Hourly Rate: ${hourly_rate}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Income Tax Rate: {income_tax_rate}%")
        print(f"Income Taxes: ${income_tax:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        print("-" * 40)
        
        # Update totals for all employees
        total_employees += 1
        total_hours += hours_worked
        total_gross_pay += gross_pay
        total_income_taxes += income_tax
        total_net_pay += net_pay
    
    # After loop ends, display totals
    print("\nSummary of Payroll Data:")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours Worked: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Income Taxes: ${total_income_taxes:.2f}")
    print(f"Total Net Pay: ${total_net_pay:.2f}")

# Run the program
if __name__ == "__main__":
    main()