import tkinter as tk
from tkinter import messagebox
import time
import threading

# Initialize the main app
app = tk.Tk()
app.title("TO-DO-LIST")
app.geometry("500x600")

# Task list to store tasks
tasks = []

# --- Task Functions ---
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_box.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        index = task_box.curselection()[0]
        tasks.pop(index)
        task_box.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected to delete!")

def complete_task():
    try:
        index = task_box.curselection()[0]
        task = tasks[index]
        tasks[index] = f"{task} (Completed)"
        task_box.delete(index)
        task_box.insert(index, tasks[index])
    except IndexError:
        messagebox.showwarning("Warning", "No task selected to complete!")

# --- Timer Functions ---
timer_running = False
time_elapsed = 0

def update_timer():
    global time_elapsed
    while timer_running:
        time.sleep(1)
        time_elapsed += 1
        minutes, seconds = divmod(time_elapsed, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        threading.Thread(target=update_timer, daemon=True).start()

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global time_elapsed, timer_running
    timer_running = False
    time_elapsed = 0
    timer_label.config(text="00:00")

# --- Task Manager GUI ---
task_frame = tk.Frame(app)
task_frame.pack(pady=10)

task_entry = tk.Entry(task_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)

add_btn = tk.Button(task_frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

task_box = tk.Listbox(app, width=50, height=10)
task_box.pack(pady=20)

delete_btn = tk.Button(app, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

complete_btn = tk.Button(app, text="Complete Task", command=complete_task)
complete_btn.pack(pady=5)

# --- Timer GUI ---
timer_frame = tk.LabelFrame(app, text="Timer", padx=10, pady=10)
timer_frame.pack(pady=20, fill="x")

timer_label = tk.Label(timer_frame, text="00:00", font=("Helvetica", 24))
timer_label.pack()

btn_frame = tk.Frame(timer_frame)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start", command=start_timer, width=10)
start_btn.pack(side=tk.LEFT, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop", command=stop_timer, width=10)
stop_btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", command=reset_timer, width=10)
reset_btn.pack(side=tk.LEFT, padx=5)

# Styling the GUI
app.configure(bg='#D1C4E9')  # Light Purple color
task_frame.configure(bg='#D1C4E9')
timer_frame.configure(bg='#D1C4E9')

task_box.configure(bg='#EDE7F6', fg='black', selectbackground='black', selectforeground='white')
timer_label.configure(bg='#D1C4E9', fg='black')
start_btn.configure(bg='#D1C4E9', fg='black')
stop_btn.configure(bg='#D1C4E9', fg='black')
reset_btn.configure(bg='#D1C4E9', fg='black')

# Run the app
app.mainloop()
 
