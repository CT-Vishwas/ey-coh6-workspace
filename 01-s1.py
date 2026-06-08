# principal = 300000
# time_in_months = 36
# rate_of_interest = 0.07
principal = float(input("Enter the principal amount: "))
time_in_months = int(input("Enter the time in months: "))
rate_of_interest = float(input("Enter the rate of interest: ")) / 100


simple_interest = (principal * time_in_months * rate_of_interest)/100
print(f"The Simple interest for Rs.{principal} for {time_in_months} months at {rate_of_interest*100:.2f}% is Rs.{simple_interest:.2f} ")