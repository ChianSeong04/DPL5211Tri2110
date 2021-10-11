#Student ID:1201200637
#Student Name:Wee Chian Seong
def main():
    length=float(input("Enter Length :"));
    width=float(input("Enter Width :"));
    re=rectangle(length,width);
    te=triangle(length,width);
    print("Reactangle area : {:.2f}".format(re));
    print("Triangle area : {:.2f}".format(te));
    

def rectangle(length,width):
    area=length*width;
    return area;

def triangle(length,width):
    area=0.5*length*width;
    return area;
i=0
while(i<2):
    main();
    i=i+1