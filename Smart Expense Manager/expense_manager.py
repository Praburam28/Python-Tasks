import mysql.connector
from abc import ABC, abstractmethod
from functools import reduce

# ----------------------------
# DATABASE CONNECTION
# ----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="expense_db"
)

cursor = conn.cursor()


# ----------------------------
# ABSTRACT CLASS
# ----------------------------
class BaseReport(ABC):

    @abstractmethod
    def monthly_report(self):
        pass

    @abstractmethod
    def highest_expense(self):
        pass


# ----------------------------
# USER CLASS
# ----------------------------
class User:

    def __init__(self, name):
        self.__name = name     # encapsulation

    def create_user(self):
        sql = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(sql, (self.__name,))
        conn.commit()

        user_id = cursor.lastrowid
        print(f"\nUser created successfully. Your User ID is: {user_id}")

    # View all users
    @staticmethod
    def view_users():
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        print("\nUsers List")
        for row in data:
            print(row)


# ----------------------------
# EXPENSE CLASS
# ----------------------------
class Expense(User, BaseReport):

    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id

    # ----------------------------
    # ADD EXPENSE
    # ----------------------------
    def add_expense(self, amount, category, description, date):

        sql = """INSERT INTO expenses
        (user_id, amount, category, description, date)
        VALUES (%s,%s,%s,%s,%s)"""

        cursor.execute(sql, (self.user_id, amount, category, description, date))
        conn.commit()

        print("Expense Added")

    # ----------------------------
    # VIEW EXPENSES
    # ----------------------------
    def view_expenses(self):

        sql = """
        SELECT u.name, e.exp_id, e.amount, e.category, e.description, e.date
        FROM expenses e
        JOIN users u
        ON u.user_id = e.user_id
        WHERE e.user_id = %s
        """

        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        print("\nExpenses")
        for row in data:
            print(row)

        return data

    # ----------------------------
    # FILTER BY CATEGORY
    # ----------------------------
    def filter_by_category(self, category):

        data = self.view_expenses()

        filtered = list(filter(lambda x: x[3] == category, data))

        print("\nFiltered Expenses:")
        for i in filtered:
            print(i)

        return filtered

    # ----------------------------
    # FILTER BY DATE
    # ----------------------------
    def filter_by_date(self, date):

        data = self.view_expenses()

        filtered = [x for x in data if str(x[5]) == date]

        print("\nFiltered by Date:")
        for i in filtered:
            print(i)

        return filtered

    # ----------------------------
    # TOTAL EXPENSE
    # ----------------------------
    def total_expense(self):

        data = self.view_expenses()

        amounts = list(map(lambda x: x[2], data))

        total = reduce(lambda a, b: a + b, amounts, 0)

        print("\nTotal Expense:", total)

        return total

    # ----------------------------
    # CATEGORY WISE SPENDING
    # ----------------------------
    def category_wise(self):

        data = self.view_expenses()

        categories = set(map(lambda x: x[3], data))

        result = {
            cat: sum([x[2] for x in data if x[3] == cat])
            for cat in categories
        }

        print("\nCategory Wise Spending")
        for k, v in result.items():
            print(k, ":", v)

        return result

    # ----------------------------
    # DELETE EXPENSE
    # ----------------------------
    def delete_expense(self, exp_id):

        sql = "DELETE FROM expenses WHERE exp_id=%s"
        cursor.execute(sql, (exp_id,))
        conn.commit()

        print("Expense Deleted")

    # ----------------------------
    # UPDATE EXPENSE
    # ----------------------------
    def update_expense(self, exp_id, amount):

        sql = "UPDATE expenses SET amount=%s WHERE exp_id=%s"
        cursor.execute(sql, (amount, exp_id))
        conn.commit()

        print("Expense Updated")

    # ----------------------------
    # MONTHLY REPORT
    # ----------------------------
    def monthly_report(self):

        sql = """
        SELECT MONTH(date), SUM(amount)
        FROM expenses
        WHERE user_id=%s
        GROUP BY MONTH(date)
        """

        cursor.execute(sql, (self.user_id,))
        data = cursor.fetchall()

        print("\nMonthly Report")
        for i in data:
            print("Month:", i[0], "Total:", i[1])

    # ----------------------------
    # HIGHEST EXPENSE
    # ----------------------------
    def highest_expense(self):

        data = self.view_expenses()

        highest = reduce(lambda a, b: a if a[2] > b[2] else b, data)

        print("\nHighest Expense:", highest)

        return highest

    # ----------------------------
    # SMART INSIGHT
    # ----------------------------
    def smart_insight(self):

        result = self.category_wise()

        highest = max(result, key=result.get)

        print("\nSmart Insight:")
        print(f"You are spending too much on {highest}")


# ----------------------------
# MENU SYSTEM
# ----------------------------

def main():

    while True:

        print("\n===== Smart Expense Manager =====")
        print("1 Add User")
        print("2 View Users")
        print("3 Add Expense")
        print("4 View Expenses")
        print("5 Category Filter")
        print("6 Date Filter")
        print("7 Total Expense")
        print("8 Category Report")
        print("9 Monthly Report")
        print("10 Highest Expense")
        print("11 Smart Insight")
        print("12 Delete Expense")
        print("13 Update Expense")
        print("0 Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            user = User(name)
            user.create_user()

        elif choice == 2:
            User.view_users()

        elif choice == 3:
            uid = int(input("User ID: "))
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")

            exp = Expense("", uid)
            exp.add_expense(amount, category, desc, date)

        elif choice == 4:
            uid = int(input("User ID: "))
            exp = Expense("", uid)
            exp.view_expenses()

        elif choice == 5:
            uid = int(input("User ID: "))
            cat = input("Category: ")
            exp = Expense("", uid)
            exp.filter_by_category(cat)

        elif choice == 6:
            uid = int(input("User ID: "))
            date = input("Date: ")
            exp = Expense("", uid)
            exp.filter_by_date(date)

        elif choice == 7:
            uid = int(input("User ID: "))
            exp = Expense("", uid)
            exp.total_expense()

        elif choice == 8:
            uid = int(input("User ID: "))
            exp = Expense("", uid)
            exp.category_wise()

        elif choice == 9:
            uid = int(input("User ID: "))
            exp = Expense("", uid)
            exp.monthly_report()

        elif choice == 10:
            uid = int(input("User ID: "))
            exp = Expense("", uid)
            exp.highest_expense()

        elif choice == 11:
            uid = int(input("User ID: "))
            exp = Expense("", uid)
            exp.smart_insight()

        elif choice == 12:
            exp_id = int(input("Expense ID to delete: "))
            exp = Expense("", 0)
            exp.delete_expense(exp_id)

        elif choice == 13:
            exp_id = int(input("Expense ID to update: "))
            amount = float(input("New Amount: "))
            exp = Expense("", 0)
            exp.update_expense(exp_id, amount)

        elif choice == 0:
            print("Exiting program...")
            break


main()