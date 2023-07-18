input_time = int(input("Enter Time in 24 Hours Format "))
if(input_time>=5 and input_time <12):
    print("Good Morning")
elif(input_time>=12 and input_time <16):
    print("Good Afternoon")
elif(input_time>=16 and input_time<=20):
    print("Good Evening")
    
elif(input_time>20 and input_time<=24) or (input_time>=0 and input_time<=4):
    print("Good Night")
else:
    print("Invalid Time")
