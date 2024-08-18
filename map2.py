import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class LocationWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Create a web engine view
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
        </head>
        <body data-rsssl=1>
            <div id="output"></div>
            <script>
                const options = {
                    enableHighAccuracy: true,
                    timeout: 5000,
                    maximumAge: 2000
                };

                navigator.geolocation.watchPosition(success, error, options);

                function success(pos) {
                    const lat = pos.coords.latitude;
                    const lng = pos.coords.longitude;
                    const accuracy = pos.coords.accuracy;

                    document.getElementById('output').innerText = `
                        User coordinates: 
                        Latitude ${lat}.
                        Longitude ${lng}.
                        Estimation accurate within ${Math.round(accuracy)} metres.`;
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
    window = LocationWidget()
    window.setWindowTitle('Location Tracker')
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
