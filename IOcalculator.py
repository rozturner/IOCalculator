# Implied Odds (IO) calculator for EPs
# Created by Roz Turner, 2022
# IO formula = (EP profit/QL) + 1

def calculateIO(x, y):
    return (x/y)+1

#Enter values
print("Welcome to the Implied Odds (IO) Calculator!")    

while True:
    profit = float(input("Enter EP profit: "))
    ql = float(input("Enter QL (as a positive integer): "))
    print("EP profit = ",profit)
    print("QL = ",ql)
    
    #calculate
    print("IO = ", calculateIO(profit,ql))
    again = input("New calculation? (y/n): ")
    if again == "y":
        continue
    else:
        print("Later!")
        break