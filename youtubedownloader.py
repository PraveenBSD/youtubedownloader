from appJar import gui
import pytube

app=gui()
app.setBg("skyBlue")
app.addLabel("title","YOUTUBE DOWNLOADER")
app.setLabelBg("title","red")
app.setFg("white")



app.addLabelEntry("Link")



def press(button):
    if button == "Cancel":
        app.stop()
    else:
        link = app.getEntry("Link")
        yt = pytube.YouTube(link)
        videos = yt.get_videos()

        def num(button):
            if(button == "Next"):
                rb="song"
                x = app.getRadioButton(rb)
                n=int(x[0])
                vid=videos[n-1]
                dest=app.directoryBox(title=None, dirName=None)

                vid.download(dest)
                app.bell()
                app.infoBox("Success", "successfully downloaded")
        s = 1
        app.setFg("black")
        app.startLabelFrame("Video Quality")
        for v in videos:
            v=str(v)
            v=v.replace("<Video:","")
            v=v.replace(">","")
            app.addRadioButton("song",str(s)+v)
            s+=1
        app.stopLabelFrame()

        #app.addLabelEntry("enter the number")
        app.addButton("Next",num)


app.addButtons(["Cancel","Submit"],press)
app.enableEnter(press)
app.go()