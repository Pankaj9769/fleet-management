# from tkinter import *
# from tkinter import messagebox
#
# import mysql
# from customtkinter import *
# import customtkinter as ctk
# from connectionSQL import cursor, connection
# from test4customtkinter import myFrame
#
#
# def refresh_ui():
#     # Clear existing UI components
#     for widget in myFrame.winfo_children():
#         widget.destroy()
#
#     # Reload data from the database
#     cursor.execute('SELECT * FROM VehicleInfo')
#     results = cursor.fetchall()
#
#     # Repopulate UI with updated data
#     for x in results:
#         mainCont = Frame(myFrame, borderwidth=2, relief='groove', background='#E0e0e0')
#         mainCont.pack(fill=BOTH, pady=10)
#
#         container = ctk.CTkFrame(mainCont, border_width=0)
#         container.pack(fill=BOTH)
#
#         vNumLab = ctk.CTkLabel(container, text="Vehicle Number:", font=("Arial", 15, "bold"))
#         vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)
#
#         vNum = ctk.CTkLabel(container, text=x[0], font=("Arial", 15))
#         vNum.pack(pady=5, side=LEFT)
#
#         vNameLab = ctk.CTkLabel(container, text="Vehicle Name:", font=("Arial", 15, "bold"))
#         vNameLab.pack(padx=(25, 0), pady=5, side=LEFT)
#
#         vName = ctk.CTkLabel(container, text=x[1], font=("Arial", 15))
#         vName.pack(pady=5, side=LEFT)
#
#         vModelLab = ctk.CTkLabel(container, text="Model:", font=("Arial", 15, "bold"))
#         vModelLab.pack(padx=(30, 0), pady=5, side=LEFT)
#
#         vModel = ctk.CTkLabel(container, text=x[3], font=("Arial", 15))
#         vModel.pack(pady=5, side=LEFT)
#
#         vDistDriven = ctk.CTkLabel(container, text="Distance Driven:", font=("Arial", 15, "bold"))
#         vDistDriven.pack(padx=(20, 0), pady=5, side=LEFT)
#
#         vDist = ctk.CTkLabel(container, text=x[4], font=("Arial", 15))
#         vDist.pack(pady=5, side=LEFT)
#
#         status = x[2]
#         # Vehicle Status Label
#         print(status)
#         if status == "Inactive":
#             vStatus = Label(container, text=status, font=("Arial", 15), foreground='Red', background='#E0E0E0')
#         elif status == "Active":
#             vStatus = Label(container, text=status, font=("Arial", 15), foreground='Green', background='#E0E0E0')
#         elif status == "Maintenance":
#             vStatus = Label(container, text=status, font=("Arial", 15), foreground='blue', background='#E0E0E0')
#
#         vStatusLab = ctk.CTkLabel(container, text="Status:", font=("Arial", 15, "bold"))
#         vStatusLab.pack(padx=(20, 0), pady=5, side=LEFT)
#         vStatus.pack(pady=5, side=LEFT)
#
#         updateDetailButton = ctk.CTkButton(container, text='Update')
#         updateDetailButton.pack(side=RIGHT)
#
#         container2 = ctk.CTkFrame(mainCont, border_width=0)
#         container2.pack(fill=BOTH)
#
#         vNumLab = ctk.CTkLabel(container2, text="Maintenance Due:", font=("Arial", 15, "bold"))
#         vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)
#
#         vNum = ctk.CTkLabel(container2, text=x[5], font=("Arial", 15))
#         vNum.pack(pady=5, side=LEFT)
#
#         removeVehicleButton = ctk.CTkButton(container2, text='Remove',
#                                             command=lambda vNum=x[0]: delete_and_refresh(vNum))
#         removeVehicleButton.pack(side=RIGHT)
#
#
# def delete_and_refresh(vNum):
#     try:
#         query = 'DELETE FROM VehicleInfo WHERE vNumber = %s'
#         cursor.execute(query, (vNum,))
#         connection.commit()  # Commit the transaction
#         messagebox.showinfo("Note", "Vehicle removed successfully")
#         refresh_ui()
#     except mysql.connector.Error as err:
#         messagebox.showerror("Error", f"Could not remove Vehicle: {err}")
#         print(err)