salary = float(input("Please Enter your monthly salary: PHP"))
default = float(30000.00)
if ( salary >= default ) : 
   print( "Congrats you are eligable for a loan! ")
   loan = float(input("Enter Amount you wish to loan: PHP"))
   if(loan <= 10 * salary):
      payment = int(input("Please choose how many months for your payment term: "))
      interest = loan * 0.10
      total = loan +interest 
      monthly = total / payment 
      print(f"\nLoan Amount: PHP {loan:.2f}")
      print(f"interest (10%); PHP {interest:.2f}")
      print(f"Total Amount to Pay: PHP {total:.2f}")
      print(f"Monthly Payment for {payment} Months: PHP{monthly:.2f}")
   
   else: print("Cannot avail loan as your requested amount exceed 10 times your monthly salary")
else:print("You are not eligible monthly salary too low to avail a loan")