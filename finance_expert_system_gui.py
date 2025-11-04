import tkinter as tk
from tkinter import messagebox


def get_finance_advice():
    try:
        income = float(income_entry.get())
        expenses = float(expense_entry.get())
        goal = goal_var.get()

        if income <= 0 or expenses < 0:
            messagebox.showerror("Input Error", "Please enter positive income and expense values.")
            return

        savings = income - expenses
        advice = ""

    
        if goal == "Savings":
            if savings > 20000:
                advice = "Excellent! You can start investing in fixed deposits or mutual funds."
            elif savings > 5000:
                advice = "Good! Keep saving regularly and track your budget monthly."
            else:
                advice = "Your expenses are too high! Try cutting down unnecessary spending."
        
        elif goal == "Investment":
            if savings > 25000:
                advice = "Perfect! You can invest in SIPs, stocks, or mutual funds."
            elif savings > 10000:
                advice = "Consider small investments like recurring deposits or ELSS schemes."
            else:
                advice = "Increase savings before entering high-risk investments."
        
        elif goal == "Debt Management":
            if expenses > income:
                advice = "You're overspending! Reduce expenses and avoid new debts."
            else:
                advice = "Focus on clearing high-interest loans first and plan an emergency fund."
        
        else:
            advice = "Please select a valid financial goal."

        messagebox.showinfo("Financial Advice", advice)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter numeric values for income and expenses.")




window = tk.Tk()
window.title("Finance Expert System 💰")
window.geometry("450x450")
window.config(bg="#E3F2FD")


tk.Label(window, text="Finance Expert System", font=("Arial", 18, "bold"), bg="#1565C0", fg="white", pady=10).pack(fill="x")


tk.Label(window, text="Enter Monthly Income (₹):", font=("Arial", 12), bg="#E3F2FD").pack(pady=10)
income_entry = tk.Entry(window, width=25, font=("Arial", 11))
income_entry.pack(pady=5)


tk.Label(window, text="Enter Monthly Expenses (₹):", font=("Arial", 12), bg="#E3F2FD").pack(pady=10)
expense_entry = tk.Entry(window, width=25, font=("Arial", 11))
expense_entry.pack(pady=5)


tk.Label(window, text="Select Your Financial Goal:", font=("Arial", 12), bg="#E3F2FD").pack(pady=10)

goal_var = tk.StringVar(value="Savings")
goals = ["Savings", "Investment", "Debt Management"]

for goal in goals:
    tk.Radiobutton(window, text=goal, variable=goal_var, value=goal, bg="#E3F2FD", font=("Arial", 11)).pack()


tk.Button(window, text="Get Financial Advice", command=get_finance_advice,
          bg="#1565C0", fg="white", font=("Arial", 12, "bold"), width=20).pack(pady=20)


tk.Label(window, text="Created by Tejal Powar 🌸", font=("Arial", 9, "italic"), bg="#E3F2FD", fg="#424242").pack(side="bottom", pady=10)

window.mainloop()
