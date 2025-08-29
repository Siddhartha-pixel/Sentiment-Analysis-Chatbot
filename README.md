##Safe AI Voice Chatbot
This project is a mental health-focused chatbot application with a graphical user interface (GUI). Developed in Python, it uses sentiment analysis to provide emotionally aware conversational support and, in critical situations, sends an emergency SMS alert to a trusted contact.

##⚙️ Features
Voice and Text Interaction: Users can communicate with the chatbot by typing or by speaking using their microphone. The system supports both voice input and text-to-speech output for natural interaction.

Sentiment Analysis: The chatbot analyzes user input to determine if the sentiment is positive, negative, or neutral. It then provides a tailored, supportive response based on the detected emotion.

Critical Keyword Detection: A predefined list of keywords related to self-harm and danger is used to identify and respond to high-risk situations immediately.

Emergency SMS Alert: In response to critical keywords, the application automatically sends a text message alert to a pre-configured trusted phone number using the Twilio API. This serves as an immediate intervention mechanism.

Accessibility & Usability: The GUI is built with CustomTkinter and includes features like "High Contrast" mode to improve readability and "Anonymous Mode" for user privacy.

Resource Suggestions: A dedicated button provides a list of mental health resources and helplines.

## 🚀 How to Run the App
Clone the Repository: Download or clone this project to your local machine.

Set up a Virtual Environment: It is highly recommended to use a virtual environment to manage dependencies. Open your terminal in the project directory and run:

Bash

python -m venv venv
Activate the Virtual Environment:

On Windows: venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

Install the Required Libraries: Install all necessary dependencies using the requirements.txt file.

Bash

pip install -r requirements.txt
Configure Twilio API: The application requires your Twilio API credentials to send SMS alerts. To keep your sensitive information secure, you must set these as environment variables on your system. You can get these details from your Twilio dashboard.

TWILIO_SID

TWILIO_AUTH_TOKEN

TWILIO_PHONE_NUMBER

TRUSTED_PHONE_NUMBER

Run the Application: Once the setup is complete, you can start the chatbot application:

Bash

python modern_chatbot5.py

## 📋 Requirements
The following Python libraries are required to run the chatbot:

customtkinter: For the modern, customizable GUI.

speechrecognition: To handle voice input from the user.

pyttsx3: To enable the chatbot's voice (text-to-speech).

transformers: To perform sentiment analysis using a pre-trained model.

torch: A dependency of the transformers library, required for the model to run.

twilio: To send emergency SMS alerts to a trusted contact.

⚠️ Important Disclaimer
This application is a prototype and should not be used as a substitute for professional medical or psychological advice. In an emergency, always contact a trained professional or an official helpline.
