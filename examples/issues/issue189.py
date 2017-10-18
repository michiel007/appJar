import sys
sys.path.append("../../")

from appJar import gui
app = gui("ttk demo")
with app.labelFrame("LabelFrame"):
    app.addLabel("l1", "Simple Label")
    app.addCheckBox("Tick me")
    app.addRadioButton("tb", "Tick me")
    app.addTextArea("t1")
    app.addButton("Press Me", None)
    app.addScale("Scale")
    app.addEntry("Entry")
app.go()

