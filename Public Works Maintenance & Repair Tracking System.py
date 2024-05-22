import tkinter as tk
from tkinter import ttk, messagebox

public_works = ["Road Maintenance", "Drainage Work", "Building Construction", "Garden Maintenance"]
status_options = ["Pending", "In Progress", "Completed"]

records = []

def add_record():
    work = work_combo.get()
    description = description_entry.get()
    date = date_entry.get()
    status = status_combo.get()
    cost = cost_entry.get()

    if not (work and description and date and status and cost):
        messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
        return

    new_record = {"work": work, "description": description, "date": date, "status": status, "cost": cost}
    records.append(new_record)
    update_record_list()
    clear_entries()

def edit_record():
    selected_items = record_table.selection()
    if selected_items:
        selected_item = selected_items[0]
        record = records[record_table.index(selected_item)]
        work_combo.set(record["work"])
        description_entry.delete(0, tk.END)
        description_entry.insert(0, record["description"])
        date_entry.delete(0, tk.END)
        date_entry.insert(0, record["date"])
        status_combo.set(record["status"])
        cost_entry.delete(0, tk.END)
        cost_entry.insert(0, record["cost"])

def save_record():
    selected_items = record_table.selection()
    if selected_items:
        selected_item = selected_items[0]
        record_index = record_table.index(selected_item)
        records[record_index] = {
            "work": work_combo.get(),
            "description": description_entry.get(),
            "date": date_entry.get(),
            "status": status_combo.get(),
            "cost": cost_entry.get()
        }
        update_record_list()
        clear_entries()

def delete_record():
    selected_items = record_table.selection()
    if selected_items:
        selected_item = selected_items[0]
        record_index = record_table.index(selected_item)
        records.pop(record_index)
        update_record_list()

def clear_entries():
    work_combo.set("")
    description_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    status_combo.set("")
    cost_entry.delete(0, tk.END)


def update_record_list():
    record_table.delete(*record_table.get_children())
    for record in records:
        record_table.insert("", tk.END, values=(record['work'], record['description'], record['date'], record['status'], record['cost']))


root = tk.Tk()
root.title("Public Works Maintenance and Repair Tracking System")
root.geometry("1280x720")  

bg_color = "#3d3d3d"
fg_color = "white"

root.configure(bg=bg_color)

button_frame = tk.Frame(root, bg=bg_color)

add_button = tk.Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=0, padx=10, pady=5)

edit_button = tk.Button(button_frame, text="Edit Record", command=edit_record)
edit_button.grid(row=0, column=1, padx=10, pady=5)

save_button = tk.Button(button_frame, text="Save Record", command=save_record)
save_button.grid(row=0, column=2, padx=10, pady=5)

delete_button = tk.Button(button_frame, text="Delete Record", command=delete_record)
delete_button.grid(row=0, column=3, padx=10, pady=5)

header_frame = tk.Frame(root, bg=bg_color)
input_frame = tk.Frame(root, bg=bg_color)
list_frame = tk.Frame(root, bg=bg_color)

header_label = tk.Label(header_frame, text="Public Works Maintenance and Repair Tracking System", font=("Arial", 18, "bold"), bg=bg_color, fg=fg_color)
header_label.pack(pady=10)

input_table = tk.Frame(input_frame, bg=bg_color)
input_table.pack(pady=20)

work_label = tk.Label(input_table, text="Work:", font=("Arial", 12), bg=bg_color, fg=fg_color)
work_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

work_combo = ttk.Combobox(input_table, values=public_works)
work_combo.grid(row=0, column=1, padx=10, pady=5)

description_label = tk.Label(input_table, text="Description:", font=("Arial", 12), bg=bg_color, fg=fg_color)
description_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

description_entry = tk.Entry(input_table)
description_entry.grid(row=1, column=1, padx=10, pady=5)

date_label = tk.Label(input_table, text="Date:", font=("Arial", 12), bg=bg_color, fg=fg_color)
date_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

date_entry = tk.Entry(input_table)
date_entry.grid(row=2, column=1, padx=10, pady=5)

status_label = tk.Label(input_table, text="Status:", font=("Arial", 12), bg=bg_color, fg=fg_color)
status_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

status_combo = ttk.Combobox(input_table, values=status_options)
status_combo.grid(row=3, column=1, padx=10, pady=5)

cost_label = tk.Label(input_table, text="Cost:", font=("Arial", 12), bg=bg_color, fg=fg_color)
cost_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

cost_entry = tk.Entry(input_table)
cost_entry.grid(row=4, column=1, padx=10, pady=5)

columns = ("work", "description", "date", "status", "cost")
record_table = ttk.Treeview(list_frame, columns=columns, show="headings")
record_table.heading("work", text="Work")
record_table.heading("description", text="Description")
record_table.heading("date", text="Date")
record_table.heading("status", text="Status")
record_table.heading("cost", text="Cost")
record_table.pack(pady=10, fill=tk.BOTH, expand=True)

button_frame.pack(side=tk.TOP, fill=tk.X)
header_frame.pack(fill=tk.X)
input_frame.pack(pady=20)
list_frame.pack(pady=20, fill=tk.BOTH, expand=True)

root.mainloop()
