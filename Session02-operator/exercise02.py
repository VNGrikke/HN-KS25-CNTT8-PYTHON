print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    
    print("Reason for rejection: ", end="")
    if donor_age < 18 and donor_weight < 50:
        print("Donor is under 18 years old AND weighs less than 50 kg.")
    elif donor_age < 18:
        print("Donor is under 18 years old.")
    elif donor_weight < 50:
        print("Donor weighs less than 50 kg.")