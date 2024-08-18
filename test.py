# import sys
#
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
#
#
# class MapWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         self.webview = QWebEngineView()
#         layout.addWidget(self.webview)
#
#         # Load HTML content into the web view
#         html_content = """
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta http-equiv="X-UA-Compatible" content="IE=edge">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Document</title>
#             <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.2/dist/leaflet.css"
#                   integrity="sha256-sA+zWATbFveLLNqWO2gtiw3HL/lh1giY/Inf1BJ0z14="
#                   crossorigin=""/>
#             <style>
#                 #map { height: 700px; }
#             </style>
#         </head>
#         <body data-rsssl=1>
#             <main>
#                 <div id="map"></div>
#             </main>
#             <script src="https://unpkg.com/leaflet@1.9.2/dist/leaflet.js"
#                     integrity="sha256-o9N1jGDZrf5tS+Ft4gbIK7mYMipq9lqpVJ91xHSyKhg="
#                     crossorigin=""></script>
#             <script>
#                 var map = L.map('map').setView([19.0760, 72.8777], 13);
#                 L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
#                     maxZoom: 19,
#                     attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
#                 }).addTo(map);
#
#                 // Create a marker using Folium
#                 var icon = L.icon({
#                     iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.2/images/marker-icon.png',
#                     iconSize: [25, 41],
#                     iconAnchor: [12, 41],
#                     popupAnchor: [1, -34],
#                     tooltipAnchor: [16, -28],
#                     shadowSize: [41, 41]
#                 });
#
#                 var marker = L.marker([18.5204, 73.8567], {icon: icon}).addTo(map);
#             </script>
#         </body>
#         </html>
#         """
#
#         # 18.5204  , 73.8567
#         self.webview.setHtml(html_content)
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MapWidget()
#     window.setWindowTitle('Map Viewer')
#     window.setGeometry(100, 100, 1200, 800)
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()

import tkinter as tk
import mysql.connector

from test2 import Page2


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Page 1", font=("Arial", 18))
        label.pack(pady=10, padx=10)

        # button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        # button.pack()

        b1 = tk.Button(self, text="Fetch", command=lambda: controller.show_frame(Page2))
        b1.place(x=5, y=100)


            # Vehicle Number Labe


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.geometry("800x500")
    app.mainloop()


