from PyQt5.QtCore import pyqtSignal
import socketio


class SocketIO(object):
    def __init__(self):
        self.io = socketio.Client()
