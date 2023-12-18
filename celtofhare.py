temp=float(input("Enter the temperature: "))
Celsius_or_Fharenheit=input("Enter Celsius(C) or Fharenheit(F): ")

if(Celsius_or_Fharenheit=='C'):
    Fharenheit=(temp*1.8)+32
    print(Fharenheit)

else:
    Celsius=(temp-32)*5/9
    print(Celsius)