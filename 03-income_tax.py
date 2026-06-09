#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate the income tax based on tax slab 2026

# Taking the income from the user
income = float(input("Enter the Annual Income: "))
tax = None
# Determine which slab does that income belong to
if income <= 2_50_000:
    print(f"Tax for the income of Rs.{income} is NIL")
elif income >2_50_000 and income <= 5_00_000:
    tax = income * (5 / 100)
elif income >5_00_000 and income <= 7_50_000:
    tax = income * (10 / 100)
elif income >7_50_000 and income <= 10_00_000:
    tax = income * (15 / 100)
elif income >10_00_000 and income <= 12_50_000:
    tax = income * (20 / 100)
elif income >12_50_000 and income <= 15_00_000:
    tax = income * (25 / 100)
else:
    tax = income * (30 / 100)

if tax != None:
    print(f"Tax for the income of Rs.{income:.2f} is Rs.{tax:.2f}")