import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class NumberConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Converter")
        self.root.geometry("400x300")

        self.tabControl = ttk.Notebook(root)
        self.tabControl.pack(expand=True, fill="both")

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Binary to All")
        self.tabControl.add(self.tab2, text="Decimal to All")
        self.tabControl.add(self.tab3, text="Hexadecimal to All")
        self.tabControl.add(self.tab4, text="Octal to All")

        self.create_binary_tab()
        self.create_decimal_tab()
        self.create_hexadecimal_tab()
        self.create_octal_tab()

    def create_binary_tab(self):
        label = tk.Label(self.tab1, text="Enter Binary Number:", font=("Arial", 12))
        label.pack(pady=10)

        self.binary_entry = tk.Entry(self.tab1, font=("Arial", 12))
        self.binary_entry.pack(pady=5)

        convert_button = tk.Button(self.tab1, text="Convert", command=self.convert_binary, bg="#4CAF50", fg="white", relief="flat")
        convert_button.pack(pady=5)

        self.binary_output_label = tk.Label(self.tab1, text="", wraplength=300, font=("Arial", 12))
        self.binary_output_label.pack(pady=10)

        clear_button = tk.Button(self.tab1, text="Clear", command=self.clear_binary, bg="#F44336", fg="white", relief="flat")
        clear_button.pack(pady=5)

    def create_decimal_tab(self):
        label = tk.Label(self.tab2, text="Enter Decimal Number:", font=("Arial", 12))
        label.pack(pady=10)

        self.decimal_entry = tk.Entry(self.tab2, font=("Arial", 12))
        self.decimal_entry.pack(pady=5)

        convert_button = tk.Button(self.tab2, text="Convert", command=self.convert_decimal, bg="#4CAF50", fg="white", relief="flat")
        convert_button.pack(pady=5)

        self.decimal_output_label = tk.Label(self.tab2, text="", wraplength=300, font=("Arial", 12))
        self.decimal_output_label.pack(pady=10)

        clear_button = tk.Button(self.tab2, text="Clear", command=self.clear_decimal, bg="#F44336", fg="white", relief="flat")
        clear_button.pack(pady=5)

    def create_hexadecimal_tab(self):
        label = tk.Label(self.tab3, text="Enter Hexadecimal Number:", font=("Arial", 12))
        label.pack(pady=10)

        self.hexadecimal_entry = tk.Entry(self.tab3, font=("Arial", 12))
        self.hexadecimal_entry.pack(pady=5)

        convert_button = tk.Button(self.tab3, text="Convert", command=self.convert_hexadecimal, bg="#4CAF50", fg="white", relief="flat")
        convert_button.pack(pady=5)

        self.hexadecimal_output_label = tk.Label(self.tab3, text="", wraplength=300, font=("Arial", 12))
        self.hexadecimal_output_label.pack(pady=10)

        clear_button = tk.Button(self.tab3, text="Clear", command=self.clear_hexadecimal, bg="#F44336", fg="white", relief="flat")
        clear_button.pack(pady=5)

    def create_octal_tab(self):
        label = tk.Label(self.tab4, text="Enter Octal Number:", font=("Arial", 12))
        label.pack(pady=10)

        self.octal_entry = tk.Entry(self.tab4, font=("Arial", 12))
        self.octal_entry.pack(pady=5)

        convert_button = tk.Button(self.tab4, text="Convert", command=self.convert_octal, bg="#4CAF50", fg="white", relief="flat")
        convert_button.pack(pady=5)

        self.octal_output_label = tk.Label(self.tab4, text="", wraplength=300, font=("Arial", 12))
        self.octal_output_label.pack(pady=10)

        clear_button = tk.Button(self.tab4, text="Clear", command=self.clear_octal, bg="#F44336", fg="white", relief="flat")
        clear_button.pack(pady=5)

    def clear_binary(self):
        self.binary_entry.delete(0, tk.END)
        self.binary_output_label.config(text="")

    def clear_decimal(self):
        self.decimal_entry.delete(0, tk.END)
        self.decimal_output_label.config(text="")

    def clear_hexadecimal(self):
        self.hexadecimal_entry.delete(0, tk.END)
        self.hexadecimal_output_label.config(text="")

    def clear_octal(self):
        self.octal_entry.delete(0, tk.END)
        self.octal_output_label.config(text="")

    def convert_binary(self):
        number = self.binary_entry.get()
        if number:
            try:
                decimal = int(number, 2)
                hexadecimal = hex(decimal)
                octal = oct(decimal)
                self.binary_output_label.config(text=f"Decimal: {decimal}\n"
                                                      f"Hexadecimal: {hexadecimal[2:]}\n"
                                                      f"Octal: {octal[2:]}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid binary number.")
        else:
            messagebox.showerror("Error", "Please enter a binary number.")

    def convert_decimal(self):
        number = self.decimal_entry.get()
        if number:
            try:
                decimal = int(number)
                binary = bin(decimal)
                hexadecimal = hex(decimal)
                octal = oct(decimal)
                self.decimal_output_label.config(text=f"Binary: {binary[2:]}\n"
                                                       f"Hexadecimal: {hexadecimal[2:]}\n"
                                                       f"Octal: {octal[2:]}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid decimal number.")
        else:
            messagebox.showerror("Error", "Please enter a decimal number.")

    def convert_hexadecimal(self):
        number = self.hexadecimal_entry.get()
        if number:
            try:
                decimal = int(number, 16)
                binary = bin(decimal)
                octal = oct(decimal)
                self.hexadecimal_output_label.config(text=f"Decimal: {decimal}\n"
                                                            f"Binary: {binary[2:]}\n"
                                                            f"Octal: {octal[2:]}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid hexadecimal number.")
        else:
            messagebox.showerror("Error", "Please enter a hexadecimal number.")

    def convert_octal(self):
        number = self.octal_entry.get()
        if number:
            try:
                decimal = int(number, 8)
                binary = bin(decimal)
                hexadecimal = hex(decimal)
                self.octal_output_label.config(text=f"Decimal: {decimal}\n"
                                                       f"Binary: {binary[2:]}\n"
                                                       f"Hexadecimal: {hexadecimal[2:]}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid octal number.")
        else:
            messagebox.showerror("Error", "Please enter an octal number.")

root = tk.Tk()
app = NumberConverterApp(root)
root.mainloop()
