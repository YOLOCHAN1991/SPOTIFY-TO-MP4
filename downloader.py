import os
import subprocess
from PyQt6 import QtCore, QtGui, QtWidgets
import enum
from SpottoYou import SpottoYou, get_config, link_type

class YoutubeDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.config = get_config()
        self.spotify = SpottoYou(self.config["client_id"], self.config["client_secret"])

        # Create the UI
        self.url_input = QtWidgets.QLineEdit()
        self.download_button = QtWidgets.QPushButton("Download")
        self.download_button.clicked.connect(self.download)
        self.progress = QtWidgets.QProgressBar()
        self.progress.setValue(0)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress)
        
        self.setLayout(layout)
        self.setWindowTitle("YouTube Downloader")

    def download(self):
        url = self.url_input.text()
        
        #output_path = self.lineEdit_output.text()
        if not url:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a valid URL and select a location to save the video.")
            return
        try:

            link = link_type(url)
                
            if link == "Spotify song":
                success = self.spotify.download_track_bestaudio(self.spotify.splink_to_ytlink(url))
            elif link == "Spotify playlist":
                success =  self.spotify.download_playlist(url)
            elif link == "YouTube video":
                success = self.spotify.download_track_bestaudio(url)
            else:
                success = None

            if not success:
                QtWidgets.QMessageBox.information(self, "Fail", "Something went wrong very wrong, imminent danger i think. Oh no. just a bad link, ups.!")
            else:
                QtWidgets.QMessageBox.information(self, "Success", "Video downloaded successfully!")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    downloader = YoutubeDownloader()
    downloader.show()
    app.exec()
