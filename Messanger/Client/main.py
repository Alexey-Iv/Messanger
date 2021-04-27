import registration as reg   # Модуль в котором есть функции регистрации и вхождения в аккаунт

# Цикл приложения

def main():
    print("Вы зарегестрированы? ", end='')
    answer = input()
    if (answer == "yes" or answer =="1"):
        reg.log_in()
    elif (answer == "no" or answer == "0"):
        reg.registration()
        reg.log_in()

if __name__ == "__main__":
    main()

# By AID