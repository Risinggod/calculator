zahl1=input("geben sie die erste zahl ein")
zahl1=float(zahl1)
zahl2=input("geben sie die zweite zahl ein")
zahl2=float(zahl2)
#funktionen
def operator_1():
    return zahl1 + zahl2
def operator_2():
    return zahl1 - zahl2
def operator_3():
    return zahl1/zahl2
def operator_4():
    return zahl1*zahl2
#continue schleife
powerfile=open("math.txt", "a")
while True:
    operator = input("geben sie einen operaotr (+,-,*,:) ein ein")
    if operator == "+":
        powerfile.write(str(zahl1)+operator+str(zahl2)+"="+str(operator_1()))
        powerfile.write("\n"+"================""\n")
        print(operator_1())
        break
    elif operator == "-":
        powerfile.write(str(zahl1) + operator + str(zahl2) + "=" + str(operator_2()))
        powerfile.write("\n" + "================""\n")
        print(operator_2())
        break
    elif operator=="/":
        powerfile.write(str(zahl1) + operator + str(zahl2) + "=" + str(operator_3()))
        powerfile.write("\n" + "================""\n")
        print(operator_3())
        break
    elif operator == "*":
        powerfile.write(str(zahl1) + operator + str(zahl2) + "=" + str(operator_4()))
        powerfile.write("\n" + "================""\n")
        print(operator_4())
        break
    else:
        powerfile.write("rong awnser lol")
        powerfile.write("\n""================"+"\n")
        print("rong input try agen")
        continue







