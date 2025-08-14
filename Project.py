lass IncomeManager:
    """
    A class to manage monthly income, savings, and expenses.
    """
    def __init__(self, monthly_income):
        """Initializes the manager with a starting monthly income."""
        self.monthly_income = monthly_income
        self.expenses = []
        self.savings = 0.0

    def add_expense(self, name, amount):
        """Adds a new expense to the list."""
        if amount > 0:
            self.expenses.append({"name": name, "amount": amount})
            print(f"✅ Added expense: {name} - ${amount}")
        else:
            print("❌ Error: Expense amount must be greater than zero.")

    def set_savings(self, amount):
        """Sets the monthly savings amount."""
        if amount >= 0:
            self.savings = amount
            print(f"💰 Monthly savings goal set to: ${amount}")
        else:
            print("❌ Error: Savings amount cannot be negative.")

    def get_total_expenses(self):
        """Calculates and returns the total amount spent on expenses."""
        return sum(item['amount'] for item in self.expenses)

    def get_balance(self):
        """Calculates and returns the remaining balance after savings and expenses."""
        total_expenses = self.get_total_expenses()
        balance = self.monthly_income - total_expenses - self.savings
        return balance

    def show_summary(self):
        """Prints a detailed summary of the finances."""
        total_expenses = self.get_total_expenses()
        balance = self.get_balance()

        print("\n--- Monthly Financial Summary ---")
        print(f"📈 Monthly Income: ${self.monthly_income:.2f}")
        print(f"💰 Savings Goal:   ${self.savings:.2f}")
        print(f"🛒 Total Expenses: ${total_expenses:.2f}")
        print("-------------------------------")
        print(f"💵 Remaining Balance: ${balance:.2f}")

        # Check for budget issues
        if balance < 0:
            print("\n⚠️  Warning: Your total spending (expenses + savings) exceeds your income.")
        elif balance == 0:
            print("\n👍  You have a perfectly balanced budget!")
        else:
            print("\n🎉  You've stayed within your budget!")


# --- Interactive Program ---
def main():
    try:
        # Get monthly income from the user
        income = float(input("Enter your monthly income: $"))
        if income <= 0:
            print("Monthly income must be a positive number. Exiting.")
            return
        
        my_budget = IncomeManager(income)

        # Get monthly savings goal
        savings_goal = float(input("Enter your monthly savings goal: $"))
        my_budget.set_savings(savings_goal)

        # Loop to add expenses
        while True:
            expense_name = input("\nEnter expense name (or type 'done' to finish): ")
            if expense_name.lower() == 'done':
                break
            
            try:
                expense_amount = float(input(f"Enter amount for '{expense_name}': $"))
                my_budget.add_expense(expense_name, expense_amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        
        my_budget.show_summary()

    except ValueError:
        print("❌ Invalid input. Please enter a number for income and amounts.")

if __name__ == "__main__":
    main()
