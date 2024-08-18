import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import CTkComboBox, CTkFrame, CTkLabel, CTkButton
import mysql.connector

from addEmp import AddEmployee
from connectionSQL import connection, cursor


class EmpInfo(tk.Tk):
    def __init__(self,dbWind = None):
        super().__init__()
        self.title("Vehicle Management System")
        self.geometry('1500x800')

        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        self.cont = ctk.CTkFrame(self)
        self.cont.pack(fill="both")

        self.cont1 = ctk.CTkFrame(self.cont)
        self.cont1.pack(side=tk.TOP, pady=3)

        self.backButton = ctk.CTkButton(self.cont1, text='Back', font=("Arial", 12), command=lambda : self.gotoDashBoard(dbWind))
        self.backButton.pack(side=tk.LEFT)


        self.myFrame = ctk.CTkScrollableFrame(self.cont, width=500, height=500)
        self.myFrame.pack(pady=0, fill="both")

        # self.status_combobox = CTkComboBox(self.cont1, values=["Status", "Model", "Distance Driven"])
        # self.status_combobox.set("Select")  # Set the default value
        # self.status_combobox.pack(side=tk.LEFT, padx=5, pady=5)

        self.AddEmployeeButton = ctk.CTkButton(self.cont1, text='Add Employee', font=("Arial", 12), command=self.gotoAddEmployee)
        self.AddEmployeeButton.pack(side=tk.LEFT, padx=(20, 0))

        self.refresh_ui()

    def gotoAddEmployee(self):
        # Create a new window for adding a vehicle
        add_vehicle_window = tk.Toplevel(self)
        add_vehicle_window.title("Add New Vehicle")

        # Instantiate the AddVehicle class in the new window
        add_vehicle_page = AddEmployee(add_vehicle_window, self.refresh_ui)

    def gotoDashBoard(self, dbWind):
        self.cont.destroy()
        self.destroy()
        dbWind()


    def gotoDashBoard(self, dbWind):
        self.cont.destroy()
        self.destroy()
        dbWind()
        # db.tkraise()

    def delete_and_refresh(self, vNum):
        try:
            query = 'DELETE FROM VehicleInfo WHERE vNumber = %s'
            cursor.execute(query, (vNum,))
            connection.commit()  # Commit the transaction
            messagebox.showinfo("Note", "Vehicle removed successfully")
            self.refresh_ui()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Could not remove Vehicle: {err}")

    def refresh_ui(self):
        # Clear existing UI components
        for widget in self.myFrame.winfo_children():
            widget.destroy()

        # Reload data from the database
        cursor.execute('SELECT * FROM EmpInfo')
        results = cursor.fetchall()

        print(results)
        # Repopulate UI with updated data
        for x in results:
            mainCont = tk.Frame(self.myFrame, borderwidth=2, relief='groove', background='#E0e0e0')
            mainCont.pack(fill='both', pady=10)

            container = ctk.CTkFrame(mainCont, border_width=0)
            container.pack(fill='both')

            vNumLab = ctk.CTkLabel(container, text="Employee Id:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side='left')

            vNum = ctk.CTkLabel(container, text=x[0], font=("Arial", 15))
            vNum.pack(pady=5, side='left')

            vNameLab = ctk.CTkLabel(container, text="Employee Name:", font=("Arial", 15, "bold"))
            vNameLab.pack(padx=(25, 0), pady=5, side='left')

            vName = ctk.CTkLabel(container, text=x[1], font=("Arial", 15))
            vName.pack(pady=5, side='left')

            vModelLab = ctk.CTkLabel(container, text="Hours Driven:", font=("Arial", 15, "bold"))
            vModelLab.pack(padx=(30, 0), pady=5, side='left')

            vModel = ctk.CTkLabel(container, text=x[2], font=("Arial", 15))
            vModel.pack(pady=5, side='left')

            vDistDriven = ctk.CTkLabel(container, text="Contact Details:", font=("Arial", 15, "bold"))
            vDistDriven.pack(padx=(20, 0), pady=5, side='left')

            status = x[3]
            vDist = tk.Label(container, text=x[3], font=("Arial", 15), foreground='green', background='#dfdfdf')
            vDist.pack(pady=5, side='left')

            vDistDriven = ctk.CTkLabel(container, text="Current Status:", font=("Arial", 15, "bold"))
            vDistDriven.pack(padx=(20, 0), pady=5, side='left')

            status = x[3]
            vDist = tk.Label(container, text=x[4], font=("Arial", 15), foreground='black', background='#dfdfdf')
            vDist.pack(pady=5, side='left')

            # Add other labels similarly

    def getFilter(self):
        filter = self.status_combobox.get().strip()
        print(filter)
        if filter == 'Status':
            data = 'vStatus'
        elif filter == 'Model':
            data = 'vModel'
        elif filter == 'Distance Driven':
            data = 'vDistDriven'
        else:
            # Handle the case where no filter is selected
            messagebox.showwarning("Warning", "Please select a valid filter.")
            return

        for widget in self.myFrame.winfo_children():
            widget.destroy()
        query = f'SELECT * FROM VehicleInfo ORDER BY {data}'
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # Render the UI with the filtered results
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Could not fetch data: {err}")

        print(results)
        for x in results:
            mainCont = ctk.CTkFrame(self.myFrame, borderwidth=2, relief='groove', background='#E0e0e0')
            mainCont.pack(fill=tk.BOTH, pady=10)

            container = ctk.CTkFrame(mainCont, border_width=0)
            container.pack(fill=tk.BOTH)

            vNumLab = ctk.CTkLabel(container, text="Vehicle Number:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side=tk.LEFT)

            vNum = ctk.CTkLabel(container, text=x[0], font=("Arial", 15))
            vNum.pack(pady=5, side=tk.LEFT)


if __name__ == "__main__":
    app = EmpInfo()
    app.mainloop()
