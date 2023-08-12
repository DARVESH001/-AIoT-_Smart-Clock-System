#include "HardwareSerial.h"
#include <SPI.h>
#include <Wire.h>
#include <SoftWire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Ethernet.h>
#include <PubSubClient.h>




// #define PIN0_SDA 18
// #define PIN0_SCL 19
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 32
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C



byte mac[] = { 0xDE, 0xAD, 103, 0xEF, 0xFE, 0xED }; // Replace with your desired MAC address
IPAddress ip(172, 16, 0, 100); // Replace with the desired IP address
IPAddress server(44, 195, 202, 69);
const char* alarm_system = "alarm_system" ;

EthernetClient ethClient ;
PubSubClient client( ethClient );

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
      // Open serial communications and wait for port to open:
  Serial3.setRx(PC11);
  Serial3.setTx(PC10);
  Serial3.begin(9600);

    while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

	Wire.setSDA(14);
	Wire.setSCL(15);
	Wire.begin();

  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    for (;;) {
    }
  }


  display.clearDisplay();
  display.display();
  
  // Print "CLOCK" on the OLED display
  display.setTextSize(2);      // Set text size
  display.setTextColor(SSD1306_WHITE); // Set text color
  display.setCursor(0, 0);     // Set text cursor position
  display.println("SMART ");    // Print "CLOCK"
  display.setTextSize(2);      // Set text size
  display.println("     CLOCK ");
  display.display();           // Display the content

  // Ethernet setup
  Ethernet.begin(mac);
  //Ethernet.init(17);

  // Wait for Ethernet to be ready
  while (!Ethernet.begin(mac)) {
    Serial.println("Failed to configure Ethernet using DHCP");
    delay(10000);
  }

  Serial.print("Ethernet connected! IP address: ");
  Serial.println(Ethernet.localIP());

  delay(2000);

  // MQTT setup
  client.setServer(server , 1883);
  client.setCallback(callback);
  reconnect();
  client.subscribe("alarm_system"); // Replace with your MQTT topic for timer duration
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.print("Received message on topic: ");
  Serial.println(topic);
  Serial.print("Message: ");
  Serial.println(message);

  // Clear the OLED display
  display.clearDisplay();

  // Display received message on the OLED screen
  display.setTextSize(1.5);      // Set text size
  display.setTextColor(SSD1306_WHITE); // Set text color
  display.setCursor(0, 0);     // Set text cursor position
  //display.println("Received:"); // Print a label
  
  display.println(message);     // Print the received message
  display.display();           // Display the content
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    if (client.connect("arduinoClient103")) {
      Serial.println("connected");
      client.subscribe(alarm_system); // Subscribe to the MQTT topic for timer duration
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

