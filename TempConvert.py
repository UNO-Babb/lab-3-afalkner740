#TempConvert.py
#Name:Alexa Falkner
#Date:09-14-2025
#Assignment:TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  Temp= int(input("What temperature in Fahrenheit? "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  print("The Celsius value is: ")
  temp=((Temp - 32)/1.8)
  num = round(temp, 1)
  print(num , "degrees")
  #Output converted temperature.
  tempF = 80

  tempC = tempF / 2

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
