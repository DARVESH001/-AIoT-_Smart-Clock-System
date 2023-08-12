import pyttsx3
import speech_recognition as sr
import time
import paho.mqtt.client as mqtt

# Your MQTT broker settings
MQTT_BROKER_HOST = "broker.emqx.io"  # Replace with your MQTT broker's hostname or IP
MQTT_BROKER_PORT = 1883  # Default MQTT port
MQTT_TOPIC = "alarm_system"  # MQTT topic to publish current time

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

def tell_time():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    period = "AM" if hour < 12 else "PM"
    hour %= 12
    if hour == 0:
        hour = 12
    time_str = f"current time-{hour}:{minute:02d} {period}."
    return time_str

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code", rc)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

    speak("Welcome! You can ask me 'What's the time?' to know the current time.")

    user_input = get_voice_input()

    if "what's the time" in user_input:
        time_str = tell_time()
        print(time_str)
        speak(time_str)
        client.publish(MQTT_TOPIC, time_str)

    #speak("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
