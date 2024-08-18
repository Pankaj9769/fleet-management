import tkinter as tk
import mysql.connector

# Establish connection to the MySQL database
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="9769",
    database="s4mpr",
    port="3306"
)

cursor = connection.cursor()


mainWindow = tk.Tk()
mainWindow.geometry("800x550+200+50")


container = tk.Frame(mainWindow, bg="#7393B3", borderwidth=2,relief="groove")
container.place(x=3, y=4, width=794, height=200)


#
# def fetchCarInfo():
#     global results
#     cursor.execute('SELECT * FROM VehicleInfo where vDistDriven=18000')
#     results = cursor.fetchone()
#     # Vehicle Number Label
#     vNumLab = tk.Label(container, text="Vehicle Number:", font=("Arial", 12, "bold"), foreground='White',
#                        background='#7393B3');
#     vNumLab.place(x=10, y=10)
#     vNum = tk.Label(container, text=results[0], font=("Arial", 12), foreground='White', background='#7393B3')
#     vNum.place(x=140, y=10)
#
#     # Vehicle Name Label
#     vNameLab = tk.Label(container, text="Vehicle Name:", font=("Arial", 12, "bold"), foreground='White',
#                         background='#7393B3');
#     vNameLab.place(x=10, y=40)
#     vName = tk.Label(container, text=results[1], font=("Arial", 12), foreground='White', background='#7393B3')
#     vName.place(x=125, y=40)
#
#     # Vehicle Model Label
#     vModelLab = tk.Label(container, text="Model:", font=("Arial", 12, "bold"), foreground='White',
#                          background='#7393B3')
#     vModelLab.place(x=300, y=10)
#     vModel = tk.Label(container, text=results[3], font=("Arial", 12), foreground='White', background='#7393B3')
#     vModel.place(x=360, y=10)
#
#     # Vehicle Distance Driven Label
#     vModelLab = tk.Label(container, text="Distance Driven:", font=("Arial", 12, "bold"), foreground='White',
#                          background='#7393B3')
#     vModelLab.place(x=300, y=40)
#     vModel = tk.Label(container, text=results[4], font=("Arial", 12), foreground='White', background='#7393B3')
#     vModel.place(x=430, y=40)
#
#     status = results[2]
#
#     # Vehicle Status Label
#     if (status == "Inactive"):
#         vStatus = tk.Label(container, text=status, font=("Arial", 12), foreground='Orange', background='#7393B3')
#     elif (status == "Active"):
#         vStatus = tk.Label(container, text=status, font=("Arial", 12), foreground='lightgreen', background='#7393B3')
#
#     vStatusLab = tk.Label(container, text="Status:", font=("Arial", 12, "bold"), foreground='White',
#                           background='#7393B3')
#     vStatusLab.place(x=550, y=10)
#
#     vStatus.place(x=610, y=10)
def fetchCarInfo():
    global results
    cursor.execute('SELECT * FROM VehicleInfo WHERE vDistDriven=18000')
    results = cursor.fetchall()  # Fetch all rows matching the condition

    # Y-coordinate for label placement
    y_coordinate = 100

    for vehicle in results:
        # Vehicle Number Label
        vNumLab = tk.Label(container, text="Vehicle Number:", font=("Arial", 12, "bold"), foreground='White',
                           background='#7393B3')
        vNumLab.place(x=10, y=y_coordinate)
        vNum = tk.Label(container, text=vehicle[0], font=("Arial", 12), foreground='White', background='#7393B3')
        vNum.place(x=140, y=y_coordinate)

        # Vehicle Name Label
        vNameLab = tk.Label(container, text="Vehicle Name:", font=("Arial", 12, "bold"), foreground='White',
                            background='#7393B3')
        vNameLab.place(x=10, y=y_coordinate + 30)
        vName = tk.Label(container, text=vehicle[1], font=("Arial", 12), foreground='White', background='#7393B3')
        vName.place(x=125, y=y_coordinate + 30)

        # Vehicle Model Label
        vModelLab = tk.Label(container, text="Model:", font=("Arial", 12, "bold"), foreground='White',
                             background='#7393B3')
        vModelLab.place(x=300, y=y_coordinate)
        vModel = tk.Label(container, text=vehicle[3], font=("Arial", 12), foreground='White', background='#7393B3')
        vModel.place(x=360, y=y_coordinate)

        # Vehicle Distance Driven Label
        vDistLab = tk.Label(container, text="Distance Driven:", font=("Arial", 12, "bold"), foreground='White',
                             background='#7393B3')
        vDistLab.place(x=300, y=y_coordinate + 30)
        vDist = tk.Label(container, text=vehicle[4], font=("Arial", 12), foreground='White', background='#7393B3')
        vDist.place(x=430, y=y_coordinate + 30)

        # Vehicle Status Label
        status = vehicle[2]
        if status == "Inactive":
            vStatus = tk.Label(container, text=status, font=("Arial", 12), foreground='Orange', background='#7393B3')
        elif status == "Active":
            vStatus = tk.Label(container, text=status, font=("Arial", 12), foreground='lightgreen', background='#7393B3')

        vStatusLab = tk.Label(container, text="Status:", font=("Arial", 12, "bold"), foreground='White',
                              background='#7393B3')
        vStatusLab.place(x=550, y=y_coordinate)
        vStatus.place(x=610, y=y_coordinate)

        # Update the y-coordinate for the next set of labels
        y_coordinate += 70  # Adjust as needed

    # Update the position of the Fetch button

# Initial call to fetch data
fetchCarInfo()





b1 = tk.Button(container, text="Fetch", command=fetchCarInfo)
b1.place(x=5, y=100)





mainWindow.mainloop()

