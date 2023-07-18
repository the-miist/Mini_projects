inp_units = int(input("enter number of units consumed"))

if inp_units>0 and inp_units<=100:
    cost = inp_units*1

elif inp_units>100 and inp_units<=200:
    over_units = inp_units - 100
    cost = 100*1 +  over_units*2

elif inp_units>200 and inp_units<=300:
    over_units = inp_units - 200
    cost = 100*1 + 100*2 + over_units*3

elif inp_units>300 and inp_units<=500:
    over_units = inp_units - 300
    cost = 100*1 + 100*2 + 100*3 + over_units*4
    
elif inp_units>500:
    over_units = inp_units - 500
    cost = 100*1 + 100*2 + 100*3 + 200*4 + over_units*5

bill = cost + (0.10*cost) + 15
print(bill)
