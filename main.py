
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
