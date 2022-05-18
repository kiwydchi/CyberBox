from PyQt5 import QtCore
from PyQt5.Qt import *
import sys

class Game(QMainWindow):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)

        self.level = 1
        self.initUI()
        self.initMenuBar()
        self.initGameData()

    def initUI(self):
        self.setWindowTitle("Cyberbox")
        self.resize(800, 650)
        self.setFixedSize(self.width(), self.height())

    def initGameData(self):
        if self.level == 1:
            self.data = [['em', 'em', 'em', 'em', 'bl', 'em', 'em', 'em', 'em', 'em', 'bl', 'em', 'em', 'em', 'em'],
                         ['em', 'em', 'em', 'em', 'em', 'lr', 'ud', 'lr', 'ud', 'lr', 'em', 'em', 'em', 'em', 'em'],
                         ['ud', 'em', 'em', 'em', 'em', 'em', 'al', 'em', 'al', 'em', 'em', 'em', 'em', 'em', 'ud'],
                         ['ud', 'em', 'bl', 'em', 'em', 'bl', 'em', 'ud', 'em', 'bl', 'em', 'em', 'bl', 'em', 'ud'],
                         ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
                         ['em', 'bl', 'em', 'bl', 'em', 'lr', 'em', 'al', 'em', 'lr', 'em', 'bl', 'em', 'bl', 'em'],
                         ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
                         ['ud', 'em', 'bl', 'em', 'em', 'bl', 'em', 'ud', 'em', 'bl', 'em', 'em', 'bl', 'em', 'ud'],
                         ['ud', 'em', 'em', 'em', 'bl', 'em', 'em', 'em', 'em', 'em', 'bl', 'em', 'em', 'em', 'ud'],
                         ['em', 'em', 'em', 'em', 'lr', 'lr', 'em', 'pl', 'em', 'lr', 'lr', 'em', 'em', 'em', 'em']]
        elif self.level == 2:
            self.data = [['em', 'em', 'em', 'em', 'bl', 'em', 'em', 'em', 'em', 'bl', 'bl', 'em', 'em', 'em', 'em'],
                         ['em', 'em', 'em', 'em', 'bl', 'bl', 'em', 'em', 'em', 'em', 'bl', 'em', 'em', 'em', 'em'],
                         ['em', 'em', 'lr', 'lr', 'lr', 'lr', 'lr', 'ud', 'lr', 'lr', 'lr', 'em', 'em', 'bl', 'ud'],
                         ['em', 'em', 'bl', 'em', 'em', 'em', 'em', 'al', 'ud', 'em', 'em', 'bl', 'bl', 'bl', 'ud'],
                         ['ud', 'em', 'lr', 'em', 'em', 'em', 'em', 'em', 'al', 'em', 'em', 'em', 'em', 'em', 'ud'],
                         ['ud', 'al', 'em', 'bl', 'bl', 'em', 'em', 'em', 'em', 'em', 'em', 'bl', 'em', 'em', 'em'],
                         ['ud', 'bl', 'bl', 'em', 'em', 'bl', 'bl', 'bl', 'bl', 'em', 'em', 'em', 'em', 'bl', 'em'],
                         ['ud', 'em', 'em', 'ud', 'em', 'em', 'bl', 'bl', 'bl', 'em', 'em', 'bl', 'em', 'lr', 'em'],
                         ['ud', 'em', 'bl', 'em', 'al', 'ud', 'em', 'em', 'bl', 'em', 'em', 'lr', 'ud', 'bl', 'em'],
                         ['em', 'em', 'bl', 'em', 'bl', 'em', 'em', 'pl', 'lr', 'em', 'em', 'bl', 'em', 'lr', 'em']]
        self.playerPosition = [9, 7]
        self.restartCount = 0

    def newGameStart(self, l):
        self.level = l
        self.initGameData()
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawGameGraph(qp)
        qp.end()

    def showHelp(self):
        button = QMessageBox.warning(self, "Помощь", u"Перемещение стрелками.\nЖёлтые квадраты можно двигать по горизонтали, зелёные - по вертикали, голубые - во всех направлениях. Красные блоки двигать нельзя.", QMessageBox.Ok)

    '''
    def createActions(self):
        self.helpAction = QAction(self)
        self.helpAction.triggered.connect(lambda: self.showHelp())'''

    def initMenuBar(self):
        self.statusBar()
        menubar = self.menuBar()
        '''levelmenu = menubar.addMenu('Help')
        levelmenu.addAction(self.helpAction)'''
        menubar.addAction("Help", lambda: self.showHelp())

    def drawGameGraph(self, qp):
        self.drawTiles(qp)
        self.drawLabel(self, qp)

    def drawTiles(self, qp):
        for row in range(10):
            for column in range(15):
                color = self.data[row][column]
                if color == 'bl':
                    qp.setBrush(QColor(148, 19, 73))
                elif color == 'lr':
                    qp.setBrush(QColor(196, 190, 20))
                elif color == 'ud':
                    qp.setBrush(QColor(107, 181, 33))
                elif color == 'al':
                    qp.setBrush(QColor(42, 222, 235))
                elif color == 'pu':
                    qp.setBrush(QColor(47, 18, 196))
                elif color == 'pl':
                    qp.setBrush(QColor(232, 154, 51))
                elif color == 'em':
                    qp.setBrush(QColor(255, 255, 255))
                qp.drawRect(25 + column * 50, 100 + row * 50, 45, 45)
                '''color = self.data[row][column]
                if color == 'bl':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("bl.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(20 + column * 50, 100 + row * 50)
                    labelImage.show()
                elif color == 'em':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("pu.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(25 + column * 50, 100 + row * 50)
                    labelImage.show()
                elif color == 'lr':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("lr.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(25 + column * 50, 100 + row * 50)
                    labelImage.show()
                elif color == 'ud':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("ud.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(25 + column * 50, 100 + row * 50)
                    labelImage.show()
                elif color == 'al':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("al.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(25 + column * 50, 100 + row * 50)
                    labelImage.show()
                elif color == 'pu':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("pu.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(25 + column * 50, 100 + row * 50)
                    labelImage.show()
                elif color == 'pl':
                    labelImage = QLabel(self)
                    pixmap = QPixmap("pl.png")
                    pixmap = pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio)
                    labelImage.setPixmap(pixmap)
                    labelImage.move(25 + column * 50, 100 + row * 50)
                    labelImage.show()'''
                '''
        qp.setPen(QPen(Qt.black, 6, Qt.SolidLine)'''
        '''pointx = 43 + self.p1[1] * 115
        pointy = 168 + self.p1[0] * 115
        qp.drawLine(pointx, pointy, pointx + 325, pointy)
        qp.drawLine(pointx + 325, pointy, pointx + 325, pointy + 325)
        qp.drawLine(pointx + 325, pointy + 325, pointx, pointy + 325)
        qp.drawLine(pointx, pointy + 325, pointx, pointy)'''

    @staticmethod
    def drawLabel(self, qp):
        qp.setFont(QFont("Verdana", 10, QFont.Light))
        qp.setPen(QColor(13, 10, 11))
        qp.setFont(QFont("Verdana", 20, QFont.Light))
        if self.level == 1:
            qp.drawText(250, 60, "Уровень 1")
        elif self.level == 2:
            qp.drawText(250, 60, "Уровень 2")
        elif self.level == 3:
            qp.drawText(250, 60, "Уровень 3")


    def keyPressEvent(self, e):
        keyCode = e.key()
        ret = False
        if keyCode == Qt.Key_Left:
            ret = self.move("Left")
        elif keyCode == Qt.Key_Right:
            ret = self.move("Right")
        elif keyCode == Qt.Key_Up:
            ret = self.move("Up")
        elif keyCode == Qt.Key_Down:
            ret = self.move("Down")
        elif keyCode == Qt.Key_R:
            ret = self.move("Restart")
        else:
            pass

        if ret:
            self.update()

    def move(self, direction):
        isMove = False
        if direction == "Left":
            isMove = self.moveLeft(self.playerPosition[0], self.playerPosition[1])
            if isMove:
                self.playerPosition[1] -= 1
        elif direction == "Right":
            isMove = self.moveRight(self.playerPosition[0], self.playerPosition[1])
            if isMove:
                self.playerPosition[1] += 1
        elif direction == "Up":
            isMove = self.moveUp(self.playerPosition[0], self.playerPosition[1])
            if isMove:
                self.playerPosition[0] -= 1
        elif direction == "Down":
            isMove = self.moveDown(self.playerPosition[0], self.playerPosition[1])
            if isMove:
                self.playerPosition[0] += 1
        elif direction == "Restart":
            isMove = self.restart()
        else:
            pass

        if not isMove:
            return False

        if self.isGameOver():
            button = QMessageBox.warning(self, "Поздравляем", u"Уровень пройден!",
                                         QMessageBox.Ok)
            self.newGameStart(self.level + 1)
        else:
            return True

    def isGameOver(self):
        if self.playerPosition[0] == 0 and self.playerPosition[1] == 7:
            return True
        return False

    def moveRight(self, y, x):
        if x >= 14 or self.data[y][x] == 'bl' or self.data[y][x] == 'ud' or self.data[y][x] == 'pu':
            return False
        if self.data[y][x + 1] == 'em':
            self.data[y][x + 1] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        elif self.moveRight(y, x + 1):
            self.data[y][x + 1] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        return False

    def moveLeft(self, y, x):
        if x <= 0 or self.data[y][x] == 'bl' or self.data[y][x] == 'ud' or self.data[y][x] == 'pu':
            return False
        if self.data[y][x - 1] == 'em':
            self.data[y][x - 1] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        if self.moveLeft(y, x - 1):
            self.data[y][x - 1] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        return False

    def moveUp(self, y, x):
        if y <= 0 or self.data[y][x] == 'bl' or self.data[y][x] == 'lr' or self.data[y][x] == 'pu':
            return False
        if self.data[y - 1][x] == 'em':
            self.data[y - 1][x] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        if self.moveUp(y - 1, x):
            self.data[y - 1][x] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        return False

    def moveDown(self, y, x):
        if y >= 9 or self.data[y][x] == 'bl' or self.data[y][x] == 'lr' or self.data[y][x] == 'pu':
            return False
        if self.data[y + 1][x] == 'em':
            self.data[y + 1][x] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        if self.moveDown(y + 1, x):
            self.data[y + 1][x] = self.data[y][x]
            self.data[y][x] = 'em'
            return True
        return False

    def restart(self):
        self.restartCount += 1
        if self.restartCount > 4:
            button = QMessageBox.warning(self, "Предупреждение", u"Вы проиграли",
                                         QMessageBox.Ok)
            return False
        self.newGameStart(self.level)
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Game()
    form.show()
    sys.exit(app.exec_())
