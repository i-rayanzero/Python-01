import pyttsx3

text = input()

while(text != "exit"):
    pyttsx3.speak(text)
    text = input()
