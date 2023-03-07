import tkinter as tk

class FinancialApp:
    def __init__(self, master):
        self.master = master
        master.title("Financial App")
        
        # Create input fields and labels
        self.label_income = tk.Label(master, text="Income:")
        self.label_income.grid(row=0, column=0, sticky="w")
        self.entry_income = tk.Entry(master)
        self.entry_income.grid(row=0, column=1)
        
        self.label_expenses = tk.Label(master, text="Expenses:")
        self.label_expenses.grid(row=1, column=0, sticky="w")
        self.entry_expenses = tk.Entry(master)
        self.entry_expenses.grid(row=1, column=1)

        # Create a button to calculate the budget
        self.button_calculate = tk.Button(master, text="Calculate", command=self.calculate_budget)
        self.button_calculate.grid(row=2, column=1)
        
        # Create a label to display the budget result
        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=3, column=1, sticky="w")
    
    def calculate_budget(self):
        try:
            income = float(self.entry_income.get())
            expenses = float(self.entry_expenses.get())
            
            # Calculate the budget and display the result
            budget = income - expenses
            self.label_result.configure(text="Your budget is: ${:.2f}".format(budget))

        except ValueError:
            # Display an error message if the inputs are invalid
            self.label_result.configure(text="Invalid input. Please enter a number.")
            

root = tk.Tk()
app = FinancialApp(root)
root.mainloop()
