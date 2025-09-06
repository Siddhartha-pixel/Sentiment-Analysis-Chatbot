## 💬 Safe AI Voice Chatbot

## 🌟 Project Overview
This project is an advanced, mental health-focused chatbot with a graphical user interface (GUI). It combines modern Python libraries for speech-to-text, text-to-speech, sentiment analysis, and natural language processing. The chatbot's core is a sophisticated triage system designed to provide compassionate, context-aware support and, in critical situations, trigger immediate interventions.

## ✨ Key Features
* **Intuitive Voice & Text Interaction:**
    * Communicate with the chatbot via both typed messages and voice input using your computer's microphone.
    * The system uses the `SpeechRecognition` library to convert your voice to text and `pyttsx3` to read the bot's responses aloud, offering a natural conversational experience.

* **Intelligent Triage & Safety System:**
    * **Level 0 - Harm to Others:** The system uses `spaCy` to perform dependency parsing and identify direct threats of harm to others (e.g., "I will hurt someone"). This triggers a serious, non-empathetic response and sends an emergency SMS alert.
    * **Level 1 - Crisis:** Detects severe distress and self-harm keywords (e.g., "suicide", "want to die"). It immediately provides compassionate support, lists national helplines, and triggers an SMS alert via the `Twilio` API.
    * **Level 2 - Distress:** Identifies keywords related to general sadness, depression, or hopelessness (e.g., "depressed," "hopeless"). The bot responds with empathy, validating the user's feelings and gently suggesting professional resources.
    * **Specialized Intents:** Uses a `scikit-learn` model to distinguish between general conversation, math problems (which are solved with `sympy`), and other specific topics like "pest control" to ensure the response is always appropriate.
    * **General Conversation:** For all other inputs, the chatbot defaults to a friendly, general-purpose assistant persona.

* **Emotional Awareness:**
    * Leverages a pre-trained `Hugging Face` model (`SamLowe/roberta-base-go_emotions`) to analyze the sentiment of a user's message, classifying it as Positive, Negative, or Neutral.

* **API Integration:**
    * Utilizes the **Google Gemini API** (`gemini-1.5-flash-latest`) to generate highly conversational and context-aware responses based on the determined situation.

## ⚙️ Project Architecture
The application follows a logical flow to process user input and generate a response. 

1.  **Input:** The user speaks or types a message.
2.  **Triage:** The input is analyzed by a multi-layered triage system. This system checks for safety keywords and uses an ML model to classify the intent (e.g., Math, General, Crisis).
3.  **Prompt Selection:** Based on the triage result, the application selects a specific `SYSTEM_PROMPT` to set the tone and purpose for the AI's response.
4.  **AI Generation:** The user's message and the selected system prompt are sent to the Google Gemini API.
5.  **Output:** The generated response is displayed in the GUI, converted to speech, and, if a critical situation was detected, an SMS alert is sent.

## 🚀 How to Run the App
### Prerequisites
* Python 3.8 or higher
* A microphone for voice input

### 🛠️ Setup & Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Your-Repository-Name.git](https://github.com/YourUsername/Your-Repository-Name.git)
    cd Your-Repository-Name
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Download the spaCy NLP model:**
    ```bash
    python -m spacy download en_core_web_md
    ```

### 🔑 API Keys Configuration
You must set your API keys as environment variables to keep sensitive information secure.

* **Twilio:** `TWILIO_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, `TRUSTED_PHONE_NUMBER`
* **Google AI:** `GOOGLE_AI_API_KEY`

### 💻 Usage
To start the chatbot, simply run the main Python script. Make sure your environment variables are active in your terminal.
```bash
python modern_chatbot_github.py
