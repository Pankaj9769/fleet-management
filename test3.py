# from tkinter import *
#
# class Lab(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("ezDrive")
#         self.geometry("1000x600")
#
#         results = [("ABC678", "Skoda", 'Inactive', "2023", '23400'),
#                    ("XYZ123", "Toyota", 'Active', "2022", '30000')]
#
#         main_frame = Frame(self)
#         main_frame.pack(fill=BOTH, expand=1)
#
#         my_canvas = Canvas(main_frame)
#         my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
#
#         my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
#         my_scrollbar.pack(side=RIGHT, fill=Y)
#
#         my_canvas.config(yscrollcommand=my_scrollbar.set)
#         my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
#
#         second_frame = Frame(my_canvas)
#         my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
#
#         container = LabelFrame(second_frame, text="Vehicle Information", bg="white", borderwidth=2, relief="groove", width=970, height=100)
#         container.pack(fill=BOTH, padx=5, pady=5)
#
#
#
#         vNumLab = Label(container, text="Vehicle Number:", font=("Arial", 12, "bold"), foreground='black',background='white')
#         vNumLab.grid(row=0,column=0, padx=(15,0))
#
#         vNum = Label(container, text="ABX454", font=("Arial", 12), foreground='black', background='blue')
#         vNum.grid(row=0,column=1)
#
#         vModelLab = Label(container, text="Model:", font=("Arial", 12, "bold"), foreground='black',background='pink')
#         vModelLab.grid(row=0,column=2)
#         vModel = Label(container, text='2020', font=("Arial", 12), foreground='black', background='yellow')
#         vModel.grid(row=0,column=3)
#
#
#
#         vNumLab = Label(container, text="Vehicle Name:", font=("Arial", 12, "bold"), foreground='black',
#                         background='white')
#         vNumLab.grid(row=2, column=0)
#         #
#         vNameLab = Label(container, text="", font=("Arial", 12, "bold"), foreground='black',background='white')
#         vNameLab.grid(row=1, column=0)
#         #
#         vName = Label(container, text="Skoda", font=("Arial", 12), foreground='black', background='white')
#         vName.grid(row=2, column=1)
#         #
#         vModelLab = Label(container, text="Kms Driven:", font=("Arial", 12, "bold"), foreground='black',
#                              background='white')
#         vModelLab.grid(row=2,column=2)
#         # vModel = Label(container, text='23054', font=("Arial", 12), foreground='black', background='white')
#         # vModel.grid(row=2,column=3)
#
#         # vNumLab = Label(container, text="", font=("Arial", 12, "bold"), foreground='black',background='white')
#         #
#         # vNumLab.grid(row=1, column=0)
#         #
#         # vNumLab = Label(container, text="Vehicle Number:", font=("Arial", 12, "bold"), foreground='black',
#         #                 background='white')
#         #
#         # vNumLab.grid(row=2, column=0)
#
#
#         # for result in results:
#         #     for label_text, value in zip(["Vehicle Number:", "Vehicle Name:", "Model:", "Distance Driven:"], result):
#         #         Label(container, text=label_text, font=("Arial", 12, "bold"), foreground='black', background='white').pack(side=LEFT, padx=(10, 5), pady=5)
#         #         Label(container, text=value, font=("Arial", 12), foreground='black', background='white').pack(side=LEFT, padx=(0, 10), pady=5)
#
#             # status = result[2]
#             # status_label = Label(container, text=status, font=("Arial", 12), foreground='Red' if status == "Inactive" else 'green', background='white')
#             # status_label.pack(side=LEFT, padx=(0, 10), pady=5)
#
# if __name__ == '__main__':
#     root = Lab()
#     root.mainloop()
import customtkinter
#
# import tkinter as tk
# from tkinter import messagebox
#
#
# class AddVehicle:
#     def __init__(self, master):
#         self.master = master
#         master.title("Add New Vehicle")
#
#         # Labels and Entry fields
#         self.vehicle_name_label = tk.Label(master, text="Vehicle Name:")
#         self.vehicle_name_label.grid(row=0, column=0, padx=5, pady=5)
#         self.vehicle_name_entry = tk.Entry(master, width=30)
#         self.vehicle_name_entry.grid(row=0, column=1, padx=5, pady=5)
#
#         self.vehicle_number_label = tk.Label(master, text="Vehicle Number:")
#         self.vehicle_number_label.grid(row=1, column=0, padx=5, pady=5)
#         self.vehicle_number_entry = tk.Entry(master, width=30)
#         self.vehicle_number_entry.grid(row=1, column=1, padx=5, pady=5)
#
#         self.model_label = tk.Label(master, text="Model:")
#         self.model_label.grid(row=2, column=0, padx=5, pady=5)
#         self.model_entry = tk.Entry(master, width=30)
#         self.model_entry.grid(row=2, column=1, padx=5, pady=5)
#
#         self.status_label = tk.Label(master, text="Leased/Owned:")
#         self.status_label.grid(row=3, column=0, padx=5, pady=5)
#
#         # Leaned/Owned status options using Radiobutton
#         self.status_var = tk.StringVar(value="Leased")  # Default selection
#         self.leased_radio = tk.Radiobutton(master, text="Leased", variable=self.status_var, value="Leased")
#         self.leased_radio.grid(row=3, column=1, padx=5, pady=5)
#         self.owned_radio = tk.Radiobutton(master, text="Owned", variable=self.status_var, value="Owned")
#         self.owned_radio.grid(row=3, column=2, padx=5, pady=5)
#
#         self.distance_label = tk.Label(master, text="Distance Driven (km):")
#         self.distance_label.grid(row=4, column=0, padx=5, pady=5)
#         self.distance_entry = tk.Entry(master, width=10)  # Adjust width based on typical distance values
#         self.distance_entry.grid(row=4, column=1, padx=5, pady=5)
#         self.distance_entry.insert(0, "0")  # Pre-fill with 0
#
#         self.maintenance_label = tk.Label(master, text="Maintenance Status:")
#         self.maintenance_label.grid(row=5, column=0, padx=5, pady=5)
#         self.maintenance_entry = tk.Entry(master, width=30)
#         self.maintenance_entry.grid(row=5, column=1, padx=5, pady=5)
#
#         # Add button
#         self.add_button = tk.Button(master, text="Add Vehicle", command=self.add_vehicle)
#         self.add_button.grid(row=6, column=1, padx=5, pady=5)
#
#     def add_vehicle(self):
#         # Get user input
#         vehicle_name = self.vehicle_name_entry.get().strip()
#         vehicle_number = self.vehicle_number_entry.get().strip()
#         model = self.model_entry.get().strip()
#         status = self.status_var.get()
#         distance_driven = self.distance_entry.get().strip()
#         maintenance_status = self.maintenance_entry.get().strip()
#
#         # Basic input validation
#         if not vehicle_name:
#             messagebox.showerror("Error", "Please enter a vehicle name.")
#             return
#         if not vehicle_number:
#             messagebox.showerror("Error", "Please enter a vehicle number.")
#             return
#
#         # Process the data (print for demonstration purposes)
#         print("Vehicle Name:", vehicle_name)
#         print("Vehicle Number:", vehicle_number)
#         print("Model:", model)
#         print("Status:", status)
#         print("Distance Driven:", distance_driven)
#         print("Maintenance Status:", maintenance_status)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AddVehicle(root)
#     root.mainloop()
