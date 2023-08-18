**[AIoT]Smart Clock System+ Voice-Recognition + TTS**

**TABLE OF CONTENTS:**
1.	INTRODUCTION
2.	HARDWARE USED
3.	SOFTWARE USED
4.	PROGRAMMING LANGUAGES
5.	WORKFLOW
6.	SETTING UP WITH PYTHON
7.	OUTPUT
8.	CONCLUSION

**1.	INTRODUCTION:**

The Smart Clock project is a remarkable embodiment of modern technology, seamlessly integrating voice recognition with a range of indispensable functions to enhance everyday life. This innovative clock not only displays the current time but offers an array of versatile features that elevate its utility. With its vibrant OLED screen, powered by the advanced Wiznet pico connection, the clock provides an intuitive visual interface, ensuring a user-friendly experience.
The clock's voice recognition capabilities make it a truly hands-free device, allowing users to effortlessly set timers, activate the stopwatch, access world clock information, set alarms, and create reminders. Imagine effortlessly starting the stopwatch with a simple command, and watching the precise timing displayed on the crisp OLED screen. Need to stay organized? The clock's reminder function will keep you on track, displaying important alerts right on the screen.
Whether you're a multitasker in need of precise time management or someone who values convenience and efficiency, this Smart Clock is designed for you. Its seamless integration of voice commands and visual display ensures that accessing its functions is a breeze. The clock doesn't just tell time; it becomes a reliable companion, helping you navigate your daily tasks effortlessly while adding a touch of elegance to your living space. Experience the future of timekeeping with our innovative Smart Clock

**2.	HARDWARE USED:**

•	WIZnet-W5300 TOE SHIELD + STM32-F429ZI board
 
•	OLED SCREEN
 
•	JUMPER WIRES
 






•	BREAD BOARD
 
•	USB MICROPHONE
 



**3.	SOFTWARES AND SERVICES USED
**
•	MQTT SERVICE
•	ARDUINO IDE
•	PYCHARM

**4.	PROGRAMMING LANGUAGES**

•	C++
•	PYTHON

MQTT-BROKER:
	MQTT acts as a broker, facilitating communication between Python and Arduino. Python sends values via MQTT to the Arduino. Arduino, configured to receive MQTT messages, and print them to the connected OLED SCREEN accordingly. This enables seamless remote control of the OLED SCREEN using MQTT protocol, bridging Python and Arduino for effective IoT applications.


GOOGLE TEXT TO SPEECH:
	recognized_text = recognizer.recognize_google(audio)
this code snippet utilizes the Google text-to-speech API service through the recognize_google function provided by the SpeechRecognition library in Python. This function sends the recorded audio data to Google's servers for speech recognition processing, and then it returns the recognized text back to your Python program. In this case, the recognize_google function is using the Google Web Speech API to perform the speech-to-text conversion, allowing you to transcribe spoken language into written text.

**5.	WORKFLOW**

The Smart Clock project has a well-defined workflow that begins with a welcome message and operates through a series of voice commands, with the wake-up word "clock." Here's a breakdown of the input function and several key functions:

1. **Input Function**:
   - Upon program start, the Smart Clock welcomes the user with a friendly message, setting the stage for interaction.
   - The user's input is primarily in the form of voice commands, initiated by saying the wake-up word "clock" followed by specific commands.

2. **Set Timer**:
   - Command: "clock set timer."
   - Function: The user can set a timer for a specific duration(in seconds) using this command.
   - Interaction: The Smart Clock responds by asking the user to specify the time for the timer, and the clock starts counting down.

3. **Set Stopwatch**:
   - Command: "clock set stopwatch."
   - Function: The user can initiate a stopwatch using this command, there are three command start, stop,exit.
   - Interaction: The Smart Clock acknowledges the command and starts the stopwatch, displaying the time on the OLED screen.

4. **Set Alarm**:
   - Command: "clock set alarm."
   - Function: The user can set an alarm for a particular time using this command.
   - Interaction: The Smart Clock prompts the user to specify the alarm time, and when the set time is reached, the alarm activates with a notification on the screen.

5. **Set Reminder**:
   - Command: "clock set reminder."
   - Function: The user can create a reminder for a specific event or task.
   - Interaction: The Smart Clock prompts the user to input the reminder details, and at the specified time, it displays the reminder on the screen.

6. **Start World Clock**:
   - Command: "clock start world clock."
   - Function: The user can access the world clock feature to check the time in different time zones.
   - Interaction: The Smart Clock displays the current time for various pre-configured world clock locations on the OLED screen.

7. **Start Current Time**:
   - Command: "clock start current time."
   - Function: The user can request the current local time.
   - Interaction: The Smart Clock displays the current local time on the OLED screen.

8. **Turn Off/Exit**:
   - Command: "turn off."
   - Function: The user can exit the program and turn off the Smart Clock.
   - Interaction: The Smart Clock acknowledges the command and gracefully shuts down the program.

The combination of voice recognition, the OLED screen, and these functions creates a dynamic and user-friendly experience, making the Smart Clock an essential companion for time management and daily organization.








FLOW CHART:
![image](https://github.com/DARVESH001/-AIoT-_Smart-Clock-System/assets/104376273/e9b31577-c4d2-4a0c-970d-9a7b7a050f7f)

 
	





SETTING UP USING PYTHON:
Setting up with MQTT:
import paho.mqtt.client as mqtt
paho.mqtt.client: This library provides a client implementation for MQTT (Message Queuing Telemetry Transport), a lightweight messaging protocol widely used in the Internet of Things (IoT) domain for communication between devices. It allows you to connect to an MQTT broker and publish messages to topics or subscribe to topics to receive messages. It's commonly used for real-time data transmission in IoT applications.
Installation: To install the paho-mqtt library, you can use pip, the Python package manager. Open your terminal or command prompt and run the following command:
 pip install paho-mqtt

Setting Up with Recogniser:
import speech_recognition as sr
This library provides an easy-to-use interface to work with various speech recognition APIs. It allows you to convert spoken language into text and supports multiple speech recognition engines, such as Google Web Speech API, Microsoft Bing Voice Recognition, and more.
Installation: To install the speech_recognition library, you can use pip:
pip install SpeechRecognition

Setting up with TTS:
import pyttsx3
This library is a text-to-speech (TTS) engine that allows you to convert text into speech. It's useful for applications where you want your computer or device to speak out information to the user.
Installation: To install the pyttsx3 library, you can use pip:
pip install pyttsx3

Another two libraries are used here threading, re. “threading” -- Threads are particularly useful when you want to perform tasks simultaneously without blocking the main program's execution. This can improve the responsiveness of your application, especially for I/O-bound tasks.
“re” -- This library is part of Python's standard library and provides support for regular expressions. Regular expressions are a powerful tool for pattern matching and text manipulation. The re library allows you to search, find, and replace specific patterns within strings.

CIRCUIT CONNECTION:
![image](https://github.com/DARVESH001/-AIoT-_Smart-Clock-System/assets/104376273/f3e50c2f-7009-45b8-92ea-380cd13fbe2e)

 


	


CONNECTION DIAGRAM:
![image](https://github.com/DARVESH001/-AIoT-_Smart-Clock-System/assets/104376273/c4f81c39-eed6-4468-b335-059ea073463c)


**OUTPUT:**
video link: https://youtu.be/D0mdfbCk6wo

CONCLUSIONS:
Certainly! The Smart Clock System project leverages various technologies to create a versatile and interactive time management solution. By integrating speech recognition, text-to-speech conversion, and MQTT communication, the system enables users to control and interact with clock-related functionalities using their voice. Users can set alarms, timers, reminders, and inquire about the current time for different timezones and countries. The project's architecture empowers users to conveniently interact with the clock functionalities through natural language, enhancing accessibility and usability. The MQTT broker facilitates real-time communication and information sharing between different modules of the system, enabling seamless integration. The project not only offers practical time-related utilities but also serves as a showcase of how emerging technologies can be integrated to create innovative and user-friendly solutions for everyday tasks.

CODE EXPLAINITION:
(Explain in the document part properly)
