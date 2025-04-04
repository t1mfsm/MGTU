import sys

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит на сумму {amount} успешно выполнен.")
        else:
            print("Ошибка: Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Снятие на сумму {amount} успешно выполнено.")
        else:
            print("Ошибка: Недостаточно средств на счете или сумма должна быть положительной.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Счет {self.account_number} на имя {self.account_holder}, баланс: {self.balance}"

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

    account = BankAccount(account_number, account_holder, initial_balance)

    print(account)

    while True:
        print("\nВыберите действие:")
        print("1. Внести депозит")
        print("2. Снять средства")
        print("3. Проверить баланс")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = float(input("Введите сумму депозита: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Текущий баланс: {account.get_balance()}")
        elif choice == "4":
            break
        else:
            print("Ошибка: Неверный выбор действия.")

if __name__ == "__main__":
    main()
