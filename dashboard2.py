from tkinter import *
from PIL import ImageTk, Image
import time
import pandas as pd
import matplotlib.pyplot as plt

from maintenanceRecord import VehicleManagementApp


class Dashboard2():
    def __init__(self, window):
        self.window = window
        window.geometry("1350x750")
        self.window.title("System Management Dashboard")
        self.window.config(background='#eff5f6')
        # Window Icon Photo
        icon = PhotoImage(file='images\\pic-icon.png')
        self.window.iconphoto(True, icon)
        self.header = Frame(self.window, bg='#3e8ecd')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header, text="Logout", bg='#04818a', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=950, y=15)


        # ================== SIDEBAR ===================================================

        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)


        # ============= BODY ==========================================================

        self.heading = Label(self.window, text='Revenue Graph', font=("", 15, "bold"), fg='#0064d3', bg='#c3f4f7')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#3e8ecd')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#3e8ecd')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#3e8ecd')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)


        # ================== SIDEBAR ===================================================


        # logo
        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='EzDrive', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=105, y=200)

        # Dashboard
        self.dashboardImage = ImageTk.PhotoImage(file='images/dashboard-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=287)

        # Manage
        self.manageImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        def gotoMaintenance():
            self.window.destroy()
            x = VehicleManagementApp(wind)
            x.mainloop()

        self.manage_text = Button(self.sidebar, text="Maintainence", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command=gotoMaintenance)
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = ImageTk.PhotoImage(file='images/settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text="Vehicle Tracking", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)

        # Exit
        self.ExitImage = ImageTk.PhotoImage(file='images/exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=25, y=452)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff')
        self.Exit_text.place(x=85, y=462)
        # Vehicle Info
        self.anotherPointerImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.anotherPointer = Label(self.sidebar, image=self.anotherPointerImage, bg='#ffffff')
        self.anotherPointer.place(x=35, y=512)  # Adjust the y-coordinate to position it below the Exit block

        self.anotherPointer_text = Button(self.sidebar, text="Vehicle Info", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                          cursor='hand2', activebackground='#ffffff')
        self.anotherPointer_text.place(x=80, y=512)  # Adjust the y-coordinate to position it below the Exit block
        # New Pointer
        self.newPointerImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.newPointer = Label(self.sidebar, image=self.newPointerImage, bg='#ffffff')
        self.newPointer.place(x=35, y=562)  # Adjust the y-coordinate to position it below the "Vehicle Info" block

        self.newPointer_text = Button(self.sidebar, text="Employee info", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                      cursor='hand2', activebackground='#ffffff')
        self.newPointer_text.place(x=80, y=562)  # Adjust the y-coordinate to position it below the "Vehicle Info" block


        # ============= BODY ==========================================================

        # Graph
        # Display the graph
        plt.style.use('bmh')
        df = pd.read_csv('prices.csv')
        x = df['Model']
        y = df['Price']
        plt.xlabel('Model', fontsize=18)
        plt.ylabel('Price($)', fontsize=16)
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.savefig('images/graph.png', bbox_inches='tight')  # Save the plot with tight bounding box

        # Resize the image to fit the frame
        graph_image = Image.open('images/graph.png')
        graph_image = graph_image.resize((700, 350))
        self.graph_image = ImageTk.PhotoImage(graph_image)

        self.graph = Label(self.bodyFrame1, image=self.graph_image, bg='#ffffff')
        self.graph.place(x=0, y=0)

        # Body Frame 2
        self.total_people = Label(self.bodyFrame2, text='230', bg='#3e8ecd', font=("", 25, "bold"), fg='white')
        self.total_people.place(x=120, y=100)

        self.totalPeopleImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.totalPeople = Label(self.bodyFrame2, image=self.totalPeopleImage, bg='#3e8ecd')
        self.totalPeople.place(x=220, y=10)

        self.totalPeople_label = Label(self.bodyFrame2, text="Total Drivers", bg='#3e8ecd', font=("", 20, "bold"),
                                       fg='white')
        self.totalPeople_label.place(x=5, y=5)

        # Body Frame 3
        self.people_left = Label(self.bodyFrame3, text='50', bg='#3e8ecd', font=("", 25, "bold"), fg='white')
        self.people_left.place(x=120, y=100)

        # left icon
        self.LeftImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#3e8ecd')
        self.Left.place(x=220, y=10)

        self.peopleLeft_label = Label(self.bodyFrame3, text="Left", bg='#3e8ecd', font=("", 20, "bold"),
                                      fg='white')
        self.peopleLeft_label.place(x=5, y=5)

        # Body Frame 4
        self.total_earnings = Label(self.bodyFrame4, text='$40,000.00', bg='#3e8ecd', font=("", 25, "bold"), fg='white')
        self.total_earnings.place(x=80, y=100)

        self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#3e8ecd', font=("", 20, "bold"),
                                    fg='white')
        self.earnings_label.place(x=5, y=5)
        # Frame 4 icon
        self.earningsIcon_image = ImageTk.PhotoImage(file='images/earn3.png')
        self.earningsIcon = Label(self.bodyFrame4, image=self.earningsIcon_image, bg='#3e8ecd')
        self.earningsIcon.place(x=220, y=0)

        # date and Time
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
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
