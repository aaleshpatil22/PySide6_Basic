import sys
import time

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QHBoxLayout, QSlider, QStyle
from PySide6.QtGui import QPixmap,QIcon
from PySide6 import QtCore
import vlc
from urllib.parse import urlparse,unquote
from qt_material import apply_stylesheet

class SongMetadataReader(QWidget):
    def __init__(self,app):
        super().__init__()
        self.app=app
        self.setWindowTitle('Alex_Player')
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout(self)
        self.label = QLabel('Select a song to Play')
        self.cover_label = QLabel()
        self.meta_layeout = QHBoxLayout()
        self.meta_layeout.addWidget(self.cover_label)
        self.meta_layeout.addWidget(self.label)
        self.layout.addLayout(self.meta_layeout)
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_song)
        self.layout.addWidget(self.browse_button)
        self.button_play = QPushButton("Play/Pause")
        self.button_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.button_play.clicked.connect(self.play)
        self.layout.addWidget(self.button_play)
        self.slider_layout = QHBoxLayout()
        self.slider0_label = QLabel("00:00")
        self.slider1_label = QLabel("00:00")
        self.position_slider = QSlider(QtCore.Qt.Horizontal)
        self.position_slider.setMinimum(0)
        self.position_slider.setMaximum(100)
        self.position_slider.setValue(0)
        #self.position_slider.valueChanged.connect(self.on_slider_move)
        self.slider_layout.addWidget(self.slider0_label)
        self.slider_layout.addWidget(self.position_slider)
        self.slider_layout.addWidget(self.slider1_label)

        self.volume_layout = QHBoxLayout()
        self.mute_button = QPushButton("")
        self.mute_button.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        try:
            self.mute_button.clicked.connect(self.mute_audio)
        except:
            print("not")
        self.volume_label = QLabel("Volume")
        self.volume_slider = QSlider(QtCore.Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(30)
        self.volume_slider.valueChanged.connect(self.volume_slider_move)
        self.volume_layout.addWidget(self.mute_button)
        self.volume_layout.addWidget(self.volume_label)
        self.volume_layout.addWidget(self.volume_slider)

        # .connect(self.on_slider_move)
        self.layout.addLayout(self.slider_layout)
        self.layout.addLayout(self.volume_layout)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_position_slider)
        self.media_player = None

    def mute_audio(self):
        try:
            if self.media_player.audio_get_volume() != 0:
                self.media_player.audio_set_volume(0)
                self.volume_slider.setValue(0)
                self.mute_button.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))
            else:
                self.media_player.audio_set_volume(30)
                self.volume_slider.setValue(30)
                self.mute_button.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        except:
            pass

    def play(self):
        try:
            if str(self.media_player.get_state()) == "State.NothingSpecial" or str(self.media_player.get_state()) == "State.Paused":
                self.media_player.play()
                self.button_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
                time.sleep(3)
                milliseconds = self.media_player.get_length()
                seconds = int(milliseconds / 1000)
                minutes = seconds // 60
                seconds = seconds % 60
                print(f"{minutes:02d}:{seconds:02d}")
                self.slider1_label.setText(f"{minutes:02d}:{seconds:02d}")
                self.timer.start(500)
            elif str(self.media_player.get_state()) == "State.Ended":
                self.label.setText("Please Select File")
                self.cover_label.setPixmap(QPixmap(""))
                self.button_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
                self.timer.stop()
            else:
                print(self.media_player.get_state())
                self.media_player.pause()
                self.button_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
                self.timer.stop()
        except:
            self.label.setText("Please Select File")

    def on_slider_move(self, value):
        try:
            position = float(value) / 100.0
            self.media_player.set_position(position)
        except:
            self.label.setText("Please Select File")

    def update_position_slider(self):
        try:
            position = self.media_player.get_position()
            if position is not None:
                value = int(position * 100)
                self.position_slider.setValue(value)
        except:
            pass

    def volume_slider_move(self, value):
        try:
            position = int(value)
            self.media_player.audio_set_volume(position)
        except:
            self.label.setText("Please Select File")


    def browse_song(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Song File', '')
        if file_path:
            try:
                self.media_player.release()
            except:
                pass
            self.read_metadata(file_path)

    def read_metadata(self, file_path):

        try:

            instance = vlc.Instance()
            self.media_player = instance.media_player_new()
            media = instance.media_new(file_path)
            self.media_player.set_media(media)
            media.parse()
            self.volume_slider.setValue(self.media_player.audio_get_volume())
            self.position_slider.setValue(0)
            #self.button_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            #self.media_player.play()

            if media:
                metadata = {
                    'Title': media.get_meta(vlc.Meta.Title) if media.get_meta(vlc.Meta.Title) else 'N/A',
                    'Artist': media.get_meta(vlc.Meta.Artist) if media.get_meta(vlc.Meta.Artist) else 'N/A',
                    'Album': media.get_meta(vlc.Meta.Album) if media.get_meta(vlc.Meta.Album) else 'N/A',
                    'Year': media.get_meta(vlc.Meta.Date) if media.get_meta(vlc.Meta.Date) else 'N/A',
                    'Genre': media.get_meta(vlc.Meta.Genre) if media.get_meta(vlc.Meta.Genre) else 'N/A'
                }
                info_text = ''
                for key, value in metadata.items():
                    info_text += f'{key}: {value}\n'
                self.label.setText(info_text)
                time.sleep(3)
                milliseconds = self.media_player.get_length()
                seconds = int(milliseconds / 1000)
                minutes = seconds // 60
                seconds = seconds % 60
                print(f"{minutes:02d}:{seconds:02d}")
                self.slider1_label.setText(f"{minutes:02d}:{seconds:02d}")

                # Convert bytes to QPixmap
                artwork_url = unquote(urlparse(media.get_meta(vlc.Meta.ArtworkURL)).path)
                print(f"Artwork URL: {artwork_url}")

                # Check if the artwork_url is not null before attempting to create a QPixmap
                if artwork_url:
                    pixmap = QPixmap()
                    pixmap.load(artwork_url[1:])

                    # Check if the pixmap is null before scaling
                    if not pixmap.isNull():
                        pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
                        self.cover_label.setPixmap(pixmap)
                    else:
                        print("Error: Pixmap is null")
                else:
                    print("Error: Artwork URL is null")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SongMetadataReader(app)
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    sys.exit(app.exec())