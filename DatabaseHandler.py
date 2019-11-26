from FileManager.FileManager import *
import sqlite3 as sql
from datetime import datetime


class Database:
    def __init__(self, name):
        # setup cursor
        db = sql.connect(name)
        cursor = db.cursor()

        #Deal with creating new table
        cursor.execute(""" CREATE TABLE IF NOT EXISTS expenses(
        id INT NOT NULL PRIMARY KEY, AUTO_INCREMENT,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount FLOAT NOT NULL,
        date DATETIME NOT NULL);""")

        self.cursor = cursor

    def add_expense(self, description: str, category: str, amount: float):
        """
        :param description:
        :param category:
        :param amount:
        :return: None
        """
        self.cursor.execute("""INSERT INTO expenses (description, category, amount, date)
        VALUES ({}, {}, {}, {});""". format(description, category, amount, datetime.now()))

    def get_by_category(self, category: str):
        """
        :param category:
        :return:
        """
        return self.cursor.execute("""SELECT description, amount FROM expenses 
        WHERE category = {} SORT BY date;""".format(category))

    def get_all(self):
        """
        Doesn't give them the expense ID
        sort by date
        :return:
        """

        return self.cursor.execute("""SELECT description, category, amount FROM expenses 
        SORT BY date;""")


class Analysis:

    def get_total_value(self, expenses: list):
        """

        :param expenses: The expenses you want to get the total value of
            - formatted desc, category, amount
        :return:
        """

    def get_num_expenses(self, expenses: list):
        """
        :param expenses: The expenses you want to get the total value of
            - formatted desc, category, amount
        :return:
        """

    def get_average_expense(self, expenses: list):
        """
        :param expenses: The expenses you want to get the total value of
            - formatted desc, category, amount
        :return:
        """

        if __name__ == '__main__':
            return self.get_total_value(expenses)/self.get_num_expenses(expenses)


def test():
    db = Database("test")
    db.add_expense("Chocolate bar", "Vitals", 10.0)
    print(db.get_all())


if __name__ == "__main__":
    test()