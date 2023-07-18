cigars = int(input('enter number of cigars'))
day = input("enter we for weekend or enter wd for week days")
day = day.lower()
if (cigars>=40 and cigars<=60) and (day == 'wd'):
    print('true')
elif (cigars>=40 and day == 'we'):
    print('true')
else: 
    print('false')
