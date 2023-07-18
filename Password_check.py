inp_pass = input("enter your password")
symbols = ['•',"'",'!','@','#' ,'$','%','^','&', '*','(',')','+', '=','_','-','{','}','[',']',':',';','"', "'",'?','<','>',',','.']
len_flag = False
upper_flag = False
lower_flag = False
num_flag = False
repeated_char = False
special_char = False
if len(inp_pass)>=6 and len(inp_pass)<=24:
    len_flag = True
    for item in inp_pass:
        if item.isupper():
            upper_flag =True

        if item.islower():
            lower_flag = True

        if item.isnumeric():
            num_flag = True

        if inp_pass.count(item) > 2:
            repeated_char = True

        if item in symbols:
            special_char = True

if (len_flag == True and upper_flag == True and lower_flag == True and num_flag == True and repeated_char ==False and special_char == True ):
    print("True//password is ok")
else:
    print("False//password not ok")
