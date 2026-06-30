temperature = int(input("Enter the temperature in °C: "))

if temperature>= 35:
    print("It's very hot. Wear light cotton clothes and stay hydrated.")
elif temperature>= 25:
    print("It's warm. Light and comfortable clothes are suitable.")
elif temperature>= 18:
    print("The weather is pleasant. Normal clothes are fine.")
else:
    print("It's a bit cool. You may need a light jacket.")