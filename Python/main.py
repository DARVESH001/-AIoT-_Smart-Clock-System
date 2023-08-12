import pyttsx3
import speech_recognition as sr
import importlib

# Dictionary of recognized commands and their corresponding module names
COMMANDS = {
    "set timer": "timer",
    "start current time": "current_time",
    "set stopwatch": "stopwatch",
    "set reminder": "reminder",
    "set alarm": "alarm",
    "start world clock": "world_clock",
    "turn off": "exit"  # Changed from "turn off"
}

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to get voice input from the user
def get_voice_input():
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

# Function to extract the command from user input
def extract_command(user_input):
    for command in COMMANDS:
        if user_input.startswith(f"clock {command}"):
            return command
    return None

# Function to execute the appropriate module based on the command
def execute_module(command):
    if command == "exit":
        speak("Turning off the system. Goodbye!")
        return False
    elif command in COMMANDS:
        module_name = COMMANDS[command]
        try:
            module = importlib.import_module(module_name)
            module.main()  # Execute the module once
            del module  # Remove the reference to the module
        except ImportError:
            speak("Command module not found. Please try again.")
    else:
        speak("Command not recognized. Please try again.")
    return True

# Main function that listens for user input and executes commands
def main():
    speak("Welcome to the Smart Clock System. You can wake me up by saying 'clock', followed by your command.")
    speak('"there are some command like set alarm,'
          ' set reminder,'
          ' set timer,'
          ' set stopwatch,'
          ' start current time,'
          ' start world clock,'
          ' turn off to close the smart clock system"')

    while True:
        user_input = get_voice_input()

        if "clock" in user_input:
            command = extract_command(user_input)
            if command:
                if not execute_module(command):
                    break
        elif "turn off" in user_input:
            speak("Turning off the clock system. Goodbye!")
            break

if __name__ == "__main__":
    main()
