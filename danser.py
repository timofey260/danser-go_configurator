import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from danserui import Ui_Dialog as Uid
from os import system
from pathlib import Path

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

load = ""
widget.songs.setText("%s\\\\AppData\\\\Local\\\\osu!\\\\Songs" % home)
widget.skins.setText("%s\\\\AppData\\\\Local\\\\osu!\\\\Skins" % home)


def bp():
    exit()


def booltostr(r: bool):
    if r:
        return "true"
    else:
        return "false"


def configure():
    f = open("settings.json", "w")
    f.write(
        '{\n'
        '	"General": {\n'
        f'		"OsuSongsDir": "{widget.songs.text()}",\n'
        f'		"OsuSkinsDir": "{widget.skins.text()}",\n'
        '		"DiscordPresenceOn": true,\n'
        '		"UnpackOszFiles": true\n'
        '	},\n'
        '	"Graphics": {\n'
        '		"Width": 1920,\n'
        '		"Height": 1080,\n'
        '		"WindowWidth": 1440,\n'
        '		"WindowHeight": 810,\n'
        f'		"Fullscreen": {booltostr(widget.fullscreenbutton.isChecked())},\n'
        f'		"VSync": {booltostr(widget.vsync.isChecked())},\n'
        f'		"FPSCap": {widget.fpscap.value()},\n'
        f'		"MSAA": {widget.msaa.value()},\n'
        f'		"ShowFPS": {booltostr(widget.showfps.isChecked())},\n'
        '		"Experimental": {\n'
        f'			"UsePersistentBuffers": {booltostr(widget.usepersistentbuffers.isChecked())}\n'
        '		}\n'
        '	},\n'
        '	"Audio": {\n'
        f'		"GeneralVolume": {widget.generalvolume.value()},\n'
        f'		"MusicVolume": {widget.musicvolume.value()},\n'
        f'		"SampleVolume": {widget.samplevolume.value()},\n'
        f'		"Offset": {widget.offset.value()},\n'
        f'		"HitsoundPositionMultiplier": {widget.positionmultiplier.value()},\n'
        f'		"IgnoreBeatmapSamples": {booltostr(widget.ignoresamples.isChecked())},\n'
        f'		"IgnoreBeatmapSampleVolume": {booltostr(widget.ignoresamplevolume.isChecked())},\n'
        f'		"BeatScale": {widget.audiobeatscale.value()},\n'
        f'		"BeatUseTimingPoints": {booltostr(widget.usingtimingpoints.isChecked())},\n'
        '		"Linux/Unix": {\n'
        '			"BassPlaybackBufferLength": 100,\n'
        '			"BassDeviceBufferLength": 10,\n'
        '			"BassUpdatePeriod": 5\n'
        '		}\n'
        '	},\n'
        '	"Input": {\n'
        f'		"LeftKey": "{widget.zkey.keySequence().toString()}",\n'
        f'		"RightKey": "{widget.xkey.keySequence().toString()}",\n'
        f'		"RestartKey": "{widget.rkey.keySequence().toString()}",\n'
        f'		"SmokeKey": "{widget.ckey.keySequence().toString()}",\n'
        f'		"MouseButtonsDisabled": {booltostr(widget.mouse.isChecked())},\n'
        f'		"MouseHighPrecision": {booltostr(widget.mousehighprecision.isChecked())},\n'
        f'		"MouseSensitivity": {widget.mousesensivity.value()}\n'
        '	},\n'
        '	"Gameplay": {\n'
        '		"HitErrorMeter": {\n'
        f'			"Show": {booltostr(widget.hiterrormeter.isChecked())},\n'
        f'			"Scale": {widget.hiterrormeterscale.value()},\n'
        f'			"Opacity": {widget.hiterrormeteropacity.value()},\n'
        '			"ShowUnstableRate": true,\n'
        '			"UnstableRateDecimals": 0,\n'
        '			"UnstableRateScale": 1\n'
        '		},\n'
        '		"Score": {\n'
        f'			"Show": {booltostr(widget.score.isChecked())},\n'
        f'			"Scale": {widget.scorescale.value()},\n'
        f'			"Opacity": {widget.scoreopacity.value()},\n'
        '			"ProgressBar": "Pie",\n'
        '			"ShowGradeAlways": true\n'
        '		},\n'
        '		"HpBar": {\n'
        f'			"Show": {booltostr(widget.hpbar.isChecked())},\n'
        f'			"Scale": {widget.hpbarscale.value()},\n'
        f'			"Opacity": {widget.hpbaropacity.value()}\n'
        '		},\n'
        '		"ComboCounter": {\n'
        f'			"Show": {booltostr(widget.combocounter.isChecked())},\n'
        f'			"Scale": {widget.combocounterscale.value()},\n'
        f'			"Opacity": {widget.combocounteropacity.value()}\n'
        '		},\n'
        '		"PPCounter": {\n'
        f'			"Show": {booltostr(widget.ppcounter.isChecked())},\n'
        f'			"Scale": {widget.ppcounterscale.value()},\n'
        f'			"Opacity": {widget.ppcounteropacity.value()},\n'
        '			"XPosition": 5,\n'
        '			"YPosition": 150,\n'
        '			"Decimals": 0,\n'
        '			"Align": "CentreLeft",\n'
        '			"ShowInResults": true\n'
        '		},\n'
        '		"KeyOverlay": {\n'
        f'			"Show": {booltostr(widget.keyoverlay.isChecked())},\n'
        f'			"Scale": {widget.keyoverlayscale.value()},\n'
        f'			"Opacity": {widget.keyoverlayopacity.value()}\n'
        '		},\n'
        '		"ScoreBoard": {\n'
        f'			"Show": {booltostr(widget.scoreboard.isChecked())},\n'
        f'			"Scale": {widget.scoreboardscale.value()},\n'
        f'			"Opacity": {widget.scoreboardopacity.value()},\n'
        '			"HideOthers": false,\n'
        '			"ShowAvatars": false,\n'
        '			"YOffset": 0\n'
        '		},\n'
        '		"Mods": {\n'
        f'			"Show": {booltostr(widget.mods.isChecked())},\n'
        f'			"Scale": {widget.modsscale.value()},\n'
        f'			"Opacity": {widget.modsopacity.value()},\n'
        '			"HideInReplays": false,\n'
        '			"FoldInReplays": false\n'
        '		},\n'
        '		"Boundaries": {\n'
        f'			"Enabled": {booltostr(widget.boundaries.isChecked())},\n'
        '			"BorderThickness": 1,\n'
        '			"BorderFill": 1,\n'
        '			"BorderColor": {\n'
        '				"Hue": 0,\n'
        '				"Saturation": 0,\n'
        '				"Value": 1\n'
        '			},\n'
        '			"BorderOpacity": 1,\n'
        '			"BackgroundColor": {\n'
        '				"Hue": 0,\n'
        '				"Saturation": 1,\n'
        '				"Value": 0\n'
        '			},\n'
        '			"BackgroundOpacity": 0.5\n'
        '		},\n'
        f'		"ShowResultsScreen": {booltostr(widget.resultscreen.isChecked())},\n'
        f'		"ResultsScreenTime": {widget.resultscreentime.value()},\n'
        f'		"ShowWarningArrows": {booltostr(widget.warningerrors.isChecked())},\n'
        f'		"FlashlightDim": {widget.flashhlightdim.value()},\n'
        f'	    "PlayUsername": "{widget.playername.text()}"\n'
        '	},\n'
        '	"Skin": {\n'
        f'		"CurrentSkin": "{widget.skin.text()}",\n'
        f'		"UseColorsFromSkin": {booltostr(widget.colorsfromskin.isChecked())},\n'
        f'		"UseBeatmapColors": {booltostr(widget.beatmapcolors.isChecked())},\n'
        '		"Cursor": {\n'
        f'			"UseSkinCursor": {booltostr(widget.skincursor.isChecked())},\n'
        f'			"Scale": {widget.cursorscale.value()},\n'
        '			"ForceLongTrail": false,\n'
        '			"LongTrailLength": 2048,\n'
        '			"LongTrailDensity": 1\n'
        '		}\n'
        '	},\n'
        '	"Cursor": {\n'
        '		"TrailStyle": 1,\n'
        '		"Style23Speed": 0.18,\n'
        '		"Style4Shift": 0.5,\n'
        '		"Colors": {\n'
        '			"EnableRainbow": true,\n'
        '			"RainbowSpeed": 8,\n'
        '			"BaseColor": {\n'
        '				"Hue": 0,\n'
        '				"Saturation": 1,\n'
        '				"Value": 1\n'
        '			},\n'
        '			"EnableCustomHueOffset": false,\n'
        '			"HueOffset": 0,\n'
        '			"FlashToTheBeat": false,\n'
        '			"FlashAmplitude": 0\n'
        '		},\n'
        '		"EnableCustomTagColorOffset": true,\n'
        '		"TagColorOffset": -36,\n'
        '		"EnableTrailGlow": true,\n'
        '		"EnableCustomTrailGlowOffset": true,\n'
        '		"TrailGlowOffset": -36,\n'
        '		"ScaleToCS": false,\n'
        '		"CursorSize": 18,\n'
        '		"CursorExpand": false,\n'
        '		"ScaleToTheBeat": true,\n'
        '		"ShowCursorsOnBreaks": true,\n'
        '		"BounceOnEdges": true,\n'
        '		"TrailScale": 1,\n'
        '		"TrailEndScale": 0.4,\n'
        '		"TrailDensity": 0.5,\n'
        '		"TrailMaxLength": 2000,\n'
        '		"TrailRemoveSpeed": 1,\n'
        '		"GlowEndScale": 0.4,\n'
        '		"InnerLengthMult": 0.9,\n'
        '		"AdditiveBlending": true,\n'
        '		"CursorRipples": true,\n'
        '		"SmokeEnabled": true\n'
        '	},\n'
        '	"Objects": {\n'
        '		"DrawApproachCircles": true,\n'
        '		"DrawComboNumbers": true,\n'
        '		"DrawFollowPoints": true,\n'
        '		"LoadSpinners": true,\n'
        '		"ScaleToTheBeat": false,\n'
        '		"StackEnabled": true,\n'
        '		"Sliders": {\n'
        '			"ForceSliderBallTexture": true,\n'
        '			"DrawEndCircles": true,\n'
        '			"DrawSliderFollowCircle": true,\n'
        '			"DrawScorePoints": true,\n'
        '			"SliderMerge": false,\n'
        '			"SliderDistortions": true,\n'
        '			"BorderWidth": 1,\n'
        '			"Quality": {\n'
        '				"CircleLevelOfDetail": 50,\n'
        '				"PathLevelOfDetail": 50\n'
        '			},\n'
        '			"Snaking": {\n'
        '				"In": true,\n'
        '				"Out": true,\n'
        '				"DurationMultiplier": 0,\n'
        '				"FadeMultiplier": 0\n'
        '			}\n'
        '		},\n'
        '		"Colors": {\n'
        '			"MandalaTexturesTrigger": 5,\n'
        '			"MandalaTexturesAlpha": 0.3,\n'
        '			"Color": {\n'
        '				"EnableRainbow": true,\n'
        '				"RainbowSpeed": 8,\n'
        '				"BaseColor": {\n'
        '					"Hue": 0,\n'
        '					"Saturation": 1,\n'
        '					"Value": 1\n'
        '				},\n'
        '				"EnableCustomHueOffset": false,\n'
        '				"HueOffset": 0,\n'
        '				"FlashToTheBeat": false,\n'
        '				"FlashAmplitude": 100\n'
        '			},\n'
        '			"UseComboColors": false,\n'
        '			"ComboColors": [\n'
        '				{\n'
        '					"Hue": 0,\n'
        '					"Saturation": 1,\n'
        '					"Value": 1\n'
        '				}\n'
        '			],\n'
        '			"UseSkinComboColors": false,\n'
        '			"UseBeatmapComboColors": false,\n'
        '			"Sliders": {\n'
        '				"WhiteScorePoints": true,\n'
        '				"ScorePointColorOffset": 0,\n'
        '				"SliderBallTint": false,\n'
        '				"Border": {\n'
        '					"UseHitCircleColor": false,\n'
        '					"Color": {\n'
        '						"EnableRainbow": false,\n'
        '						"RainbowSpeed": 8,\n'
        '						"BaseColor": {\n'
        '							"Hue": 0,\n'
        '							"Saturation": 0,\n'
        '							"Value": 1\n'
        '						},\n'
        '						"EnableCustomHueOffset": false,\n'
        '						"HueOffset": 0,\n'
        '						"FlashToTheBeat": false,\n'
        '						"FlashAmplitude": 100\n'
        '					},\n'
        '					"EnableCustomGradientOffset": true,\n'
        '					"CustomGradientOffset": 0\n'
        '				},\n'
        '				"Body": {\n'
        '					"UseHitCircleColor": true,\n'
        '					"Color": {\n'
        '						"EnableRainbow": false,\n'
        '						"RainbowSpeed": 8,\n'
        '						"BaseColor": {\n'
        '							"Hue": 0,\n'
        '							"Saturation": 1,\n'
        '							"Value": 0\n'
        '						},\n'
        '						"EnableCustomHueOffset": false,\n'
        '						"HueOffset": 0,\n'
        '						"FlashToTheBeat": true,\n'
        '						"FlashAmplitude": 100\n'
        '					},\n'
        '					"InnerOffset": -0.5,\n'
        '					"OuterOffset": -0.05,\n'
        '					"InnerAlpha": 0.8,\n'
        '					"OuterAlpha": 0.8\n'
        '				}\n'
        '			}\n'
        '		}\n'
        '	},\n'
        '	"Playfield": {\n'
        '		"DrawObjects": true,\n'
        '		"DrawCursors": true,\n'
        '		"Scale": 1,\n'
        '		"OsuShift": true,\n'
        '		"ShiftY": 0,\n'
        '		"ShiftX": 0,\n'
        '		"ScaleStoryboardWithPlayfield": true,\n'
        '		"LeadInTime": 5,\n'
        '		"LeadInHold": 2,\n'
        '		"FadeOutTime": 5,\n'
        '		"SeizureWarning": {\n'
        '			"Enabled": true,\n'
        '			"Duration": 5\n'
        '		},\n'
        '		"Background": {\n'
        f'			"LoadStoryboards": {booltostr(widget.loadstoryboards.isChecked())},\n'
        f'			"LoadVideos": {booltostr(widget.loadvideos.isChecked())},\n'
        f'			"FlashToTheBeat": {booltostr(widget.flashtobeat.isChecked())},\n'
        '			"Dim": {\n'
        f'				"Intro": {widget.dimintro.value()},\n'
        f'				"Normal": {widget.dimnormal.value()},\n'
        f'				"Breaks": {widget.dimbreaks.value()}\n'
        '			},\n'
        '			"Parallax": {\n'
        f'				"Amount": {widget.paralaxamount.value()},\n'
        f'				"Speed": {widget.paralaxspeed.value()}\n'
        '			},\n'
        '			"Blur": {\n'
        f'				"Enabled": {booltostr(widget.blur.isChecked())},\n'
        '				"Values": {\n'
        f'					"Intro": {widget.blurintro.value()},\n'
        f'					"Normal": {widget.blurnormal.value()},\n'
        f'					"Breaks": {widget.blurbreaks.value()}\n'
        '				}\n'
        '			},\n'
        '			"Triangles": {\n'
        f'				"Enabled": {booltostr(widget.triangles.isChecked())},\n'
        f'				"Shadowed": {booltostr(widget.trianglesshadow.isChecked())},\n'
        f'				"DrawOverBlur": {booltostr(widget.trianglesdrawoverblur.isChecked())},\n'
        f'				"ParallaxMultiplier": {widget.trianglesparalaxmultiplier.value()},\n'
        f'				"Density": {widget.trianglesdensity.value()},\n'
        f'				"Scale": {widget.trianglesscale.value()},\n'
        f'				"Speed": {widget.trianglesspeed.value()}\n'
        '			}\n'
        '		},\n'
        '		"Logo": {\n'
        f'			"DrawSpectrum": {booltostr(widget.drawspectrum.isChecked())},\n'
        '			"Dim": {\n'
        f'				"Intro": {widget.drawspectrumintro.value()},\n'
        f'				"Normal": {widget.drawspectrumnormal.value()},\n'
        f'				"Breaks": {widget.drawspectrumbreaks.value()}\n'
        '			}\n'
        '		},\n'
        '		"Bloom": {\n'
        f'			"Enabled": {booltostr(widget.bloom.isChecked())},\n'
        f'			"BloomToTheBeat": {booltostr(widget.bloomtobeat.isChecked())},\n'
        f'			"BloomBeatAddition": {widget.bloomtobeatadd.value()},\n'
        f'			"Threshold": {widget.bloomthreshold.value()},\n'
        f'			"Blur": {widget.bloomblur.value()},\n'
        f'			"Power": {widget.bloompower.value()}\n'
        '		}\n'
        '	},\n'
        '	"Dance": {\n'
        '		"Movers": [\n'
        '		"spline"\n'
        '		],\n'
        '		"Spinners": [\n'
        '		"circle"\n'
        '		],\n'
        '		"DoSpinnersTogether": true,\n'
        '		"SpinnerRadius": 100,\n'
        '		"Battle": false,\n'
        '		"SliderDance": false,\n'
        '		"RandomSliderDance": false,\n'
        '		"TAGSliderDance": true,\n'
        '		"Bezier": {\n'
        '			"Aggressiveness": 60,\n'
        '			"SliderAggressiveness": 3\n'
        '		},\n'
        '		"Flower": {\n'
        '			"AngleOffset": 90,\n'
        '			"DistanceMult": 0.666,\n'
        '			"StreamAngleOffset": 90,\n'
        '			"LongJump": -1,\n'
        '			"LongJumpMult": 0.7,\n'
        '			"LongJumpOnEqualPos": false\n'
        '		},\n'
        '		"HalfCircle": {\n'
        '			"RadiusMultiplier": 1,\n'
        '			"StreamTrigger": 130\n'
        '		},\n'
        '		"Spline": {\n'
        '			"RotationalForce": false,\n'
        '			"StreamHalfCircle": true,\n'
        '			"StreamWobble": true,\n'
        '			"WobbleScale": 0.67\n'
        '		},\n'
        '		"Momentum": {\n'
        '			"SkipStackAngles": false,\n'
        '			"StreamRestrict": true,\n'
        '			"DurationMult": 2,\n'
        '			"DurationTrigger": 500,\n'
        '			"StreamMult": 0.7,\n'
        '			"RestrictAngle": 90,\n'
        '			"RestrictArea": 40,\n'
        '			"RestrictInvert": true,\n'
        '			"DistanceMult": 0.6,\n'
        '			"DistanceMultOut": 0.45\n'
        '		},\n'
        '		"ExGon": {\n'
        '			"Delay": 50\n'
        '		}\n'
        '	},\n'
        '	"Knockout": {\n'
        '		"Mode": 0,\n'
        '		"ExcludeMods": "",\n'
        '		"HideMods": "",\n'
        '		"MaxPlayers": 50,\n'
        '		"BubbleMinimumCombo": 200,\n'
        '		"RevivePlayersAtEnd": true,\n'
        '		"LiveSort": false,\n'
        '		"SortBy": "Score",\n'
        '		"MinCursorSize": 3,\n'
        '		"MaxCursorSize": 7,\n'
        '		"AddDanser": true,\n'
        '	"DanserName": "danser"\n'
        '	},\n'
        '	"Recording": {\n'
        '		"FrameWidth": 1920,\n'
        '		"FrameHeight": 1080,\n'
        '		"FPS": 60,\n'
        '		"Encoder": "libx264",\n'
        '		"EncoderOptions": "-crf 14",\n'
        '		"Profile": "high",\n'
        '		"Preset": "faster",\n'
        '		"PixelFormat": "yuv420p",\n'
        '		"Filters": "",\n'
        '		"AudioCodec": "aac",\n'
        '		"AudioBitrate": "320k",\n'
        '		"AudioFilters": "",\n'
        '		"OutputDir": "F:\\\\Desktop\\\\dancer",\n'
        '		"Container": "mp4",\n'
        '		"MotionBlur": {\n'
        '			"Enabled": false,\n'
        '			"OversampleMultiplier": 3,\n'
        '			"BlendFrames": 5,\n'
        '			"BlendWeights": {\n'
        '				"UseManualWeights": false,\n'
        '				"ManualWeights": "1 1.7 2.1 4.1 5",\n'
        '				"AutoWeightsID": 1,\n'
        '				"GaussWeightsMult": 1.5\n'
        '			}\n'
        '		}\n'
        '	}\n'
        '}')
    f.close()


def play():
    global load
    system(f"danser.exe {widget.lineEdit.text()}")


def modss():
    if widget.ht.isChecked() or widget.hdfi.isChecked() or widget.ezhr.isChecked() or widget.nf.isChecked() or \
            widget.sdpf.isChecked() or widget.dtnc.isChecked() or widget.fl.isChecked():
        return True
    else:
        return False


def text():
    global load
    load = ""
    knockout = ""
    mods = ""
    start = ""
    end = ""
    author, creator, title, difficulty = "", "", "", ""
    if widget.author.isChecked():
        author = "-a=\"" + widget.authorc.text() + "\""
    if widget.creator.isChecked():
        creator = "-c=\"" + widget.creatorc.text() + "\""
    if widget.title.isChecked():
        title = "-t=\"" + widget.titlec.text() + "\""
    if widget.difficulty.isChecked():
        difficulty = "-d=\"" + widget.difficultyc.text() + "\""
    level = f"{author} {creator} {title} {difficulty}"

    if widget.knockout.isChecked():  # knockout mods
        knockout = "-knockout"
        if modss():
            mods = "-mods="
            if widget.ht.isChecked():
                mods = mods + "HT"
            if widget.nf.isChecked():
                mods = mods + "NF"
            if widget.fl.isChecked():
                mods = mods + "FL"

            if widget.hdfi.checkState() == Qt.CheckState.PartiallyChecked:
                mods = mods + "HD"
            elif widget.hdfi.checkState() == Qt.CheckState.Checked:
                mods = mods + "FI"
            if widget.dtnc.checkState() == Qt.CheckState.PartiallyChecked:
                mods = mods + "DT"
            elif widget.dtnc.checkState() == Qt.CheckState.Checked:
                mods = mods + "NC"
            if widget.sdpf.checkState() == Qt.CheckState.PartiallyChecked:
                mods = mods + "SD"
            elif widget.sdpf.checkState() == Qt.CheckState.Checked:
                mods = mods + "PF"
            if widget.ezhr.checkState() == Qt.CheckState.PartiallyChecked:
                mods = mods + "EZ"
            elif widget.ezhr.checkState() == Qt.CheckState.Checked:
                mods = mods + "HR"

    load = f"{knockout} {mods} {start} {end} {level}"
    if widget.start.isChecked():
        load += f"-start={widget.starts.value()}"
    if widget.end.isChecked():
        load += f"-end={widget.ends.value()}"

    if widget.skip.isChecked():
        load += " -skip"
    if widget.qstart.isChecked():
        load += " -quickstart"
    widget.lineEdit.setText(load)
    # widget.


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


test()
# code
# buttons
widget.exit.clicked.connect(bp)
widget.coinfirm.clicked.connect(configure)
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

widget.author.clicked.connect(text)
widget.difficulty.clicked.connect(text)
widget.title.clicked.connect(text)
widget.creator.clicked.connect(text)

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
