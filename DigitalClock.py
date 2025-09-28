## Unique Digital Clock using Python (PyQt5)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00", self)
        self.date_label = QLabel("", self)   
        self.toggle_button = QPushButton("Switch to 24-Hour Clock", self)

        self.timer = QTimer(self)
        self.use_12_hour = True  

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 400, 200)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.toggle_button)
        self.setLayout(vbox)


        # Time label styling
        self.time_label.setAlignment(Qt.AlignCenter)
        self.date_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 90px; color: lime;")
        self.date_label.setStyleSheet("font-size: 30px; color: cyan;")
        self.toggle_button.setStyleSheet("font-size: 18px; padding: 5px;" 
                                         "color: orange;")
        self.setStyleSheet("background-color: black;")


        # Try to load custom font
        font_id = QFontDatabase.addApplicationFont(r"d:\Python course\All Exercises\DS-DIGIT.TTF")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 90, QFont.Bold, italic=True)
        else:
            # Fallback font
            my_font = QFont("Arial", 90, QFont.Bold, italic=True)

        self.time_label.setFont(my_font)


        # Connect toggle button
        self.toggle_button.clicked.connect(self.toggle_format)


        # Timer to update every second
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Initial update
        self.update_time()
        

    def toggle_format(self):
        """Switch between 12-hour and 24-hour format"""
        self.use_12_hour = not self.use_12_hour
        if self.use_12_hour:
            self.toggle_button.setText("Switch to 24-Hour")
        else:
            self.toggle_button.setText("Switch to 12-Hour")
        self.update_time()


    def update_time(self):
        """Update time and date display"""
        
        if self.use_12_hour:
            current_time = QTime.currentTime().toString("hh:mm:ss AP")
        else:
            current_time = QTime.currentTime().toString("HH:mm:ss")

        current_date = QDate.currentDate().toString("dddd, MMMM dd yyyy")

        self.time_label.setText(current_time)
        self.date_label.setText(current_date)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
