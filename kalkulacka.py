import tkinter as tk


class KalkulackaModel:

    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def evaluate_expression(self):
        try:
            if "×" in self.expression:
                self.expression = self.expression.replace("×", "*")
                self.result = eval(self.expression)
            elif "÷" in self.expression:
                self.expression = self.expression.replace("÷", "/")
                self.result = eval(self.expression)
            else:
                self.result = eval(self.expression)

            if self.result % 1 == 0:
                self.expression = str(int(self.result))
            else:
                self.expression = str(self.result)

        except ZeroDivisionError:
            self.expression = "Error: Division by zero"
        except SyntaxError:
            self.expression = "Error: Invalid syntax"
        except Exception as e:
            self.expression = "Error:" + str(e)