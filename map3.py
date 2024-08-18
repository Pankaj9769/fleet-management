# import sys
#
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
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
#     window.setGeometry(0, 0, 1200, 800)
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()


import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton


class MapWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        # Load HTML content into the web view
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.2/dist/leaflet.css"
                  integrity="sha256-sA+zWATbFveLLNqWO2gtiw3HL/lh1giY/Inf1BJ0z14="
                  crossorigin=""/>
            <style>
                #map { height: 700px; }
            </style>
        </head>
        <body data-rsssl=1>
            <main>
                <div id="map"></div>
            </main>
            <script src="https://unpkg.com/leaflet@1.9.2/dist/leaflet.js"
                    integrity="sha256-o9N1jGDZrf5tS+Ft4gbIK7mYMipq9lqpVJ91xHSyKhg="
                    crossorigin=""></script>
            <script>
                var map = L.map('map').setView([19.0760, 72.8777], 13); 
                L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                }).addTo(map); 

                // Create a marker using Folium
                var icon = L.icon({
                    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.2/images/marker-icon.png',
                    iconSize: [25, 41],
                    iconAnchor: [12, 41],
                    popupAnchor: [1, -34],
                    tooltipAnchor: [16, -28],
                    shadowSize: [41, 41]
                });

                var marker = L.marker([18.5204, 73.8567], {icon: icon}).addTo(map);
            </script>
        </body>
        </html>
        """

        # 18.5204  , 73.8567
        self.webview.setHtml(html_content)

        # Add back button
        # back_button = QPushButton('Back')
        self.back_button = QPushButton('Back', self)
        self.back_button.clicked.connect(self.navigate_back)
        layout.addWidget(self.back_button)

    def navigate_back(self):
        # Hide the current widget (map page)
        self.hide()

        # Show the previous widget (dashboard page)
        if self.parent():
            self.parent().show()


def main():
    app = QApplication(sys.argv)
    window = MapWidget()
    window.setWindowTitle('Map Viewer')
    window.setGeometry(0, 0, 1200, 800)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
