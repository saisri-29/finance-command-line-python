import json

class PersonalFinanceManager:
    def __init__(self):
        self.balance = 0.0
        self.income = []  # Initialize the income list
        self.expenses = []
        self.load_data()

    def load_data(self):
        try:
            with open('finance_data.json', 'r') as file:
                data = json.load(file)
                self.balance = data.get('balance', 0.0)
                self.income = data.get('income', [])
                self.expenses = data.get('expenses', [])
        except FileNotFoundError:
            self.save_data()  # Create a new file if it doesn't exist

    def save_data(self):
        data = {
            'balance': self.balance,
            'income': self.income,
            'expenses': self.expenses
        }
        with open('finance_data.json', 'w') as file:
            json.dump(data, file)

    def add_income(self, amount, source):
        if amount < 0:
            print("Income amount must be positive.")
            return
        self.income.append({'amount': amount, 'source': source})
        self.balance += amount
        self.save_data()
        print(f"Added income: {amount} from {source}")

    def add_expense(self, amount, category):
        if amount < 0:
            print("Expense amount must be positive.")
            return
        self.expenses.append({'amount': amount, 'category': category})
        self.balance -= amount
        self.save_data()
        print(f"Added expense: {amount} for {category}")

    def view_balance(self):
        print(f"Current balance: {self.balance}")

    def view_income(self):
        print("Income:")
        for entry in self.income:
            print(f"Source: {entry['source']}, Amount: {entry['amount']}")

    def view_expenses(self):
        print("Expenses:")
        for entry in self.expenses:
            print(f"Category: {entry['category']}, Amount: {entry['amount']}")

def main():
    manager = PersonalFinanceManager()
    
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Income")
        print("5. View Expenses")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter income amount: "))
                source = input("Enter income source: ")
                manager.add_income(amount, source)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                manager.add_expense(amount, category)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        elif choice == '3':
            manager.view_balance()
        elif choice == '4':
            manager.view_income()
        elif choice == '5':
            manager.view_expenses()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
