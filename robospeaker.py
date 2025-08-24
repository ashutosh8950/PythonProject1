import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to RoboSpeaker (type 'q' to quit)")
    while True:
        x = input("Enter what you want to speak: ")
        if x.lower() == "q":
            print("Goodbye! Program ended.")
            break
        t = threading.Thread(target=speak, args=(x,))
        t.start()
