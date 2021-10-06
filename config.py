import json

name = ''
g = {}
openfile = "settings/default.json"


def new(n: str, p):
    global g, name
    name = n
    g = p[name]


def close(p):
    global name
    p[name] = g


def file(widget):
    global g, name
    i = json.loads(open(openfile, "r").read())

    p = i["General"]
    p["OsuSongsDir"] = widget.songs.text()
    p["OsuSkinsDir"] = widget.skins.text()
    i["General"] = p

    p = i["Graphics"]
    p["Width"] = widget.width.value()
    p["Height"] = widget.height.value()
    p["WindowWidth"] = widget.winwidth.value()
    p["WindowHeight"] = widget.winheight.value()
    p["Fullscreen"] = widget.fullscreenbutton.isChecked()
    p["VSync"] = widget.vsync.isChecked()
    p["FPSCap"] = widget.fpscap.value()
    p["MSAA"] = widget.msaa.value()
    p["ShowFPS"] = widget.showfps.isChecked()
    p["Experimental"]["UsePersistentBuffers"] = widget.usepersistentbuffers.isChecked()
    i["Graphics"] = p

    p = i["Audio"]
    p["GeneralVolume"] = widget.generalvolume.value()
    p["MusicVolume"] = widget.musicvolume.value()
    p["SampleVolume"] = widget.samplevolume.value()
    p["Offset"] = widget.offset.value()
    p["HitsoundPositionMultiplier"] = widget.positionmultiplier.value()
    p["IgnoreBeatmapSamples"] = widget.ignoresamples.isChecked()
    p["IgnoreBeatmapSampleVolume"] = widget.ignoresamplevolume.isChecked()
    p["BeatScale"] = widget.audiobeatscale.value()
    p["BeatUseTimingPoints"] = widget.usingtimingpoints.isChecked()
    i["Audio"] = p

    p = i["Input"]
    p["LeftKey"] = widget.zkey.keySequence().toString()
    p["RightKey"] = widget.xkey.keySequence().toString()
    p["RestartKey"] = widget.rkey.keySequence().toString()
    p["SmokeKey"] = widget.ckey.keySequence().toString()
    p["MouseButtonsDisabled"] = widget.mouse.isChecked()
    p["MouseHighPrecision"] = widget.mousehighprecision.isChecked()
    p["MouseSensitivity"] = widget.mousesensivity.value()
    i["Input"] = p

    p = i["Gameplay"]

    p["ShowResultsScreen"] = widget.resultscreen.isChecked()
    p["ResultsScreenTime"] = widget.resultscreentime.value()
    p["ShowWarningArrows"] = widget.warningerrors.isChecked()
    p["FlashlightDim"] = widget.flashlightdim.value()
    p["PlayUsername"] = widget.playername.text()

    new("HitErrorMeter", p)
    g["Show"] = widget.hiterrormeter.isChecked()
    g["Scale"] = widget.hiterrormeterscale.value()
    g["Opacity"] = widget.hiterrormeteropacity.value()

    close(p)

    new("AimErrorMeter", p)
    g["Show"] = widget.aem.isChecked()
    g["Scale"] = widget.aemscale.value()
    g["Opacity"] = widget.aemopacity.value()
    g["Align"] = widget.aemalign.currentText()
    g["XPosition"] = widget.aemxpos.value()
    g["YPosition"] = widget.aemypos.value()
    close(p)

    new("Score", p)
    g["Show"] = widget.score.isChecked()
    g["Scale"] = widget.scorescale.value()
    g["Opacity"] = widget.scoreopacity.value()
    close(p)

    new("HpBar", p)
    g["Show"] = widget.hpbar.isChecked()
    g["Scale"] = widget.hpbarscale.value()
    g["Opacity"] = widget.hpbaropacity.value()
    close(p)

    new("ComboCounter", p)
    g["Show"] = widget.combocounter.isChecked()
    g["Scale"] = widget.combocounterscale.value()
    g["Opacity"] = widget.combocounteropacity.value()
    close(p)

    new("PPCounter", p)
    g["Show"] = widget.ppcounter.isChecked()
    g["Scale"] = widget.ppcounterscale.value()
    g["Opacity"] = widget.ppcounteropacity.value()
    g["XPosition"] = widget.ppxpos.value()
    g["YPosition"] = widget.ppypos.value()
    g["Align"] = widget.ppalign.currentText()
    close(p)

    new("HitCounter", p)
    g["Show"] = widget.hitcounter.isChecked()
    g["Scale"] = widget.hcscale.value()
    g["Opacity"] = widget.hcopacity.value()
    g["XPosition"] = widget.hcxpos.value()
    g["YPosition"] = widget.hcypos.value()
    g["Align"] = widget.hcalign.currentText()
    close(p)

    new("KeyOverlay", p)
    g["Show"] = widget.keyoverlay.isChecked()
    g["Scale"] = widget.keyoverlayscale.value()
    g["Opacity"] = widget.keyoverlayopacity.value()
    close(p)

    new("ScoreBoard", p)
    g["Show"] = widget.scoreboard.isChecked()
    g["Scale"] = widget.scoreboardscale.value()
    g["Opacity"] = widget.scoreboardopacity.value()
    close(p)

    new("Mods", p)
    g["Show"] = widget.mods.isChecked()
    g["Scale"] = widget.modsscale.value()
    g["Opacity"] = widget.modsopacity.value()
    close(p)

    new("Boundaries", p)
    g["Enabled"] = widget.boundaries.isChecked()
    close(p)

    i["Gameplay"] = p

    p = i["Skin"]
    p["CurrentSkin"] = widget.skin.text()
    p["UseColorsFromSkin"] = widget.colorsfromskin.isChecked()
    p["UseBeatmapColors"] = widget.beatmapcolors.isChecked()
    new("Cursor", p)
    g["UseSkinCursor"] = widget.skincursor.isChecked()
    g["Scale"] = widget.cursorscale.value()
    close(p)
    i["Skin"] = p

    p = i["Cursor"]
    p["TrailStyle"] = widget.trailstyle.value()
    p["Style23Speed"] = widget.style23speed.value()
    i["Cursor"] = p

    p = i["Playfield"]
    n = p["Background"]
    n["LoadStoryboards"] = widget.loadstoryboards.isChecked()
    n["LoadVideos"] = widget.loadvideos.isChecked()
    n["FlashToTheBeat"] = widget.flashtobeat.isChecked()

    new("Dim", n)
    g["Intro"] = widget.dimintro.value()
    g["Normal"] = widget.dimnormal.value()
    g["Breaks"] = widget.dimbreaks.value()
    close(n)

    new("Parallax", n)
    g["Amount"] = widget.paralaxamount.value()
    g["Speed"] = widget.paralaxspeed.value()
    close(n)

    new("Blur", n)
    g["Enabled"] = widget.blur.isChecked()
    g["Values"] = {
        "Intro": widget.blurintro.value(),
        "Normal": widget.blurnormal.value(),
        "Breaks": widget.blurbreaks.value()
    }
    close(n)

    new("Triangles", n)
    g["Enabled"] = widget.triangles.isChecked()
    g["Shadowed"] = widget.trianglesshadow.isChecked()
    g["DrawOverBlur"] = widget.trianglesdrawoverblur.isChecked()
    g["ParallaxMultiplier"] = widget.trianglesparalaxmultiplier.value()
    g["Density"] = widget.trianglesdensity.value()
    g["Scale"] = widget.trianglesscale.value()
    g["Speed"] = widget.trianglesspeed.value()
    close(n)
    p["Background"] = n

    new("Logo", p)
    g["DrawSpectrum"] = widget.drawspectrum.isChecked()
    g["Dim"] = {
        "Intro": widget.drawspectrumintro.value(),
        "Normal": widget.drawspectrumnormal.value(),
        "Breaks": widget.drawspectrumbreaks.value()
    }
    close(p)

    new("Bloom", p)
    g["Enabled"] = widget.bloom.isChecked()
    g["BloomToTheBeat"] = widget.bloomtobeat.isChecked()
    g["BloomBeatAddition"] = widget.bloomtobeatadd.value()
    g["Threshold"] = widget.bloomthreshold.value()
    g["Blur"] = widget.bloomblur.value()
    g["Power"] = widget.bloompower.value()
    close(p)

    i["Playfield"] = p
    with open(openfile, "w") as f:
        i = str(i)
        i = i.replace("'", '"').replace("True", 'true').replace("False", 'false').replace("\\\\\\\\", "\\\\")
        f.write(i)
