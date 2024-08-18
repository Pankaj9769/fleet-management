# from twilio.rest import Client
# import pywhatkit
# account_sid = 'AC0b4943acc3c8a18dbcb6b3cbcd770fa9'
# auth_token = 'e842c23dc5247d81e4afa55ec783c86a'
# client = Client(account_sid, auth_token)
# pywhatkit.sendwhatmsg("+919769295104", "Hi Pankaj",00,41)
# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='HELLO SIR!',
#   to='whatsapp:+919167646099'
# )
# #
# # print(message.sid)
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtWebEngineWidgets import QWebEngineView
#
# class MapWidget(QWidget):
#     def __init__(self, latitude, longitude, parent=None):
#         super().__init__(parent)
#
#         # Create a layout
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         # Create a web engine view
#         self.webview = QWebEngineView()
#         layout.addWidget(self.webview)
#
#         # Load the map with the specified latitude and longitude
#         html = f"""
#         <!DOCTYPE html>
#         <html>
#             <head>
#                 <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
#                 <meta charset="utf-8">
#                 <style>
#                     /* Set the size of the div element that contains the map */
#                     #map {{
#                         height: 400px;
#                         width: 100%;
#                     }}
#                 </style>
#             </head>
#             <body>
#                 <div id="map"></div>
#                 <script>
#                     function initMap() {{
#                         var location = {{lat: {latitude}, lng: {longitude}}};
#                         var map = new google.maps.Map(document.getElementById('map'), {{
#                             zoom: 10,
#                             center: location
#                         }});
#                         var marker = new google.maps.Marker({{
#                             position: location,
#                             map: map
#                         }});
#                     }}
#                 </script>
#                 <script src="https://maps.googleapis.com/maps/api/js?key=JTv2cWdDa-5rRcu_dsHUBn4hXTVKsp8GP0T0EUNkS50&callback=initMap" async defer></script>
#             </body>
#         </html>
#         """
#         self.webview.setHtml(html)
#
# def main():
#     latitude = 40.7128  # Example latitude
#     longitude = -74.0060  # Example longitude
#
#     app = QApplication(sys.argv)
#     window = QWidget()
#     layout = QVBoxLayout()
#     window.setLayout(layout)
#
#     # Create the map widget
#     map_widget = MapWidget(latitude, longitude)
#     layout.addWidget(map_widget)
#
#     window.setWindowTitle('Map Plotter')
#     window.setGeometry(100, 100, 800, 600)
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWidget(QWidget):
    def __init__(self):
        super().__init__()

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
                #map { height: 350px; }
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
                const map = L.map('map'); 
                map.setView([51.505, -0.09], 13); 
                L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                }).addTo(map); 
                let marker, circle, zoomed;
                navigator.geolocation.watchPosition(success, error);
                function success(pos) {
                    const lat = pos.coords.latitude;
                    const lng = pos.coords.longitude;
                    const accuracy = pos.coords.accuracy;
                    if (marker) {
                        map.removeLayer(marker);
                        map.removeLayer(circle);
                    }
                    marker = L.marker([lat, lng]).addTo(map);
                    circle = L.circle([lat, lng], { radius: accuracy }).addTo(map);
                    if (!zoomed) {
                        zoomed = map.fitBounds(circle.getBounds()); 
                    }
                    map.setView([lat, lng]);
                }
                function error(err) {
                    if (err.code === 1) {
                        alert("Please allow geolocation access");
                    } else {
                        alert("Cannot get current location");
                    }
                }
            </script>
        </body>
        </html>
        """
        self.webview.setHtml(html_content)

def main():
    app = QApplication(sys.argv)
    window = MapWidget()
    window.setWindowTitle('Map Viewer')
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
