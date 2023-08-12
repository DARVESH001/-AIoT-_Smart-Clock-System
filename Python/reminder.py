import time
import speech_recognition as sr
import pyttsx3
import paho.mqtt.client as mqtt


# Your MQTT broker settings
MQTT_BROKER_HOST = "broker.emqx.io"  # Replace with your MQTT broker's hostname or IP
MQTT_BROKER_PORT = 1883  # Default MQTT port
MQTT_TOPIC = "alarm_system"  # MQTT topic to publish reminders

# Function to convert text to speech
def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def recognize_speech(prompt):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(prompt)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).strip()
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return recognize_speech(prompt)
    except sr.RequestError:
        print("Speech recognition service unavailable. Please check your internet connection.")
        return None

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to get reminder text from user
def get_reminder_text():
    speak("Please say your reminder:")
    return recognize_speech("Please say your reminder:")

# Function to get reminder time from user
def get_reminder_time():
    speak("Please say the hour (0-23) for the reminder: ")
    hour = int(recognize_speech("Please say the hour (0-23) for the reminder: "))
    speak("Please say the minute (0-59) for the reminder: ")
    minute = int(recognize_speech("Please say the minute (0-59) for the reminder: "))
    return hour, minute

# Callback function when connecting to MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code", rc)

def main():
    speak("welcome of the reminder system.")
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

    while True:
        reminder_text = get_reminder_text()
        if reminder_text is not None:
            hour, minute = get_reminder_time()
            current_time = time.localtime()
            reminder_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, hour, minute, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
            reminder_timestamp = time.mktime(reminder_time)

            now = time.mktime(current_time)
            wait_time = reminder_timestamp - now
            if wait_time <= 0:
                speak("Reminder time is in the past. Please set a future time.")
            else:
                print(f"Reminder set for: {hour:02d}:{minute:02d}")
                speak(f"Reminder set for: {hour:02d}:{minute:02d}")
                time.sleep(wait_time)
                speak(f"Reminder: {reminder_text}")
                final_reminder = f"Reminder: {reminder_text} - Time: {hour:02d}:{minute:02d}"
                client.publish(MQTT_TOPIC, final_reminder)

        speak("Do you want to set another reminder? (yes/no): ")
        exit_choice = recognize_speech("Do you want to set another reminder? (yes/no): ").lower()
        if exit_choice != "yes":
            break

if __name__ == "__main__":
    main()
