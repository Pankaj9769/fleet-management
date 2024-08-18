import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import CTkComboBox, CTkFrame, CTkLabel, CTkButton
import mysql.connector
from addVehicle import AddVehicle
from connectionSQL import connection, cursor

class VehicleInfo(tk.Tk):
    def __init__(self, dbWind = None):
        super().__init__()
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        self.geometry('1500x700')

        self.cont1 = ctk.CTkFrame(self)
        self.cont1.pack(side=TOP, pady=3)


        self.backButton = ctk.CTkButton(self.cont1, text='Back', font=("Arial", 12),command=lambda : self.gotoDashBoard(dbWind))
        self.backButton.pack(side=LEFT)

        self.myFrame = ctk.CTkScrollableFrame(self, width=500, height=500)
        self.myFrame.pack(pady=0, fill="both")

        # Initial rendering of UI
        self.refresh_ui()

        self.status_combobox = CTkComboBox(self.cont1, values=["Status", "Model", "Distance Driven"])
        self.status_combobox.set("Select")  # Set the default value
        self.status_combobox.pack(side=LEFT, padx=5, pady=5)

        self.filterButton = ctk.CTkButton(self.cont1, text='Filter', font=("Arial", 12), command=self.getFilter)
        self.filterButton.pack(side=LEFT, padx=(20, 0))

        # Button to open the Add Vehicle window
        self.add_vehicle_button = CTkButton(self.cont1, text="Add Vehicle", command=self.open_add_vehicle_window)
        self.add_vehicle_button.pack(side=LEFT, padx=(20, 0))

    def gotoDashBoard(self, dbWind):
        self.cont1.destroy()
        self.destroy()
        dbWind()

    def delete_and_refresh(self, vNum):
        try:
            query1 = 'DELETE FROM MaintenanceRecord WHERE vNumber = %s'
            print(query1)
            cursor.execute(query1, (vNum,))

            query = 'DELETE FROM VehicleInfo WHERE vNumber = %s'
            print(query)
            cursor.execute(query, (vNum,))
            connection.commit()  # Commit the transaction
            messagebox.showinfo("Note", "Vehicle removed successfully")
            self.refresh_ui()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Could not remove Vehicle: {err}")
            print(err)

    def refresh_ui(self):
        # Clear existing UI components
        for widget in self.myFrame.winfo_children():
            widget.destroy()

        # Reload data from the database
        cursor.execute('SELECT * FROM VehicleInfo')
        results = cursor.fetchall()

        # Repopulate UI with updated data
        for x in results:
            mainCont = Frame(self.myFrame, borderwidth=2, relief='groove', background='#E0e0e0')
            mainCont.pack(fill=BOTH, pady=10)

            container = ctk.CTkFrame(mainCont, border_width=0)
            container.pack(fill=BOTH)

            vNumLab = ctk.CTkLabel(container, text="Vehicle Number:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

            vNum = ctk.CTkLabel(container, text=x[0], font=("Arial", 15))
            vNum.pack(pady=5, side=LEFT)

            vNameLab = ctk.CTkLabel(container, text="Vehicle Name:", font=("Arial", 15, "bold"))
            vNameLab.pack(padx=(25, 0), pady=5, side=LEFT)

            vName = ctk.CTkLabel(container, text=x[1], font=("Arial", 15))
            vName.pack(pady=5, side=LEFT)

            vModelLab = ctk.CTkLabel(container, text="Model:", font=("Arial", 15, "bold"))
            vModelLab.pack(padx=(30, 0), pady=5, side=LEFT)

            vModel = ctk.CTkLabel(container, text=x[3], font=("Arial", 15))
            vModel.pack(pady=5, side=LEFT)

            vDistDriven = ctk.CTkLabel(container, text="Distance Driven:", font=("Arial", 15, "bold"))
            vDistDriven.pack(padx=(20, 0), pady=5, side=LEFT)

            vDist = ctk.CTkLabel(container, text=x[4], font=("Arial", 15))
            vDist.pack(pady=5, side=LEFT)

            vStatusLab = ctk.CTkLabel(container, text="Status:", font=("Arial", 15, "bold"))
            vStatusLab.pack(padx=(20, 0), pady=5, side=LEFT)

            status = x[2]
            # Vehicle Status Label
            if status == "Inactive":
                vStatus = Label(container, text=status, font=("Arial", 15), foreground='red',background='#dfdfdf')
            elif status == "Active":
                vStatus = Label(container, text=status, font=("Arial", 15), foreground='green', background='#dfdfdf')
            elif status == "Maintenance":
                vStatus = Label(container, text=status, font=("Arial", 15), foreground='blue', background='#dfdfdf')

            # Vehicle Status Label

            vStatus.pack(pady=5, side=LEFT)



            updateDetailButton = ctk.CTkButton(container, text='Update')
            updateDetailButton.pack(side=RIGHT)

            container2 = ctk.CTkFrame(mainCont, border_width=0)
            container2.pack(fill=BOTH)

            vNumLab = ctk.CTkLabel(container2, text="Maintenance Due:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

            vNum = ctk.CTkLabel(container2, text=x[5], font=("Arial", 15))
            vNum.pack(pady=5, side=LEFT)

            removeVehicleButton = ctk.CTkButton(container2, text='Remove',
                                                command=lambda vNum=x[0]: self.delete_and_refresh(vNum))
            removeVehicleButton.pack(side=RIGHT)

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
            mainCont = Frame(self.myFrame, borderwidth=2, relief='groove', background='#E0e0e0')
            mainCont.pack(fill=BOTH, pady=10)

            container = ctk.CTkFrame(mainCont, border_width=0)
            container.pack(fill=BOTH)

            vNumLab = ctk.CTkLabel(container, text="Vehicle Number:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

            vNum = ctk.CTkLabel(container, text=x[0], font=("Arial", 15))
            vNum.pack(pady=5, side=LEFT)

            vNameLab = ctk.CTkLabel(container, text="Vehicle Name:", font=("Arial", 15, "bold"))
            vNameLab.pack(padx=(25, 0), pady=5, side=LEFT)

            vName = ctk.CTkLabel(container, text=x[1], font=("Arial", 15))
            vName.pack(pady=5, side=LEFT)

            vModelLab = ctk.CTkLabel(container, text="Model:", font=("Arial", 15, "bold"))
            vModelLab.pack(padx=(30, 0), pady=5, side=LEFT)

            vModel = ctk.CTkLabel(container, text=x[3], font=("Arial", 15))
            vModel.pack(pady=5, side=LEFT)

            vDistDriven = ctk.CTkLabel(container, text="Distance Driven:", font=("Arial", 15, "bold"))
            vDistDriven.pack(padx=(20, 0), pady=5, side=LEFT)

            vDist = ctk.CTkLabel(container, text=x[4], font=("Arial", 15))
            vDist.pack(pady=5, side=LEFT)

            vStatusLab = ctk.CTkLabel(container, text="Status:", font=("Arial", 15, "bold"))
            vStatusLab.pack(padx=(20, 0), pady=5, side=LEFT)

            status = x[2]
            # Vehicle Status Label
            if status == "Inactive":
                vStatus = Label(container, text=status, font=("Arial", 15), foreground='Red', background='#E0E0E0')
            elif status == "Active":
                vStatus = Label(container, text=status, font=("Arial", 15), foreground='Green', background='#E0E0E0')
            elif status == "Maintenance":
                vStatus = Label(container, text=status, font=("Arial", 15), foreground='blue', background='#E0E0E0')


            vStatus.pack(pady=5, side=LEFT)

            updateDetailButton = ctk.CTkButton(container, text='Update')
            updateDetailButton.pack(side=RIGHT)

            container2 = ctk.CTkFrame(mainCont, border_width=0)
            container2.pack(fill=BOTH)

            vNumLab = ctk.CTkLabel(container2, text="Maintenance Due:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

            vNum = ctk.CTkLabel(container2, text=x[5], font=("Arial", 15))
            vNum.pack(pady=5, side=LEFT)

            removeVehicleButton = ctk.CTkButton(container2, text='Remove',
                                                command=lambda vNum=x[0]: self.delete_and_refresh(vNum))
            removeVehicleButton.pack(side=RIGHT)

    def open_add_vehicle_window(self):
        # Create a new window for adding a vehicle
        add_vehicle_window = Toplevel(self)
        add_vehicle_window.title("Add New Vehicle")

        # Instantiate the AddVehicle class in the new window
        add_vehicle_page = AddVehicle(add_vehicle_window, self.refresh_ui)
def showVehInfo():
    app = VehicleInfo()
    app.mainloop()
    # window = Tk()
    # VehicleInfo(window)
    # window.mainloop()


if __name__ == "__main__":
    showVehInfo()
