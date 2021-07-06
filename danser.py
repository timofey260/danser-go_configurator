import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from danserui import Ui_Dialog as Uid
from os import system
from pathlib import Path
from config import file

home = str(Path.home())
home = home.replace("\\", "\\\\")
# import config

app = QApplication(sys.argv)
form = QWidget()
widget = Uid()
widget.setupUi(form)
form.setWindowTitle("Danser configurator")
app_icon = QIcon()
app_icon.addFile('icon.png')
app.setWindowIcon(app_icon)
form.show()

widget.songs.setText("%s\\\\AppData\\\\Local\\\\osu!\\\\Songs" % home)
widget.skins.setText("%s\\\\AppData\\\\Local\\\\osu!\\\\Skins" % home)


def bp():
    exit()


def play():
    system(f"danser.exe {widget.lineEdit.text()}")


def modss():
    if widget.ht.isChecked() or widget.hdfi.isChecked() or widget.ezhr.isChecked() or widget.nf.isChecked() or \
            widget.sdpf.isChecked() or widget.dtnc.isChecked() or widget.fl.isChecked():
        return True
    else:
        return False


def text():
    level = ""
    if widget.author.isChecked():
        level += " -a=\"" + widget.authorc.text() + "\""
    if widget.creator.isChecked():
        level += " -c=\"" + widget.creatorc.text() + "\""
    if widget.title.isChecked():
        level += " -t=\"" + widget.titlec.text() + "\""
    if widget.difficulty.isChecked():
        level += " -d=\"" + widget.difficultyc.text() + "\""
    if widget.tag.isChecked():
        level += " -tag=\"" + widget.tagc.value() + "\""
    if widget.cursors.isChecked():
        level += " -tag=\"" + widget.cursorsc.value() + "\""

    if widget.knockout.isChecked():  # knockout mods
        mods = ""
        level += " -knockout"
        if modss():
            mods = " -mods="
            if widget.ht.isChecked():
                mods += "HT"
            if widget.nf.isChecked():
                mods += "NF"
            if widget.fl.isChecked():
                mods += "FL"

            if widget.hdfi.checkState() == Qt.CheckState.PartiallyChecked:
                mods += "HD"
            elif widget.hdfi.checkState() == Qt.CheckState.Checked:
                mods += "FI"

            if widget.dtnc.checkState() == Qt.CheckState.PartiallyChecked:
                mods += "DT"
            elif widget.dtnc.checkState() == Qt.CheckState.Checked:
                mods += "NC"

            if widget.sdpf.checkState() == Qt.CheckState.PartiallyChecked:
                mods += "SD"
            elif widget.sdpf.checkState() == Qt.CheckState.Checked:
                mods += "PF"

            if widget.ezhr.checkState() == Qt.CheckState.PartiallyChecked:
                mods += "EZ"
            elif widget.ezhr.checkState() == Qt.CheckState.Checked:
                mods += "HR"

        level += mods

    if widget.start.isChecked():
        level += f" -start={widget.starts.value()}"
    if widget.end.isChecked():
        level += f" -end={widget.ends.value()}"


    if widget.skip.isChecked():
        level += " -skip"
    if widget.qstart.isChecked():
        level += " -quickstart"
    widget.lineEdit.setText(level)
    # widget


def dtnc():
    if widget.dtnc.isChecked():
        widget.ht.setChecked(False)
    text()


def ht():
    if widget.ht.isChecked():
        widget.dtnc.setChecked(False)
    text()


def sdpf():
    if widget.sdpf.isChecked():
        widget.nf.setChecked(False)
    text()


def nf():
    if widget.nf.isChecked():
        widget.sdpf.setChecked(False)
    text()


def test():
    if not widget.bloom.isChecked():
        widget.bloomtobeat.setDisabled(True)
        widget.bloomtobeatadd.setDisabled(True)
        widget.bloompower.setDisabled(True)
        widget.bloomblur.setDisabled(True)
        widget.bloomthreshold.setDisabled(True)
    else:
        widget.bloomtobeat.setDisabled(False)
        widget.bloomtobeatadd.setDisabled(False)
        widget.bloompower.setDisabled(False)
        widget.bloomblur.setDisabled(False)
        widget.bloomthreshold.setDisabled(False)
    if not widget.blur.isChecked():
        widget.blurintro.setDisabled(True)
        widget.blurnormal.setDisabled(True)
        widget.blurbreaks.setDisabled(True)
    else:
        widget.blurintro.setDisabled(False)
        widget.blurnormal.setDisabled(False)
        widget.blurbreaks.setDisabled(False)
    if not widget.triangles.isChecked():
        widget.trianglesscale.setDisabled(True)
        widget.trianglesspeed.setDisabled(True)
        widget.trianglesshadow.setDisabled(True)
        widget.trianglesparalaxmultiplier.setDisabled(True)
        widget.trianglesdrawoverblur.setDisabled(True)
        widget.trianglesdensity.setDisabled(True)
    else:
        widget.trianglesscale.setDisabled(False)
        widget.trianglesspeed.setDisabled(False)
        widget.trianglesshadow.setDisabled(False)
        widget.trianglesparalaxmultiplier.setDisabled(False)
        widget.trianglesdrawoverblur.setDisabled(False)
        widget.trianglesdensity.setDisabled(False)

    if not widget.knockout.isChecked():  # mod list
        widget.modlist.setDisabled(True)
    else:
        widget.modlist.setDisabled(False)
    if not widget.start.isChecked():  # timing
        widget.starts.setDisabled(True)
    else:
        widget.starts.setDisabled(False)
    if not widget.end.isChecked():
        widget.ends.setDisabled(True)
    else:
        widget.ends.setDisabled(False)

    if widget.vsync.isChecked():  # vsync
        widget.fpscap.setDisabled(True)
    else:
        widget.fpscap.setDisabled(False)

    if not widget.difficulty.isChecked():
        widget.difficultyc.setDisabled(True)
    else:
        widget.difficultyc.setDisabled(False)
    if not widget.author.isChecked():
        widget.authorc.setDisabled(True)
    else:
        widget.authorc.setDisabled(False)
    if not widget.title.isChecked():
        widget.titlec.setDisabled(True)
    else:
        widget.titlec.setDisabled(False)
    if not widget.creator.isChecked():
        widget.creatorc.setDisabled(True)
    else:
        widget.creatorc.setDisabled(False)
    if not widget.cursors.isChecked():
        widget.cursorsc.setDisabled(True)
    else:
        widget.cursorsc.setDisabled(False)
    if not widget.tag.isChecked():
        widget.tagc.setDisabled(True)
    else:
        widget.tagc.setDisabled(False)


test()
# code
# buttons
widget.exit.clicked.connect(bp)
widget.coinfirm.clicked.connect(file(widget))
widget.play.clicked.connect(play)

widget.bloom.clicked.connect(test)
widget.blur.clicked.connect(test)
widget.triangles.clicked.connect(test)
widget.knockout.clicked.connect(test)
widget.start.clicked.connect(test)
widget.end.clicked.connect(test)
widget.vsync.clicked.connect(test)

widget.skip.clicked.connect(text)
widget.qstart.clicked.connect(text)
# title
widget.author.clicked.connect(test)
widget.difficulty.clicked.connect(test)
widget.title.clicked.connect(test)
widget.creator.clicked.connect(test)
widget.cursors.clicked.connect(test)
widget.tag.clicked.connect(test)

widget.tag.clicked.connect(text)
widget.cursors.clicked.connect(text)
widget.author.clicked.connect(text)
widget.difficulty.clicked.connect(text)
widget.title.clicked.connect(text)
widget.creator.clicked.connect(text)

widget.cursorsc.textChanged.connect(text)
widget.tagc.textChanged.connect(text)
widget.authorc.textChanged.connect(text)
widget.titlec.textChanged.connect(text)
widget.difficultyc.textChanged.connect(text)
widget.creatorc.textChanged.connect(text)
# reset mods
widget.knockout.clicked.connect(text)
widget.fl.clicked.connect(text)
widget.ezhr.clicked.connect(text)
widget.hdfi.clicked.connect(text)
widget.ht.clicked.connect(text)
widget.dtnc.clicked.connect(text)
widget.sdpf.clicked.connect(text)
widget.nf.clicked.connect(text)
# start&end
widget.start.clicked.connect(text)
widget.end.clicked.connect(text)
widget.starts.valueChanged.connect(text)
widget.ends.valueChanged.connect(text)

widget.ht.clicked.connect(ht)
widget.dtnc.clicked.connect(dtnc)
widget.sdpf.clicked.connect(sdpf)
widget.nf.clicked.connect(nf)

# exit
sys.exit(app.exec_())
