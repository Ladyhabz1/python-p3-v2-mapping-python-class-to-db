#!/usr/bin/env python3
# lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Reset the table
Department.drop_table()
Department.create_table()

# Create departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# Update HR department details
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

# Delete payroll department
print("Deleting Payroll...")
payroll.delete()  # Deletes from database, but object still exists in memory

# Verify deletion in the database
CURSOR.execute("SELECT * FROM departments WHERE id = ?", (payroll.id,))
result = CURSOR.fetchone()
print("Payroll exists in DB:", bool(result))  # Should print False

# Start debugging session
ipdb.set_trace()
