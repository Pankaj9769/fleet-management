import tkinter as tk
from tkinter import ttk
import mysql


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Page 2", font=("Arial", 18))
        label.pack(pady=10, padx=10)

        # Establish connection to the MySQL database
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="9769",
            database="s4mpr",
            port="3306"
        )

        mFrame = tk.Frame(self)
        mFrame.pack(fill="both", expand =1)

        myCanvas = tk.Canvas(mFrame)
        myCanvas.pack(side="left", fill='both', expand=1)

        scrollbar = ttk.Scrollbar(mFrame,orient='vertical',command=myCanvas.yview)
        scrollbar.pack(side='right',fill='y')

        myCanvas.configure(yscrollcommand=scrollbar.set,)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

        secFrame = tk.Frame(myCanvas)
        myCanvas.create_window((0,0), window=secFrame,anchor='nw')

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM VehicleInfo')
        result = cursor.fetchall()
        container_x = 5
        container_y = 5
        x_co = 10
        y_co = 10

        for i in result:
            results = i

            container = tk.Frame(self, bg="white", borderwidth=2, relief="groove")
            container.place(x=container_x, y=container_y, width=792, height=100)
            print(type(results[0]))
            print(results)

            vNumLab = tk.Label(self, text="Vehicle Number:", font=("Arial", 12, "bold"), foreground='black',
                               background='white')
            vNumLab.place(x=x_co, y=y_co)
            vNum = tk.Label(self, text=results[0], font=("Arial", 12), foreground='black', background='white')
            vNum.place(x=x_co+130, y=y_co)

            # Vehicle Name Label
            vNameLab = tk.Label(self, text="Vehicle Name:", font=("Arial", 12, "bold"), foreground='black',
                                background='white')
            vNameLab.place(x=x_co, y=y_co+30)
            vName = tk.Label(self, text=results[1], font=("Arial", 12), foreground='black', background='white')
            vName.place(x=x_co+115, y=y_co+30)

            # Vehicle Model Label
            vModelLab = tk.Label(self, text="Model:", font=("Arial", 12, "bold"), foreground='black',
                                 background='white')
            vModelLab.place(x=x_co+290, y=y_co)
            vModel = tk.Label(secFrame, text=results[3], font=("Arial", 12), foreground='black', background='white')
            vModel.place(x=x_co+350, y=y_co)

            # Vehicle Distance Driven Label
            vModelLab = tk.Label(self, text="Distance Driven:", font=("Arial", 12, "bold"), foreground='black',
                                 background='white')
            vModelLab.place(x=x_co+290, y=y_co+30)
            vModel = tk.Label(self, text=results[4], font=("Arial", 12), foreground='black', background='white')
            vModel.place(x=x_co+420, y=y_co+30)

            status = results[2]

            # Vehicle Status Label
            if (status == "Inactive"):
                vStatus = tk.Label(self, text=status, font=("Arial", 12), foreground='Red', background='white')
            elif (status == "Active"):
                vStatus = tk.Label(self, text=status, font=("Arial", 12), foreground='green', background='white')

            vStatusLab = tk.Label(self, text="Status:", font=("Arial", 12, "bold"), foreground='black',
                                  background='white')
            vStatusLab.place(x=x_co+540, y=y_co)

            vStatus.place(x=x_co+600, y=y_co)
            container_y+=110
            y_co+=110



