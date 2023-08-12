import speech_recognition as sr
import pyttsx3
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "alarm_system"

def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    """Captures voice input and returns the recognized text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, I am unable to access the speech recognition service. Please try again later.")
        return ""

def set_timer():
    """Allows the user to set a timer using voice input."""
    speak("Please tell me the duration for the timer in seconds.")
    timer_duration = get_voice_input()

    try:
        timer_duration = int(timer_duration)
        speak(f"Timer set for {timer_duration} seconds.")

        return timer_duration
    except ValueError:
        speak("Invalid duration format. Please try again.")
        return set_timer()

def countdown_timer(duration):
    """Displays the timer countdown on the console and sends the timer value to MQTT topic."""
    mqtt_client = mqtt.Client()
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT)

    for seconds in range(duration, -1, -1):
        timer_str = f"Timer- {seconds // 60:02d}:{seconds % 60:02d}"
        print(timer_str, end='\r')  # Use '\r' to overwrite the previous line in the console
        mqtt_client.publish(MQTT_TOPIC, timer_str)  # Publish timer value to MQTT topic
        time.sleep(1)

    print("Timer ended")
    mqtt_client.publish(MQTT_TOPIC, "Timer ended")  # Publish timer ended message to MQTT topic
    mqtt_client.disconnect()

def main():
    speak("Welcome to the Timer function using voice input.")
    timer_duration = set_timer()

    if timer_duration is not None:
        countdown_timer(timer_duration)

if __name__ == "__main__":
    main()
