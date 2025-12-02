import datetime

class Transaction:
    def __init__(self, transaction_id, amount, transaction_type, description, date=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        if isinstance(date, str):  # Check if date is a string
            self.date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")  # Convert string to datetime
        else:
            self.date = date if date else datetime.datetime.now()  # Use current time if no date is provided

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}\nAmount: {self.amount}\nType: {self.transaction_type}\nDescription: {self.description}\nDate: {self.date.strftime('%Y-%m-%d %H:%M:%S')}\n"

class TransactionTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print(f"Transaction {transaction.transaction_id} added successfully.")

    def show_all_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def filter_transactions_by_date(self, start_date, end_date):
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        filtered_transactions = [
            t for t in self.transactions if start_date <= t.date <= end_date
        ]
        
        for transaction in filtered_transactions:
            print(transaction)

    def total_amount_for_type(self, transaction_type):
        total = sum(
            t.amount for t in self.transactions if t.transaction_type.lower() == transaction_type.lower()
        )
        print(f"Total amount for {transaction_type}: {total}")
        return total

def main():
    print("Program Started")  # Debugging message to check if main() runs
    
    tracker = TransactionTracker()

    t1 = Transaction(transaction_id=1, amount=1000, transaction_type="income", description="Salary payment")
    t2 = Transaction(transaction_id=2, amount=200, transaction_type="expense", description="Grocery shopping")
    t3 = Transaction(transaction_id=3, amount=500, transaction_type="income", description="Freelance work", date="2025-04-15 10:00:00")
    t4 = Transaction(transaction_id=4, amount=50, transaction_type="expense", description="Coffee", date="2025-04-20 15:00:00")
    
    tracker.add_transaction(t1)
    tracker.add_transaction(t2)
    tracker.add_transaction(t3)
    tracker.add_transaction(t4)

    print("\nAll Transactions:")
    tracker.show_all_transactions()

    print("\nTransactions between 2025-04-14 and 2025-04-21:")
    tracker.filter_transactions_by_date("2025-04-14", "2025-04-21")

    tracker.total_amount_for_type("income")
    tracker.total_amount_for_type("expense")

if __name__ == "__main__":
    main()