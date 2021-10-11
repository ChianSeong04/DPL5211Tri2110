#Student ID:1201200637
#Student Name:Wee Chian Seong

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print("\tDATA ENTRY\t");
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    id=int(input("Enter staff id : "));
    salary=float(input("Enter staff salary : RM "));
    unit=int(input("Enter total units sold :"));
    bonus=get_bonus(unit,salary)
    nett=get_nett_salary(salary,bonus);
    display(salary,unit,bonus,nett);

def get_bonus(unit,salary):
    if(unit>1000):
        total_bonus=(salary*0.2);
    else:
        total_bonus=(salary*0.1);

    return total_bonus;

def get_nett_salary(salary,bonus):
    total=salary+bonus;
    return total;

def display(salary,unit,bonus,nett):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print("\tSALARY SLIP\t");
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print("Staff ID : {}".format(id));
    print("Staff Salary :RM {:.2f}".format(salary));
    print("Units Sold : {}".format(unit));
    print("Bonus :RM {:.2f}".format(bonus));
    print("Nett Salary:RM {:.2f}".format(nett));

main();