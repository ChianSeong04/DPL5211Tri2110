#Student ID:1201200637
#Student Name:Wee Chian Seong

def main():
    print("=====================");
    print("\t Main Menu \t");
    print("=====================");
    print("1. Convert centimeter to meter");
    print("2. Convert meter to centimeter");
    choice=int(input("Enter your choice: "));
    if(choice==1):
        get_cm();
    elif(choice==2):
        get_meter();
    else:
        print("Invalid Choice");

def cm_to_meter(cm):
    meter= cm/100;
    return meter;
    
def get_cm():
    cm= float(input("Enter Centimenter : "));
    m=cm_to_meter(cm);
    print("{:.2f} centimeter equals to {:.2f} meter".format(cm,m))

def get_meter():
    meter=float(input("Enter Meter : "));
    cm=meter_to_cm(meter);
    print("{:.2f} meters equals to {:.2f} centimeters2".format(meter,cm));

def meter_to_cm(meter):
    cm=meter*100;
    return cm;

main();