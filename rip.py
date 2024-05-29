import os
import chardet
import tkinter as tk
from tkinter import filedialog

def detect_encoding(filename):
    with open(filename, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def process_attendees(filename):
    employees = []
    partners = []

    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    encoding = detect_encoding(filename)

    with open(filename, encoding=encoding) as file:
        for line in file:
            my_list = line.split('\t')
            # print(my_list)
            if 'Attendee' in my_list:
                for item in my_list:
                    if '@' in item:
                        name, domain = item.split('@')
                        if domain.strip() == 'hpe.com' and item.lower() not in employees:
                            employees.append(item.lower())
                        elif domain.strip() != 'hpe.com' and item.lower() not in partners:
                            partners.append(item.lower())

    print('-----------------------------------------------')
    print("Employees:")
    print('-----------------------------------------------')
    for i in employees:
        print(i)
    print('-----------------------------------------------')
    print("Partners:")
    print('-----------------------------------------------')
    for i in partners:
        print(i)
    print('-----------------------------------------------')
    print(f"{len(employees)} employees attended the call")
    print(f"{len(partners)} partners attended the call")
    print('-----------------------------------------------')

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    filename = filedialog.askopenfilename(
        title="Select file",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )
    if filename:
        process_attendees(filename)
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_file()
