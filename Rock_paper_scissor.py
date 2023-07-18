p1 = input("p1 enter 'r' for rock/'p' for paper/'s' for scissors")
p2 = input("p2 enter 'r' for rock/'p' for paper/'s' for scissors")
p1 = p1.lower()
p2 = p2.lower()
if (p1=='r' and p2=='s') or (p1== 's' and p2=='p') or (p1== 'p' and p2=='r'):
    print("The winner is p1")
elif (p1=='p' and p2=='s') or (p1== 'r' and p2=='p') or (p1=='s' and p2=='r'):
    print("The winner is p2")
elif (p1==p2) and (p1=='r'or p1=='p'or p1=='s') and (p2=='r'or p2=='p'or p2=='s'):
    print("its a draw!!!")
else:
    print("error")
