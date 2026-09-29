age = int(input("What is your sge? --> "))
rev = float(input("Your monthly revenue: "))
cc = int(input(" Your credit score; "))
yb = float(input(" Years in business ---> "))
hd = bool(input(" Filed for bankruptcy ---> "))
collateral = str(input(" Collateral name : "))
collateral_val = float(input("Your collateral value ---> "))

max_loan = 0
base_fee = 0

if age >= 21 and hd == False and yb >= 2.0: #tier1
    print("BASELINE PASSED")
    if cc >= 720:
        print("CREDIT SCORE CONSIDERED HIGH")
        max_loan = rev * 3
        if rev >= 50000:
           print("ABOVE 50K REVENUE")
           base_fee = max_loan * 0.015 
           print("BASE FEE IS SET TO ",base_free)
        else:
            print("REVENUE BELOW 50K")
            base_fee = max_loan * 0.025
            print("BASE FEE IS SET TO ",base_fee)

        #collateral
        if collateral_val >= max_loan:
         print("COLLATERAL ",collateral," with a value of ,"collateral_val ", is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for ", collateral)

        #surcharge
        if collateral_val % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE, total base fee is ", base_fee)
        else:
            print("collateral value divisible by 5000")


    elif cc <= 620 and cc < 720: #tier2
        print("Credit score within range of 620 to 720")
        max_loan = rev * 1.5
        if yb >= 5.0:
            base_fee = max_loan * 0.02
            print("Years in business greater then 5 years base fee is ", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Years in business lower than 5 years base feee is ", base_fee)

#collateral
        if collateral_val >= max_loan:
            print("COLLATERAL ",collateral", with a value of", collateral_val ", is ACCEPTED ")
        else:
            print("Rejected: Insufficient collateral value for ", collateral)

        #surcharge
        if collateral_val % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE, total base fee is ", base_fee)
        else:
            print("collateral value divisible by 5000")

    elif cc < 620: #tier3
        print("Credit score too low")
    else:
        print("INVALID")

else:
    print("BASELINE FAILED")
