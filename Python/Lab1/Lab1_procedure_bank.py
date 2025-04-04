import sys

def create_account(account_number, account_holder, balance=0):
    return {
        "account_number": account_number,
        "account_holder": account_holder,
        "balance": balance
    }

def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        print(f"Депозит на сумму {amount} успешно выполнен.")
    else:
        print("Ошибка: Сумма депозита должна быть положительной.")

def withdraw(account, amount):
    if amount > 0 and amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Снятие на сумму {amount} успешно выполнено.")
    else:
        print("Ошибка: Недостаточно средств на счете или сумма должна быть положительной.")

def get_balance(account):
    return account["balance"]

def main():
    if len(sys.argv) == 4:
        account_number = sys.argv[1]
        account_holder = sys.argv[2]
        initial_balance = float(sys.argv[3])
    elif len(sys.argv) == 1:
        account_number = input("Введите номер счета: ")
        account_holder = input("Введите имя владельца счета: ")
        initial_balance = float(input("Введите начальный баланс счета: "))
    else:
        print("Использование: python bank_account.py <номер_счета> <имя_владельца> <начальный_баланс>")
        sys.exit(1)

    account = create_account(account_number, account_holder, initial_balance)

    print(f"Счет {account['account_number']} на имя {account['account_holder']}, баланс: {account['balance']}")

    while True:
        print("\nВыберите действие:")
        print("1. Внести депозит")
        print("2. Снять средства")
        print("3. Проверить баланс")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = float(input("Введите сумму депозита: "))
            deposit(account, amount)
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            withdraw(account, amount)
        elif choice == "3":
            print(f"Текущий баланс: {get_balance(account)}")
        elif choice == "4":
            break
        else:
            print("Ошибка: Неверный выбор действия.")

if __name__ == "__main__":
    main()
