# **Transaction Tracker (Python Project)**

A simple and efficient Python-based **Transaction Tracking System** that helps you record, view, and analyze financial transactions.
This project demonstrates usage of **Object-Oriented Programming (OOP)**, **date filtering**, and **basic financial calculations** in Python.

---

## 🚀 Features

* **Add Transactions** with ID, amount, type, date, and description
* **Auto-date assignment** if not provided
* **View all transactions** in a clean formatted output
* **Filter transactions by date range**
* **Calculate total income or expenses**
* Uses only Python’s built-in `datetime` module

---

## 🧩 Project Structure

```
TransactionTracker Project
│
├── Transaction
│     ├── transaction_id
│     ├── amount
│     ├── transaction_type
│     ├── description
│     └── date
│
└── TransactionTracker
      ├── add_transaction()
      ├── show_all_transactions()
      ├── filter_transactions_by_date()
      └── total_amount_for_type()
```

---

## 📝 How It Works

### 1. Create Transaction objects

```python
t1 = Transaction(1, 1000, "income", "Salary payment")
t2 = Transaction(2, 200, "expense", "Grocery shopping")
t3 = Transaction(3, 500, "income", "Freelance work", date="2025-04-15 10:00:00")
t4 = Transaction(4, 50, "expense", "Coffee", date="2025-04-20 15:00:00")
```

### 2. Add them to the tracker

```python
tracker.add_transaction(t1)
tracker.add_transaction(t2)
tracker.add_transaction(t3)
tracker.add_transaction(t4)
```

### 3. Display all transactions

```python
tracker.show_all_transactions()
```

### 4. Filter by date range

```python
tracker.filter_transactions_by_date("2025-04-14", "2025-04-21")
```

### 5. Calculate totals

```python
tracker.total_amount_for_type("income")
tracker.total_amount_for_type("expense")
```

---

## ▶️ Running the Program

Make sure you have **Python 3.x** installed.

Run the script using:

```bash
python3 main.py
```

You will see output such as:

* Program start confirmation
* Transactions added
* Full transaction list
* Filtered transactions
* Totals for income and expenses

---

## 📂 File Structure (Example)

```
project/
│── main.py
│── README.md
```

---

## 📌 Dependencies

This project is fully standalone and requires **no external libraries**.
Uses only:

* `datetime` (built-in)

---

## 📷 Example Output

```
Program Started
Transaction 1 added successfully.
Transaction 2 added successfully.
Transaction 3 added successfully.
Transaction 4 added successfully.

All Transactions:
Transaction ID: 1
Amount: 1000
Type: income
Description: Salary payment
Date: 2025-04-15 12:30:00

...
```

---

## 📚 Learning Highlights

* Python OOP
* Constructors and methods
* Lists and filtering
* Datetime parsing and formatting
* Clean code practices

---

## 💡 Future Enhancements

* Export transactions to CSV or JSON
* Add a graphical UI (Tkinter or PyQt)
* Generate charts for income vs expenses
* Add a database or login system
* Build a web interface using Flask or Django

---

If you want, I can also generate:
✅ A GitHub project description
✅ A project banner/logo
✅ A more advanced version of the code

Just let me know!




