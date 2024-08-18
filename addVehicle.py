import customtkinter
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime,timedelta
import mysql.connector

from connectionSQL import cursor, connection

customtkinter.set_appearance_mode('light')

class AddVehicle:
    def __init__(self, master,refresh_ui=None):
        self.master = master
        master.title("Add New Vehicle")

        # Labels and Entry fields
        self.vehicle_name_label = ctk.CTkLabel(master, text="Vehicle Name:", width=15)
        self.vehicle_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.vehicle_name_entry = ctk.CTkEntry(master, width=150)
        self.vehicle_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.vehicle_number_label = ctk.CTkLabel(master, text="Vehicle Number:", width=15)
        self.vehicle_number_label.grid(row=1, column=0, padx=5, pady=5)
        self.vehicle_number_entry = ctk.CTkEntry(master, width=150)
        self.vehicle_number_entry.grid(row=1, column=1, padx=5, pady=5)

        self.model_label = ctk.CTkLabel(master, text="Model:", width=15)
        self.model_label.grid(row=2, column=0, padx=5, pady=5)
        self.model_entry = ctk.CTkEntry(master, width=150)
        self.model_entry.grid(row=2, column=1, padx=5, pady=5)

        self.status_label = ctk.CTkLabel(master, text="Leased/Owned:", width=15)
        self.status_label.grid(row=3, column=0, padx=5, pady=5)

        self.status_combobox = ctk.CTkComboBox(master, values=["Leased", "Owned"])
        self.status_combobox.set("Leased")  # Set the default value
        self.status_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.distance_label = ctk.CTkLabel(master, text="Distance Driven (km):")
        self.distance_label.grid(row=4, column=0, padx=5, pady=5)
        self.distance_entry = ctk.CTkEntry(master, width=150)  # Adjust width based on typical distance values
        self.distance_entry.grid(row=4, column=1, padx=5, pady=5)
        self.distance_entry.insert(0, "0")  # Pre-fill with 0

        self.maintenance_label = ctk.CTkLabel(master, text="Maintenance Status:", width=15)
        self.maintenance_label.grid(row=5, column=0, padx=5, pady=5)
        self.maintenance_status = ctk.CTkComboBox(master, values=["Active", "Inactive", "Maintenance"])
        self.maintenance_status.set("Active")  # Set the default value
        self.maintenance_status.grid(row=5, column=1, padx=5, pady=5)

        # Add button
        self.add_button = ctk.CTkButton(master, text="Add Vehicle", command=lambda: self.add_vehicle(refresh_ui))
        self.add_button.grid(row=6, column=1, padx=5, pady=5)

    def add_vehicle(self,refresh_ui):
        # Get user input (code omitted for brevity)
        vehicle_name = self.vehicle_name_entry.get().strip()
        vehicle_number = self.vehicle_number_entry.get().strip()
        model = self.model_entry.get().strip()
        status = self.status_combobox.get()
        distance_driven = self.distance_entry.get().strip()
        maintenance_status = self.maintenance_status.get().strip()

        if not vehicle_name:
            messagebox.showerror("Error", "Please enter a vehicle name.")
            return
        if not vehicle_number:
            messagebox.showerror("Error", "Please enter a vehicle number.")
            return

        print("Vehicle Name:", vehicle_name)
        print("Vehicle Number:", vehicle_number.upper())
        print("Model:", model)
        print("Status:", status)
        print("Distance Driven:", distance_driven)
        print("Maintenance Status:", maintenance_status)

        print(datetime.now().date())
        current_date = datetime.now().date()

        # Add 2 months to the current date
        two_months_later = (current_date)
                            # + timedelta(days=2 * 30))
        print(two_months_later)

        # Construct and execute SQL query
        query = f'INSERT INTO VehicleInfo VALUES ("{vehicle_number.upper()}","{vehicle_name}","{maintenance_status}","{model}","{distance_driven}","{two_months_later}", "Available")'
        print("SQL Query:", query)  # Debugging output
        try:
            cursor.execute(query)
            connection.commit()             # Commit the transaction
            # root.destroy()
            refresh_ui()
            self.master.destroy()
            messagebox.showinfo('Note', 'Vehicle Added Successfully')
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'An error occurred: {err}')


if __name__ == "__main__":
    root = ctk.CTk()
    app = AddVehicle(root)
    root.geometry('800x600')
    root.mainloop()


