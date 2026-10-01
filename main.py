import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QListWidgetItem, QCheckBox,
    QFrame, QGraphicsDropShadowEffect, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QFont, QIcon, QPixmap, QPainter, QLinearGradient, QBrush

SKINS = [
    "Renegade Raider", "Black Knight", "Skull Trooper", "Midas",
    "Peely", "Fishstick", "Travis Scott", "Aerial Assault Trooper",
    "Ghoul Trooper", "Recon Expert", "Wildcat", "Meowscles",
]

class NumClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NumClient")
        self.setFixedSize(760, 520)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ---- root ----
        root = QWidget()
        self.setCentralWidget(root)
        root.setStyleSheet("background: transparent;")
        outer = QVBoxLayout(root)
        outer.setContentsMargins(20, 20, 20, 20)

        # ---- main frame ----
        frame = QFrame()
        frame.setObjectName("frame")
        frame.setStyleSheet("""
            QFrame#frame {
                background-color: #0d0d12;
                border-radius: 18px;
                border: 1px solid #7b2cff;
            }
        """)
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(45)
        glow.setColor(QColor(123, 44, 255, 200))
        glow.setOffset(0, 0)
        frame.setGraphicsEffect(glow)
        outer.addWidget(frame)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(14)

        # ---- title bar ----
        title_row = QHBoxLayout()
        title = QLabel("NumClient")
        title.setStyleSheet("""
            color: #b388ff;
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 3px;
        """)
        title_row.addWidget(title)
        title_row.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(28, 28)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("""
            QPushButton {
                color: #ff5c8a; background: transparent;
                border: none; font-size: 16px; font-weight: bold;
            }
            QPushButton:hover { color: #fff; background: #ff2d6f; border-radius: 6px; }
        """)
        close_btn.clicked.connect(self.close)
        title_row.addWidget(close_btn)
        layout.addLayout(title_row)

        # ---- divider ----
        line = QFrame()
        line.setFixedHeight(1)
        line.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
                           "stop:0 transparent, stop:0.5 #7b2cff, stop:1 transparent);")
        layout.addWidget(line)

        # ---- body ----
        body = QHBoxLayout()
        body.setSpacing(18)

        # skin list
        left = QVBoxLayout()
        lbl = QLabel("SKINS")
        lbl.setStyleSheet("color:#8a8aa0; font-size:11px; letter-spacing:2px; font-weight:bold;")
        left.addWidget(lbl)

        self.list = QListWidget()
        self.list.setStyleSheet("""
            QListWidget {
                background: #08080c;
                border: 1px solid #241a3d;
                border-radius: 12px;
                color: #d0d0e0;
                font-size: 13px;
                padding: 6px;
                outline: none;
            }
            QListWidget::item {
                padding: 8px 10px;
                border-radius: 8px;
            }
            QListWidget::item:selected {
                background: #7b2cff;
                color: white;
            }
            QListWidget::item:hover {
                background: #1a1030;
            }
        """)
        for s in SKINS:
            self.list.addItem(QListWidgetItem(s))
        left.addWidget(self.list)
        body.addLayout(left, 3)

        # options
        right = QVBoxLayout()
        lbl2 = QLabel("OPTIONS")
        lbl2.setStyleSheet("color:#8a8aa0; font-size:11px; letter-spacing:2px; font-weight:bold;")
        right.addWidget(lbl2)

        opts_frame = QFrame()
        opts_frame.setStyleSheet("""
            QFrame {
                background: #08080c;
                border: 1px solid #241a3d;
                border-radius: 12px;
            }
        """)
        opts_layout = QVBoxLayout(opts_frame)
        opts_layout.setContentsMargins(14, 14, 14, 14)
        opts_layout.setSpacing(10)

        for name in ["Skin Changer", "Backbling", "Pickaxe", "Emote", "Glider", "Contrail"]:
            cb = QCheckBox(name)
            cb.setCursor(Qt.PointingHandCursor)
            cb.setStyleSheet("""
                QCheckBox { color:#c8c8dd; font-size:13px; spacing:10px; }
                QCheckBox::indicator {
                    width:16px; height:16px; border-radius:4px;
                    border:1px solid #7b2cff; background:#0d0d12;
                }
                QCheckBox::indicator:checked {
                    background:#7b2cff;
                    image: none;
                    border:1px solid #b388ff;
                }
            """)
            opts_layout.addWidget(cb)

        opts_layout.addStretch()
        right.addWidget(opts_frame)
        body.addLayout(right, 2)

        layout.addLayout(body)

        # ---- status ----
        self.status = QLabel("Ready.")
        self.status.setStyleSheet("color:#6f6f85; font-size:11px;")
        layout.addWidget(self.status)

        # ---- inject button ----
        self.inject = QPushButton("INJECT")
        self.inject.setCursor(Qt.PointingHandCursor)
        self.inject.setFixedHeight(52)
        self.inject.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                            stop:0 #7b2cff, stop:1 #b14cff);
                color: white;
                font-size: 17px;
                font-weight: 900;
                letter-spacing: 4px;
                border-radius: 14px;
                border: none;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                            stop:0 #8e3dff, stop:1 #c566ff);
            }
            QPushButton:pressed {
                background: #5c1fbf;
            }
        """)
        self.inject.clicked.connect(self.on_inject)
        layout.addWidget(self.inject)

        # ---- drag window ----
        self._drag_pos = None

    def on_inject(self):
        self.status.setText("Injected successfully  ✔   (demo)")
        self.status.setStyleSheet("color:#7bff9e; font-size:11px; font-weight:bold;")
        self.inject.setText("INJECTED")
        QTimer.singleShot(2500, self.reset_btn)

    def reset_btn(self):
        self.inject.setText("INJECT")
        self.status.setText("Ready.")
        self.status.setStyleSheet("color:#6f6f85; font-size:11px;")

    # dragging frameless window
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self._drag_pos = e.globalPos() - self.frameGeometry().topLeft()
            e.accept()

    def mouseMoveEvent(self, e):
        if self._drag_pos and e.buttons() == Qt.LeftButton:
            self.move(e.globalPos() - self._drag_pos)
            e.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NumClient()
    w.show()
    sys.exit(app.exec_())