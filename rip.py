import os
import chardet
import tkinter as tk
from tkinter import filedialog, simpledialog

def detect_encoding(filename):
    with open(filename, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def process_attendees(filename, output_filename):
    employees = []
    partners = []

    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    encoding = detect_encoding(filename)

    with open(filename, encoding=encoding) as file:
        for line in file:
            my_list = line.split('\t')
            if 'Attendee' in my_list:
                for item in my_list:
                    if '@' in item:
                        name, domain = item.split('@')
                        if domain.strip() == 'hpe.com' and item.lower() not in employees:
                            employees.append(item.lower())
                        elif domain.strip() != 'hpe.com' and item.lower() not in partners:
                            partners.append(item.lower())

    output_lines = []
    output_lines.append('+++++++++++++++++++++++++++++++++++++++++++++++')
    output_lines.append(f"{len(employees)} employees attended the call")
    output_lines.append(f"{len(partners)} partners attended the call")
    output_lines.append('+++++++++++++++++++++++++++++++++++++++++++++++')
    output_lines.append("Employees:")
    output_lines.append('-----------------------------------------------')
    for i in employees:
        output_lines.append(i)
    output_lines.append('+++++++++++++++++++++++++++++++++++++++++++++++')
    output_lines.append("Partners:")
    output_lines.append('-----------------------------------------------')
    for i in partners:
        output_lines.append(i)
    output_lines.append('+++++++++++++++++++++++++++++++++++++++++++++++')
    
    # Print to terminal
    for line in output_lines:
        print(line)
    
    # Write to output file
    with open(output_filename, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')

    print(f"Output written to {output_filename}")

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    filename = filedialog.askopenfilename(
        title="Select file",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )
    if filename:
        output_filename = simpledialog.askstring("Output File", "Enter the output file name (with .txt extension):")
        if output_filename:
            if not output_filename.endswith('.txt'):
                output_filename += '.txt'
            process_attendees(filename, output_filename)
        else:
            print("No output file name provided.")
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_file()
