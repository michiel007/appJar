import sys
sys.path.append("../../")
from appJar import gui

redWords = ("string", "integer", "boolean", "real")
greenWords = ("print", "input")

def highlightSyntax(param):
    for w in redWords:
        app.tagTextAreaPattern("ta", "red", w)

    for w in greenWords:
        app.tagTextAreaPattern("ta", "green", w)

    app.tagTextAreaRange("ta", "red", 1.0, 1.4)

with gui("Text Editor", "300x400") as app:
    app.text("ta", focus=True, change=highlightSyntax)
    app.tagTextArea("ta", "red", background="red", foreground="white")
    app.tagTextArea("ta", "green", background="green", foreground="white")
