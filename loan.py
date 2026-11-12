#loan
loan_amt = float(input(" enter amount --> ")) #target 1
years = int(input(" enter year to pay -->  ")) #loan application

month = years * 12
principal = loan_amt/month
remaining_bal = loan_amt

print("MONTH\t|\tPAYMENT\t\t|\tINTEREST\t|\tPRINCIPAL\t|\tBALANCE\t\t|")
for x in range ( 1, month+1) :
    remaining_bal -= principal
    loan_interest = remaining_bal * 0.00256
    monthly_pay = loan_interest + principal
    #print(x, round(monthly_pay), round(loan_interest), round(principal,2), round(remaining_bal,2))

    #string formatting
    print(f"|{x} \t|\t {round(monthly_pay,2)} \t\t| \t {round(loan_interest,2)} \t\t|\t {round(principal,2)} \t\t|\t {round(remaining_bal,2)}\t\t|")

