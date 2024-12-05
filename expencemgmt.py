from expencehelper import *
y=0
while(y==0):
    print("1 for insert expence")
    print("2 for display expence")
    opt=int(input("Enter the option"))
    if(opt==1):
       expence_entry() 
    if(opt==2):
       display_expences() 
    y=int(input("Do you want to continue?0 for yes"))