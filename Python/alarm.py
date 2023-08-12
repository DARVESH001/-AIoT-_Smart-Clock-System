import time
import pyttsx3
import paho.mqtt.client as mqtt
import speech_recognition as sr

# Your MQTT broker settings
MQTT_BROKER_HOST = "broker.emqx.io"  # Replace with your MQTT broker's hostname or IP
MQTT_BROKER_PORT = 1883  # Default MQTT port
MQTT_TOPIC = "alarm_system"  # MQTT topic to publish alarm commands


def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def recognize_time_input(prompt):
    recognizer = sr.Recognizer()

    while True:
        try:
            speak(prompt)
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
            time_input = recognizer.recognize_google(audio).lower()

            value = parse_hour_minute(time_input)
            if value is not None:
                return value
            else:
                speak("Invalid time input. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError:
            speak("Sorry, I am unable to access the speech recognition service. Please try again later.")
        except ValueError:
            speak("Invalid input. Please provide a valid number.")


def parse_hour_minute(time_input):
    try:
        value = int(time_input)
        if 0 <= value <= 59:
            return value
    except ValueError:
        pass
    return None


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code", rc)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

    speak("Welcome to the Alarm System. Set time for the alarm.")

    while True:
        alarm_hour = recognize_time_input("Please say the alarm hour.")
        alarm_minute = recognize_time_input("Please say the alarm minute.")

        current_time = time.localtime()
        alarm_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, alarm_hour,
                                       alarm_minute, 0, current_time.tm_wday, current_time.tm_yday,
                                       current_time.tm_isdst))
        alarm_timestamp = time.mktime(alarm_time)

        now = time.mktime(current_time)
        wait_time = alarm_timestamp - now

        if wait_time <= 0:
            speak("Alarm time is in the past. Please set a future time.")
        else:
            alarm_time_str = f"Alarm time: {alarm_hour:02d}:{alarm_minute:02d}"
            print(alarm_time_str)
            client.publish(MQTT_TOPIC, alarm_time_str)

            time.sleep(wait_time)

            alarm_alert_message = "ALARM ALERT !!"
            client.publish(MQTT_TOPIC, alarm_alert_message)

            speak("Wake up! The alarm is ringing.")
            break  # Exit the loop after setting the alarm


if __name__ == "__main__":
    main()
