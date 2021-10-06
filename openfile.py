import json
from config import openfile

name = ''
g = {}


def new(n: str, p):
    global g, name
    name = n
    g = p[name]


def openf(widget):
    global g, name
    i = json.loads(open(openfile, "r").read())

    p = i["General"]
    widget.songs.setText(str(p["OsuSongsDir"]).replace("\\", "\\\\"))
    widget.skins.setText(str(p["OsuSkinsDir"]).replace("\\", "\\\\"))

    p = i["Graphics"]
    widget.width.setValue(p["Width"])
    widget.height.setValue(p["Height"])
    widget.winwidth.setValue(p["WindowWidth"])
    widget.winheight.setValue(p["WindowHeight"])
    widget.fullscreenbutton.setChecked(p["Fullscreen"])
    widget.vsync.setChecked(p["VSync"])
    widget.fpscap.setValue(p["FPSCap"])
    widget.msaa.setValue(p["MSAA"])
    widget.showfps.setChecked(p["ShowFPS"])
    widget.usepersistentbuffers.setChecked(p["Experimental"]["UsePersistentBuffers"])

    p = i["Audio"]
    widget.generalvolume.setValue(p["GeneralVolume"])
    widget.musicvolume.setValue(p["MusicVolume"])
    widget.samplevolume.setValue(p["SampleVolume"])
    widget.offset.setValue(p["Offset"])
    widget.positionmultiplier.setValue(p["HitsoundPositionMultiplier"])
    widget.ignoresamples.setChecked(p["IgnoreBeatmapSamples"])
    widget.ignoresamplevolume.setChecked(p["IgnoreBeatmapSampleVolume"])
    widget.audiobeatscale.setValue(p["BeatScale"])
    widget.usingtimingpoints.setChecked(p["BeatUseTimingPoints"])

    p = i["Input"]
    widget.zkey.setKeySequence(p["LeftKey"])
    widget.xkey.setKeySequence(p["RightKey"])
    widget.rkey.setKeySequence(p["RestartKey"])
    widget.ckey.setKeySequence(p["SmokeKey"])
    widget.mouse.setChecked(p["MouseButtonsDisabled"])
    widget.mousehighprecision.setChecked(p["MouseHighPrecision"])
    widget.mousesensivity.setValue(p["MouseSensitivity"])

    p = i["Gameplay"]

    widget.resultscreen.setChecked(p["ShowResultsScreen"])
    widget.resultscreentime.setValue(p["ResultsScreenTime"])
    widget.warningerrors.setChecked(p["ShowWarningArrows"])
    widget.flashlightdim.setValue(p["FlashlightDim"])
    widget.playername.setText(p["PlayUsername"])

    new("HitErrorMeter", p)
    widget.hiterrormeter.setChecked(g["Show"])
    widget.hiterrormeterscale.setValue(g["Scale"])
    widget.hiterrormeteropacity.setValue(g["Opacity"])

    new("AimErrorMeter", p)
    widget.aem.setChecked(g["Show"])
    widget.aemscale.setValue(g["Scale"])
    widget.aemopacity.setValue(g["Opacity"])
    widget.aemalign.setCurrentIndex(widget.aemalign.findText(g["Align"]))
    widget.aemxpos.setValue(g["XPosition"])
    widget.aemypos.setValue(g["YPosition"])

    new("Score", p)
    widget.score.setChecked(g["Show"])
    widget.scorescale.setValue(g["Scale"])
    widget.scoreopacity.setValue(g["Opacity"])

    new("HpBar", p)
    widget.hpbar.setChecked(g["Show"])
    widget.hpbarscale.setValue(g["Scale"])
    widget.hpbaropacity.setValue(g["Opacity"])

    new("ComboCounter", p)
    widget.combocounter.setChecked(g["Show"])
    widget.combocounterscale.setValue(g["Scale"])
    widget.combocounteropacity.setValue(g["Opacity"])

    new("PPCounter", p)
    widget.ppcounter.setChecked(g["Show"])
    widget.ppcounterscale.setValue(g["Scale"])
    widget.ppcounteropacity.setValue(g["Opacity"])
    widget.ppxpos.setValue(g["XPosition"])
    widget.ppypos.setValue(g["YPosition"])
    widget.ppalign.setCurrentIndex(widget.ppalign.findText(g["Align"]))

    new("HitCounter", p)
    widget.hitcounter.setChecked(g["Show"])
    widget.hcscale.setValue(g["Scale"])
    widget.hcopacity.setValue(g["Opacity"])
    widget.hcxpos.setValue(g["XPosition"])
    widget.hcypos.setValue(g["YPosition"])
    widget.hcalign.setCurrentIndex(widget.hcalign.findText(g["Align"]))

    new("KeyOverlay", p)
    widget.keyoverlay.setChecked(g["Show"])
    widget.keyoverlayscale.setValue(g["Scale"])
    widget.keyoverlayopacity.setValue(g["Opacity"])

    new("ScoreBoard", p)
    widget.scoreboard.setChecked(g["Show"])
    widget.scoreboardscale.setValue(g["Scale"])
    widget.scoreboardopacity.setValue(g["Opacity"])

    new("Mods", p)
    widget.mods.setChecked(g["Show"])
    widget.modsscale.setValue(g["Scale"])
    widget.modsopacity.setValue(g["Opacity"])

    new("Boundaries", p)
    widget.boundaries.setChecked(g["Enabled"])

    p = i["Skin"]
    widget.skin.setText(p["CurrentSkin"])
    widget.colorsfromskin.setChecked(p["UseColorsFromSkin"])
    widget.beatmapcolors.setChecked(p["UseBeatmapColors"])

    new("Cursor", p)
    widget.skincursor.setChecked(g["UseSkinCursor"])
    widget.cursorscale.setValue(g["Scale"])

    p = i["Cursor"]
    widget.trailstyle.setValue(p["TrailStyle"])
    widget.style23speed.setValue(p["Style23Speed"])

    p = i["Playfield"]
    n = p["Background"]
    widget.loadstoryboards.setChecked(n["LoadStoryboards"])
    widget.loadvideos.setChecked(n["LoadVideos"])
    widget.flashtobeat.setChecked(n["FlashToTheBeat"])

    new("Dim", n)
    widget.dimintro.setValue(g["Intro"])
    widget.dimnormal.setValue(g["Normal"])
    widget.dimbreaks.setValue(g["Breaks"])

    new("Parallax", n)
    widget.paralaxamount.setValue(g["Amount"])
    widget.paralaxspeed.setValue(g["Speed"])

    new("Blur", n)
    widget.blur.setChecked(g["Enabled"])
    widget.blurintro.setValue(g["Values"]["Intro"]),
    widget.blurnormal.setValue(g["Values"]["Normal"]),
    widget.blurbreaks.setValue(g["Values"]["Breaks"])

    new("Triangles", n)
    widget.triangles.setChecked(g["Enabled"])
    widget.trianglesshadow.setChecked(g["Shadowed"])
    widget.trianglesdrawoverblur.setChecked(g["DrawOverBlur"])
    widget.trianglesparalaxmultiplier.setValue(g["ParallaxMultiplier"])
    widget.trianglesdensity.setValue(g["Density"])
    widget.trianglesscale.setValue(g["Scale"])
    widget.trianglesspeed.setValue(g["Speed"])
    p["Background"] = n

    new("Logo", p)
    widget.drawspectrum.setChecked(g["DrawSpectrum"])

    widget.drawspectrumintro.setValue(g["Dim"]["Intro"]),
    widget.drawspectrumnormal.setValue(g["Dim"]["Normal"]),
    widget.drawspectrumbreaks.setValue(g["Dim"]["Breaks"])

    new("Bloom", p)
    widget.bloom.setChecked(g["Enabled"])
    widget.bloomtobeat.setChecked(g["BloomToTheBeat"])
    widget.bloomtobeatadd.setValue(g["BloomBeatAddition"])
    widget.bloomthreshold.setValue(g["Threshold"])
    widget.bloomblur.setValue(g["Blur"])
    widget.bloompower.setValue(g["Power"])
