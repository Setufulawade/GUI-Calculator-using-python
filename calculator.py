import tkinter as tk

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Calculator")
        self.geometry("400x400")

        self.result_var = tk.StringVar()
        self.last_operator = None

        self.create_widgets()

    def create_number_button(self, text, row, col):
        button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col)

    def create_widgets(self):
        # Entry widget to display the result
        entry_result = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10)
        entry_result.grid(row=0, column=0, columnspan=4)

        # Buttons for numbers, operators, and backspace
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("Backspace", 5, 0),
        ]

        for (text, row, col) in buttons:
            if text == "Backspace":
                self.create_number_button(text, row, col)
            else:
                if text == ".":
                    row += 1
                self.create_number_button(text, row, col)

    def on_button_click(self, text):
        if text == "=":
            self.on_equals_click()
        elif text == "Backspace":
            self.on_backspace_click()
        else:
            if self.last_operator is None:
                current_text = self.result_var.get()
                new_text = current_text + text
                self.result_var.set(new_text)
            else:
                current_text = self.result_var.get()
                new_text = current_text + text
                self.result_var.set(new_text)
                self.last_operator = None

    def on_backspace_click(self):
        current_text = self.result_var.get()
        new_text = current_text[:-1]
        self.result_var.set(new_text)

    def on_equals_click(self):
        current_text = self.result_var.get()
        try:
            result = eval(current_text)
            self.result_var.set(result)
        except ZeroDivisionError:
            self.result_var.set("Error: Division by zero")
        except:
            self.result_var.set("Error")

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()