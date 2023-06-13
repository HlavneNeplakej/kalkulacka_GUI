import tkinter as tk


class KalkulackaModel:

    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except ZeroDivisionError:
            self.expression = "Error: Division by zero"
        except SyntaxError:
            self.expression = "Error: Invalid syntax"
        except Exception as e:
            self.expression = "Error:" + str(e)