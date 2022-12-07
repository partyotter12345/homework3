#congress.py
#HMWK_3


age = int(input("What is your age? "))
citizen_years = int(input("How many years have you been a citizen? "))

# Determine eligibility
if age >= 30 and citizen_years >= 9:
  print("You are eligible for both the House and Senate.")
elif age >= 25 and citizen_years >= 7:
  print("You eligible only for the House.")
else:
  print("You are ineligible for Congress.")
