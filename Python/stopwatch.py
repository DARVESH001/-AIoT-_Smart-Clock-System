import pyttsx3
import speech_recognition as sr
import threading
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "alarm_system"

stopwatch_running = False
start_time = 0
countdown_thread = None


def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def start_stopwatch():
    """Starts the stopwatch."""
    global stopwatch_running, start_time
    stopwatch_running = True
    start_time = time.time()


def stop_stopwatch():
    """Stops the stopwatch."""
    global stopwatch_running
    stopwatch_running = False


def format_time(seconds):
    """Formats the elapsed time in HH:MM:SS format."""
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def stopwatch_timer():
    """Prints the stopwatch timer in the format HH:MM:SS."""
    global stopwatch_running, start_time

    while stopwatch_running:
        elapsed_time = time.time() - start_time
        print(f"\rStopwatch: {format_time(elapsed_time)}", end="")
        send_mqtt_time(format_time(elapsed_time))  # Send the time to MQTT
        time.sleep(1)

def countdown_thread_function(duration):
    """Starts the countdown for the given duration."""
    global stopwatch_running

    while duration > 0 and stopwatch_running:
        time.sleep(1)
        duration -= 1

    stop_stopwatch()

def process_voice_command(command):
    """Processes the voice command."""
    global countdown_thread, stopwatch_running

    if "start" in command:
        if not stopwatch_running:
            start_stopwatch()
            countdown_thread = threading.Thread(target=countdown_thread_function, args=(60,))  # Change the countdown duration as needed (60 seconds here).
            countdown_thread.start()
            threading.Thread(target=stopwatch_timer).start()  # Start the stopwatch timer in a separate thread.

    elif "stop" in command:
        if stopwatch_running:
            print("stopwatch ended!!")
            stop_stopwatch()

    elif "exit" in command:

        print("Exiting the program.")

        if stopwatch_running:
            stop_stopwatch()

        return "exit"  # Return "exit" to indicate program should exit

    return "continue"


def get_voice_command():
    """Captures voice command and returns the recognized text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Sorry, I am unable to access the speech recognition service. Please try again later.")
        return ""

def send_mqtt_time(time_str):
    """Sends the stopwatch time to the MQTT broker."""
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT)
    client.publish(MQTT_TOPIC, time_str)
    client.disconnect()

def main():
    print("Welcome to the Voice Controlled Stopwatch.")
    speak("Welcome to the Voice Controlled Stopwatch.")
    speak("you can say START to start the stopwatch, STOP to stop the stopwatch and EXIT to exit the stopwatch")

    while True:
        command = get_voice_command()

        if command:
            result = process_voice_command(command)
            if result == "exit":
                break

if __name__ == "__main__":
    main()
