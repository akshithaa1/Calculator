import tkinter as tk

# Function to update the result label
def update_display(value):
    current = entry_display.get()
    if current == '0':
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, value)
    else:
        entry_display.insert(tk.END, value)

# Function to handle the clear button
def clear():
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, '0')

# Function to evaluate the expression
def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, 'Error')

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for display
entry_display = tk.Entry(root, width=30, justify='right', font=('Arial', 16))
entry_display.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operations in the correct order
button_values = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for value in button_values:
    if value == '=':
        tk.Button(root, text=value, padx=20, pady=20, command=calculate, font=('Arial', 16)).grid(row=row_val, column=col_val)
    elif value == '0':
        tk.Button(root, text=value, padx=20, pady=20, command=lambda v=value: update_display(v), font=('Arial', 16)).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 1
    else:
        tk.Button(root, text=value, padx=20, pady=20, command=lambda v=value: update_display(v), font=('Arial', 16)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, command=clear, font=('Arial', 16)).grid(row=row_val, column=col_val)

# Start the GUI main loop
root.mainloop()
