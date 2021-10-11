#Student ID:1201200637
#Student Name:Wee Chian Seong

def my_function(name,contact,salary,overtime):
    print("Hello",name);
    print("This is my phone number :",contact);
    total=float(salary)+ float(overtime)
    print("Your salary this month is RM {:.2f}".format(total))

my_function("Shawn Wee","1246",4000,500);