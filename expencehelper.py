expences=[]
def expence_entry():
    title=input("Enter the title of expence")
    amount=input("Enter the amount of expence")
    date=input("Enter the date of expence")
    expences.append((title,amount,date))
def display_expences():
    for expence in expences:
            print(expence[0]+" "+expence[1]+" "+expence[2])