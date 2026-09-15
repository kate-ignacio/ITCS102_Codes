age = int(input(" Enter your age ---> "))
is_employed = bool(input(" Are you currently employed ---> "))
credit_score = int(input(" Credit score ---> "))
annual_income = float(input(" How much is your annual income ---> "))
has_collateral = bool(input(" Do you have any collateral ---> "))


if age >= 21 and is_employed == True:
    print("Accepted")
    if credit_score >= 750: 
        print(" You have a high credot score")
        if annual_income >= 100000:
            print(" You have a high annual income")
            if has_collateral == True:
             base_rate = 4.5
             print(" Your base rate is", base_rate) 
            else:
               base_rate = 5.0
            print(" Your base rate is", base_rate)
    elif credit_score >= 600 and credit_score < 750:
       print("Your credit score is less than 750 ")
       if has_collateral == True:
          print("You have collateral")
          base_rate = 7.0 
          print("Your base rate is", base_rate)
       elif annual_income <= 40000:
          print("Low annual income")
          base_rate = 9.5
          print("Your base rate is", base_rate)
       else:
          base_rate = 8.0
          print("Your base rate is", base_rate)
    elif credit_score <= 600:
       print("Rejected: Credit score too low")
    else:
       print("Invalid details")
else:
    print("sorry")
