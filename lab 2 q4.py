#Student ID:1201200637
#Student Name:Wee Chian Seong
BNN=1.50
GP=5.6
print("Invoice for Fruits Purchase")
print("---------------------------")
qtybnn=float(input("Enter the quantity(comb) of banana bought:"))
qtygp=float(input("Enter the amount (kg) of grapes bought:"))
totalbnn=qtybnn*BNN
totalgp=qtygp*GP
total=totalbnn+totalgp
print("Item         Qty          Price         Total")
print("Banana(comb) {}           RM{:.2f}      RM{:.2f}".format(qtybnn,BNN,totalbnn))
print("Grapes(kg)   {}           RM{:.2f}      RM{:.2f}".format(qtygp,GP,totalgp))

print("Total RM{:.2f}".format(total))