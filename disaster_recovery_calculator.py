import csv
def calculate():
    file=input("Type the file name: ")
    with open(f'{file}.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Asset Name','Asset Value', 'Exposure Factor Risk', 'Single Loss Expectancy', 'Times', 'Years', 'Annualized Loss Expectancy'])
    cicle = True
    while cicle is True:
        print("Disaster Recovery Calculator\n")
        asset=input("Insert the name of the asset:\n")
        AV = float(input("AV -> Asset Value:\n$"))
        EF = int(input("EF -> Exposure Factor Risk of asset:\n%"))
        EFc = EF/100
        SLE = AV * EFc
        print("""

ARO -> Annualized Rate of Occurrence:

Set X and Y VALUES:

X times every Y years

        """)
        X=input("Set X value: ")
        Y=input("Set Y value: ")
        ARO=float(int(X)/int(Y))
        ALE = SLE * ARO
        print("The ALE is: $ ", ALE)
        with open(f'{file}.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([asset,AV, EF, SLE, X, Y, ALE])
        usrin=input("Continue? Y/n: ")
        if usrin=='Y' or usrin=='y':
            continue
        else:
            cicle = False
calculate() # Start to calculate
