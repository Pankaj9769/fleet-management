import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import CTkComboBox, CTkButton
import mysql.connector

from connectionSQL import connection, cursor
from twilio.rest import Client

class EmpPage(tk.Tk):
    def __init__(self, dbWind=None):
        super().__init__()
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        self.geometry('1500x700')

        self.cont1 = ctk.CTkFrame(self)
        self.cont1.pack(side=TOP, pady=3)

        query = "SELECT * FROM Assign WHERE ABS(TIMESTAMPDIFF(MINUTE, NOW(), assign_time) >0)"
        cursor.execute(query)
        deleted_records = cursor.fetchall()  # Fetch the records to be deleted
        print(len(deleted_records))

        print("This", deleted_records)
        query_delete = "DELETE FROM Assign WHERE TIMESTAMPDIFF(MINUTE, assign_time, NOW()) > 0"
        cursor.execute(query_delete)
        for m in range(len(deleted_records)):
            vNum = deleted_records[m][3]
            eId = deleted_records[m][0]
            queryUpdVeh = f"Update VehicleInfo set vCurrStatus = 'Available' WHERE vNumber='{vNum}'"
            cursor.execute(queryUpdVeh)
            queryUpdEmp = f"UPDATE EmpInfo SET eCurrStatus = 'Available' WHERE emp_id = {eId}"
            cursor.execute(queryUpdEmp)
            queryUpdEmp = f"UPDATE EmpInfo SET eHours = eHours + 1 WHERE emp_id = {eId}"
            cursor.execute(queryUpdEmp)
            print('done')

        connection.commit()  # Commit the transaction

        self.backButton = ctk.CTkButton(self.cont1, text='Back', font=("Arial", 12), command=lambda : self.gotoDashBoard(dbWind))
        self.backButton.pack(side=LEFT)



        self.myFrame = ctk.CTkScrollableFrame(self, width=500, height=500)
        self.myFrame.pack(pady=0, fill="both")

        # Initial rendering of UI
        self.refresh_ui()

        self.status_combobox = CTkComboBox(self.cont1, values=["Status", "Model", "Distance Driven"])
        self.status_combobox.set("Select")  # Set the default value
        self.status_combobox.pack(side=LEFT, padx=5, pady=5)

        self.filterButton = ctk.CTkButton(self.cont1, text='Filter', font=("Arial", 12))
        self.filterButton.pack(side=LEFT, padx=(20, 0))

        # Button to open the Add Vehicle window
        self.add_vehicle_button = CTkButton(self.cont1, text="Add Vehicle")
        self.add_vehicle_button.pack(side=LEFT, padx=(20, 0))

    def delete_and_refresh(self, vNum):
        try:
            query1 = 'DELETE FROM MaintenanceRecord WHERE vNumber = %s'

            cursor.execute(query1, (vNum,))

            query = 'DELETE FROM VehicleInfo WHERE vNumber = %s'

            cursor.execute(query, (vNum,))
            connection.commit()  # Commit the transaction
            messagebox.showinfo("Note", "Vehicle removed successfully")
            self.refresh_ui()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Could not remove Vehicle: {err}")


    def gotoDashBoard(self, dbWind):
        self.cont1.destroy()
        self.destroy()
        dbWind()

    def refresh_ui(self):
        # Clear existing UI components
        for widget in self.myFrame.winfo_children():
            widget.destroy()

        # Reload data from the database
        cursor.execute('SELECT * FROM Assign')
        results = cursor.fetchall()



        # Repopulate UI with updated data
        for x in results:
            mainCont = Frame(self.myFrame, borderwidth=2, relief='groove', background='#E0e0e0')
            mainCont.pack(fill=BOTH, pady=10)

            container = ctk.CTkFrame(mainCont, border_width=0)
            container.pack(fill=BOTH)

            vNumLab = ctk.CTkLabel(container, text="Name:", font=("Arial", 15, "bold"))
            vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

            vNum = ctk.CTkLabel(container, text=x[1], font=("Arial", 15))
            vNum.pack(pady=5, side=LEFT)

            vNameLab = ctk.CTkLabel(container, text="Employee Id:", font=("Arial", 15, "bold"))
            vNameLab.pack(padx=(25, 0), pady=5, side=LEFT)

            vName = ctk.CTkLabel(container, text=x[0], font=("Arial", 15))
            vName.pack(pady=5, side=LEFT)

            vModelLab = ctk.CTkLabel(container, text="Vehicle Assigned:", font=("Arial", 15, "bold"))
            vModelLab.pack(padx=(30, 0), pady=5, side=LEFT)

            vModel = ctk.CTkLabel(container, text=x[3], font=("Arial", 15))
            vModel.pack(pady=5, side=LEFT)

            vDistDriven = ctk.CTkLabel(container, text="Vehicle Name:", font=("Arial", 15, "bold"))
            vDistDriven.pack(padx=(20, 0), pady=5, side=LEFT)

            vDistDriven = ctk.CTkLabel(container, text=x[4], font=("Arial", 15))
            vDistDriven.pack(padx=(0,0), pady=5, side=LEFT)

            current_date = datetime.now().date()
            query = f"SELECT vMaintenanceDue FROM VehicleInfo WHERE vNumber = '{x[3]}'"
            cursor.execute(query)
            res = cursor.fetchone()
            vMaintenanceDue = res[0]
            # print("THIS",vMaintenanceDue)

            account_sid = 'AC0b4943acc3c8a18dbcb6b3cbcd770fa9'
            auth_token = 'e842c23dc5247d81e4afa55ec783c86a'
            client = Client(account_sid, auth_token)

            # message = client.messages.create(
            #     from_='whatsapp:+14155238886',
            #     body=f'Dear {x[1]},\n'
            #          f'Vehicle Assigned: {x[0]}\n'
            #          f'Vehicle Name: {vName}',
            #     to=f'whatsapp:+{x[2]}'
            # )

            if vMaintenanceDue == current_date:
                account_sid = 'AC0b4943acc3c8a18dbcb6b3cbcd770fa9'
                auth_token = 'e842c23dc5247d81e4afa55ec783c86a'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=f'Dear {x[1]},\n'
                         f'Vehicle Number: {x[3]}\n'
                         f'Maintenance Due: {x[5]}',
                    to='whatsapp:+919769295104'
                )



if __name__ == "__main__":
    app = EmpPage()
    app.mainloop()
