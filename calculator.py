import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x500")
        self.root.resizable(False, False)

        # Variable to store the current expression
        self.expression = ""
        self.input_text = tk.StringVar()

        # Create the UI
        self.create_widgets()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, width=300, height=100, bg="grey")
        display_frame.pack(expand=True, fill="both")

        # Display label
        display_label = tk.Label(
            display_frame,
            textvariable=self.input_text,
            anchor="e",
            bg="grey",
            fg="white",
            font=("Arial", 24),
        )
        display_label.pack(expand=True, fill="both", padx=10, pady=10)

        # History label (to show the expression like "5000+300+468")
        self.history_text = tk.StringVar()
        history_label = tk.Label(
            display_frame,
            textvariable=self.history_text,
            anchor="e",
            bg="grey",
            fg="white",
            font=("Arial", 12),
        )
        history_label.pack(expand=True, fill="both", padx=10)

        # Buttons frame
        buttons_frame = tk.Frame(self.root, width=300, height=400, bg="black")
        buttons_frame.pack(expand=True, fill="both")

        # Button layout
        buttons = [
            ("AC", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("÷", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
        ]

        # Create and place buttons
        for (text, row, col) in buttons:
            if text == "=":
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    bg="orange",
                    fg="white",
                    bd=0,
                    command=lambda x=text: self.on_button_click(x)
                )
            else:
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18),
                    bg="white" if text.isdigit() or text == "." else "lightgrey",
                    fg="black",
                    bd=0,
                    command=lambda x=text: self.on_button_click(x)
                )
            if text == "0":
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
            elif text == "=":
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
            else:
                button.grid(row=row, column=col, sticky="nsew")

        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i + 1, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text == "AC":
            self.expression = ""
            self.input_text.set("")
            self.history_text.set("")
        elif button_text == "⌫":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif button_text == "=":
            try:
                # Replace symbols for evaluation
                expression_to_eval = self.expression.replace("×", "*").replace("÷", "/")
                result = eval(expression_to_eval)
                self.input_text.set(result)
                self.history_text.set(self.expression)
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.input_text.set("")
                self.history_text.set("")
        elif button_text == "%":
            try:
                result = eval(self.expression) / 100
                self.input_text.set(result)
                self.history_text.set(self.expression + "%")
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            self.expression += button_text
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()