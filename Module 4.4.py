import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(operation, x1, x2):
    if operation == 1:
        logging.info("Dodaję " + str(x1) + " i " + str(x2))
        print("Wynik to " + str(x1+x2))
    elif operation == 2:
        logging.info("Odejmuję " + str(x2) + " od " + str(x1))
        print("Wynik to " + str(x1-x2))
    elif operation == 3:
        logging.info("Mnożę " + str(x1) + " i " + str(x2))
        print("Wynik to " + str(x1*x2))
    elif operation == 4:
        logging.info("Dzielę " + str(x1) + " przez " + str(x2))
        print("Wynik to " + str(x1/x2))
    

if __name__ == "__main__":
    input_operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    x1 = input("Podaj pierwszą liczbę:")
    x2 = input("Podaj drugą liczbę:")
    print(calculator(input_operation, float(x1), float(x2)))