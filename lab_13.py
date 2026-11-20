
# CSV Payroll Management System

import csv
import os

filename = "payroll.csv"

while True:
    print("\n--- PAYROLL MANAGEMENT ---")
    print("1. Add Employee")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        salary = float(input("Enter basic salary: "))

        tax = salary * 0.10
        net_salary = salary - tax

        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(filename) == 0:
                writer.writerow(["Name", "Salary", "Tax", "Net Salary"])

            writer.writerow([name, salary, tax, net_salary])

        print("Employee payroll saved!")

    elif choice == "2":
        print("\n--- PAYROLL RECORDS ---")

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(" | ".join(row))

        except FileNotFoundError:
            print("No payroll records found!")

    elif choice == "3":
        print("Payroll system closed!")
        break

    else:
        print("Invalid choice!")
