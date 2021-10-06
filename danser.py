import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from danserui import Ui_Dialog as Uid

from os import system
from pathlib import Path  # home path

from config import file
from openfile import openf

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
    openf(widget)


def play():
    system(f"danser.exe {widget.lineEdit.text()}")


def modss():
    if widget.ht.isChecked() or widget.hdfi.isChecked() or widget.ezhr.isChecked() or widget.nf.isChecked() or \
            widget.sdpf.isChecked() or widget.dtnc.isChecked() or widget.fl.isChecked():
        return True
    else:
        return False


def coninfirm():
    file(widget)


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
        level += " -tag=" + str(widget.tagc.value())
    if widget.cursors.isChecked():
        level += " -cursors=" + str(widget.cursorsc.value())

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


def checked(argument, arguments, invert: bool = True):
    if type(arguments) != list:
        arguments = [arguments]
    if not invert:
        if argument.isChecked():
            for ar in arguments:
                ar.setDisabled(True)
        else:
            for ar in arguments:
                ar.setDisabled(False)
    else:
        if not argument.isChecked():
            for ar in arguments:
                ar.setDisabled(True)
        else:
            for ar in arguments:
                ar.setDisabled(False)


def test():
    checked(widget.bloom, [widget.bloomtobeat, widget.bloomtobeatadd, widget.bloompower, widget.bloomblur,
                           widget.bloomthreshold])
    checked(widget.blur, [widget.blurintro, widget.blurnormal, widget.blurbreaks])
    checked(widget.triangles, [widget.trianglesscale, widget.trianglesspeed, widget.trianglesshadow,
                               widget.trianglesparalaxmultiplier, widget.trianglesdrawoverblur,
                               widget.trianglesdensity])
    checked(widget.knockout, widget.modlist)

    checked(widget.start, widget.starts)  # timing
    checked(widget.end, widget.ends)

    checked(widget.vsync, widget.fpscap, False)

    checked(widget.difficulty, widget.difficultyc)  # launch
    checked(widget.author, widget.authorc)
    checked(widget.title, widget.titlec)
    checked(widget.creator, widget.creatorc)
    checked(widget.cursors, widget.cursorsc)
    checked(widget.tag, widget.tagc)

    checked(widget.fullscreenbutton, [widget.winwidth, widget.winheight])


test()
# code
# buttons
widget.exit.clicked.connect(bp)
widget.coinfirm.clicked.connect(coninfirm)
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
# start&end
widget.start.clicked.connect(text)
widget.end.clicked.connect(text)
widget.starts.valueChanged.connect(text)
widget.ends.valueChanged.connect(text)

widget.ht.clicked.connect(ht)
widget.dtnc.clicked.connect(dtnc)
widget.sdpf.clicked.connect(sdpf)
widget.nf.clicked.connect(nf)

# resolution
widget.fullscreenbutton.clicked.connect(test)

# exit
sys.exit(app.exec())
