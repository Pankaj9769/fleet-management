from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from twilio.rest import Client

from assignedEmp import EmpPage
from connectionSQL import cursor, connection
from empInfo import EmpInfo
from maintenanceRecord import VehicleManagementApp
from vehicleInformation import VehicleInfo
from datetime import datetime



class Dashboard2:
    def __init__(self, window):
        query = 'SELECT COUNT(emp_id) FROM EmpInfo'
        cursor.execute(query)
        driverCount = cursor.fetchall() # Fetch the count value from the result

        query2 = 'SELECT * FROM EmpInfo WHERE eCurrStatus = "Available"'
        cursor.execute(query2)
        availEmp = cursor.fetchall()
        print()
        query1 = 'SELECT * FROM VehicleInfo where vCurrStatus= "Available"'
        cursor.execute(query1)
        vehicleCount = cursor.fetchall()
        print()
        i=0
        if len(availEmp)<len(vehicleCount):
            i=len(availEmp)

        else:
            i=len(vehicleCount)


        if i>0:
            for m in range(i):
                empId = availEmp[m][0]
                empName = availEmp[m][1]
                empCont = availEmp[m][3]
                 # print(type(empCont))
                vName= vehicleCount[m][1]
                vNum =  vehicleCount[m][0]
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

                try:
                    print(vNum)

                    query2 = f"INSERT INTO Assign (emp_id, eName, eContact, vNumber, vName, assign_time) VALUES ({empId}, '{empName}', {empCont}, '{vNum}', '{vName}', '{formatted_datetime}')"
                    cursor.execute(query2)
                    queryUpdVeh = f"Update VehicleInfo set vCurrStatus = 'Not Available' WHERE vNumber='{vNum}'"
                    cursor.execute(queryUpdVeh)
                    queryUpdEmp = f"UPDATE EmpInfo SET eCurrStatus = 'Not Available' WHERE emp_id = {empId}"
                    cursor.execute(queryUpdEmp)

                    connection.commit()
                except Exception as err:
                    print("Err", err)





        self.window = window
        window.geometry("1350x750")
        self.window.title("System Management Dashboard")
        self.window.config(background='#eff5f6')
        # Window Icon Photo
        icon = PhotoImage(file=r'images\pic-icon.png')
        self.window.iconphoto(True, icon)
        self.header = Frame(self.window, bg='#3e8ecd')
        self.header.place(x=300, y=0, width=1070, height=60)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # =============================================================================
        # ============= BODY ==========================================================

        self.heading = Label(self.window, text='Revenue Graph', font=("", 15, "bold"), fg='#0064d3', bg='#c3f4f7')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.bodyFrame1 = Frame(self.window, bg='#FFFFFF')
        self.bodyFrame1.place(x=328, y=145, width=1040, height=300)

        self.bodyFrame5 = Frame(self.window, bg='#FFFFFF')
        self.bodyFrame5.place(x=328, y=145, width=600, height=250)

        # Example data (replace this with your own array of data)
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 15, 25, 30]

        # Plot the graph
        fig, ax = plt.subplots(figsize=(8, 4))

        ax.set_xlabel('Model', fontsize=18)  # Use ax.set_xlabel instead of ax.xlabel
        ax.set_ylabel('Months', fontsize=16)  # Use ax.set_ylabel instead of ax.ylabel

        ax.plot(x, y)
        ax.set_xlabel('X', fontsize=18)  # This line is redundant if you already set the xlabel above
        ax.set_ylabel('Y', fontsize=18)  # This line is redundant if you already set the ylabel above

        # Embed the graph into Tkinter window
        self.canvas = FigureCanvasTkAgg(fig, master=self.bodyFrame5)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#3e8ecd')
        self.bodyFrame2.place(x=328, y=495, width=310, height=200)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#3e8ecd')
        self.bodyFrame3.place(x=680, y=495, width=310, height=200)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#3e8ecd')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=200)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        self.logoImage = ImageTk.PhotoImage(file=r'images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='EzDrive', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=105, y=200)

        # Dashboard
        self.dashboardImage = ImageTk.PhotoImage(file=r'images/dashboard-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=287)

        # Manage
        self.manageImage = ImageTk.PhotoImage(file=r'images/manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        def gotoMaintenance():
            self.window.destroy()
            x = VehicleManagementApp(wind)
            x.mainloop()

        self.manage_text = Button(self.sidebar, text="Maintenance", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command=gotoMaintenance)
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = ImageTk.PhotoImage(file=r'images/settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=35, y=402)

        def gotoAssign():
            self.window.destroy()
            x = EmpPage(wind)
            x.mainloop()

        self.settings_text = Button(self.sidebar, text="Vehicle Assigned", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=gotoAssign)
        self.settings_text.place(x=80, y=402)

        # Vehicle Information
        self.ExitImage = ImageTk.PhotoImage(file=r'images/car.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=25, y=460)

        def gotoVehicle():
            self.window.destroy()
            x = VehicleInfo(wind)
            x.mainloop()

        self.Exit_text = Button(self.sidebar, text="Vehicle Information", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff',command=gotoVehicle)
        self.Exit_text.place(x=85, y=462)
        # Employee Information
        self.anotherPointerImage = ImageTk.PhotoImage(file=r'images/profile.png')
        self.anotherPointer = Label(self.sidebar, image=self.anotherPointerImage, bg='#ffffff')
        self.anotherPointer.place(x=35, y=512)

        def gotoEmp():
            self.window.destroy()
            x = EmpInfo(wind)
            x.mainloop()

        self.anotherPointer_text = Button(self.sidebar, text="Employee Information", bg='#ffffff',
                                          font=("", 13, "bold"), bd=0,
                                          cursor='hand2', activebackground='#ffffff',  command=gotoEmp)
        self.anotherPointer_text.place(x=80, y=512)
        # Exit
        self.newPointerImage = ImageTk.PhotoImage(file=r'images/exit-icon.png')
        self.newPointer = Label(self.sidebar, image=self.newPointerImage, bg='#ffffff')
        self.newPointer.place(x=27, y=562)

        self.newPointer_text = Button(self.sidebar, text="Exit", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                      cursor='hand2', activebackground='#ffffff')
        self.newPointer_text.place(x=90, y=570)

        # ============= BODY ==========================================================

        # Body Frame 2
        self.total_people = Label(self.bodyFrame2, text=driverCount, bg='#3e8ecd', font=("", 25, "bold"), fg='white')
        self.total_people.place(x=120, y=100)

        self.totalPeopleImage = ImageTk.PhotoImage(file=r'images/left-icon.png')
        self.totalPeople = Label(self.bodyFrame2, image=self.totalPeopleImage, bg='#3e8ecd')
        self.totalPeople.place(x=220, y=10)

        self.totalPeople_label = Label(self.bodyFrame2, text="Total Drivers", bg='#3e8ecd', font=("", 20, "bold"),
                                       fg='white')
        self.totalPeople_label.place(x=5, y=5)
        # Body Frame 3
        self.people_left = Label(self.bodyFrame3, text='$3,000.00', bg='#3e8ecd', font=("", 25, "bold"), fg='white')
        self.people_left.place(x=90, y=100)

        # left icon
        self.LeftImage = ImageTk.PhotoImage(file=r'images/earn3.png')
        self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#3e8ecd')
        self.Left.place(x=220, y=10)

        self.peopleLeft_label = Label(self.bodyFrame3, text="Montly income", bg='#3e8ecd', font=("", 20, "bold"),
                                      fg='white')
        self.peopleLeft_label.place(x=5, y=5)

        # Body Frame 4
        self.total_earnings = Label(self.bodyFrame4, text='$40,000.00', bg='#3e8ecd', font=("", 25, "bold"), fg='white')
        self.total_earnings.place(x=80, y=100)

        self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#3e8ecd', font=("", 20, "bold"),
                                    fg='white')
        self.earnings_label.place(x=5, y=5)
        # Frame 4 icon
        self.earningsIcon_image = ImageTk.PhotoImage(file=r'images/earn3.png')
        self.earningsIcon = Label(self.bodyFrame4, image=self.earningsIcon_image, bg='#3e8ecd')
        self.earningsIcon.place(x=220, y=0)

        # date and Time
        self.clock_image = ImageTk.PhotoImage(file=r"images/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)


def wind():
    window = Tk()
    Dashboard2(window)
    window.mainloop()


if __name__ == '__main__':
    wind()
