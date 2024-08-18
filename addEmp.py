import customtkinter
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime,timedelta
import mysql.connector

from connectionSQL import cursor, connection

customtkinter.set_appearance_mode('light')

class AddEmployee:
    def __init__(self, master,refresh_ui=None):
        self.master = master
        master.title("Add New Employee")

        # Labels and Entry fields
        self.employee_name_label = ctk.CTkLabel(master, text="Name:", width=15)
        self.employee_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.employee_name_entry = ctk.CTkEntry(master, width=150)
        self.employee_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.employee_contact_label = ctk.CTkLabel(master, text="Employee Contact:", width=15)
        self.employee_contact_label.grid(row=1, column=0, padx=5, pady=5)
        self.employee_contact_entry = ctk.CTkEntry(master, width=150)
        self.employee_contact_entry.grid(row=1, column=1, padx=5, pady=5)

        self.employee_id = ctk.CTkLabel(master, text="Employee Id:", width=15)
        self.employee_id.grid(row=2, column=0, padx=5, pady=5)
        self.employee_id_entry = ctk.CTkEntry(master, width=150)
        self.employee_id_entry.grid(row=2, column=1, padx=5, pady=5)

        self.status_label = ctk.CTkLabel(master, text="Availability:", width=15)
        self.status_label.grid(row=5, column=0, padx=5, pady=5)
        self.status_label_entry = ctk.CTkComboBox(master, values=["Available", "Not Available"])
        self.status_label_entry.set("Available")  # Set the default value
        self.status_label_entry.grid(row=5, column=1, padx=5, pady=5)

      # Add button
        self.add_button = ctk.CTkButton(master, text="Add Employee", command=lambda: self.add_employee(refresh_ui))
        self.add_button.grid(row=6, column=1, padx=5, pady=5)

    def add_employee(self,refresh_ui):
        # Get user input (code omitted for brevity)
        empName = self.employee_name_entry.get().strip()
        eHours = 0
        eContact = self.employee_contact_entry.get().strip()
        eId = self.employee_id_entry.get().strip()
        eStatus = self.status_label_entry.get()

        if not empName:
            messagebox.showerror("Error", "Please enter a vehicle name.")
            return
        if not eContact:
            messagebox.showerror("Error", "Please enter a vehicle number.")
            return

        # id = cursor.execute("Select Count(emp_id)  from EmpInfo")
        # newId = cursor.fetchone()[0]

        # Construct and execute SQL query
        query = f'INSERT INTO EmpInfo VALUES ({eId},"{empName}",{eHours},{eContact},"{eStatus}")'
        print("SQL Query:", query)  # Debugging output
        try:
            cursor.execute(query)
            connection.commit()             # Commit the transaction
            # root.destroy()
            refresh_ui()
            self.master.destroy()
            messagebox.showinfo('Note', 'Employee Added Successfully')
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'An error occurred: {err}')


if __name__ == "__main__":
    root = ctk.CTk()
    app = AddEmployee(root)
    root.geometry('800x600')
    root.mainloop()


