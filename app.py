import tkinter as tk

expenses = []

def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()

    if amount and category:
        entry = f"₹{amount} - {category}"
        expenses.append(entry)

        # Add to listbox
        listbox.insert(tk.END, entry)

        result_label.config(text="Expense added!")

        # Clear inputs
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        result_label.config(text="Please fill all fields")


def delete_expense():
    selected = listbox.curselection()

    if not selected:
        result_label.config(text="Select an item to delete")
        return

    index = selected[0]

    listbox.delete(index)
    expenses.pop(index)

    result_label.config(text="Expense deleted")
# Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("300x350")

# Title
tk.Label(root, text="Expense Tracker", font=("Arial", 14)).pack(pady=10)

# Inputs
tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

# Button
tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="Delete Selected Expense", command=delete_expense).pack(pady=5)

# Result
result_label = tk.Label(root, text="")
result_label.pack()

# Listbox (NEW 🔥)
tk.Label(root, text="Expenses:").pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Run
root.mainloop()