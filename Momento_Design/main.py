from text_editor import TextEditor
from history import History
from text_momento import TextMomento



text = TextEditor()
history = History()

text.write("Hello, ")
text.write("World")
text.write(" I am here to test the momento design Pattern")

print(text.getText())

#  Saving the text written 



history.addMomento(text.saveText())

text.write("I am here to test the momento design Pattern")
history.addMomento(text.saveText())
history.getHistory()

print(text.getText())

history.undo()
history.getHistory()

print(text.getText())

text.restore(history.undo())



