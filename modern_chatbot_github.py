import customtkinter as ctk
import threading
import speech_recognition as sr
import pyttsx3
from transformers import pipeline
from twilio.rest import Client

# ---------------------------
# Sentiment Analysis Setup
# ---------------------------
print("Loading sentiment model...")
sentiment_analyzer = pipeline("sentiment-analysis")

# ---------------------------
# Text-to-Speech Setup
# ---------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# ---------------------------
# Twilio SMS Alert Setup
# ---------------------------
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TRUSTED_PHONE_NUMBER = os.getenv("TRUSTED_PHONE_NUMBER")

twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_alert_sms(user_text):
    message = f"⚠️ ALERT: User expressed thoughts indicating danger: '{user_text}'"
    try:
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=TRUSTED_PHONE_NUMBER
        )
        print("Alert SMS sent successfully!")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# ---------------------------
# Critical Negative Keywords
# ---------------------------
critical_negative_words = [
    "suicide", "kill myself", "end my life", "die", "harm myself", "cut myself",
    "hang myself", "jump off", "depressed", "hopeless", "worthless", "alone",
    "give up", "no way out", "cant go on", "destroy myself", "self harm",
    "pain too much", "kill", "die soon", "tired of living", "want to die",
    "life is over", "hopelessness", "i hate myself", "cant handle life",
    "life is meaningless", "i am done", "end it all", "i feel dead inside",
    "ready to die", "self destruction", "hurt myself", "life is painful",
    "kill me", "i am worthless", "suffering too much", "kill my pain",
    "no hope", "give up on life", "suicidal thoughts", 
    "i cant cope", "life is hopeless", "hate my life", "dont want to live",
    "life is over", "life is meaningless", "ready to end it", "finished with life" ,"blood"
]

# ---------------------------
# GUI Setup
# ---------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Safe AI Voice Chatbot")
app.geometry("780x700")
app.configure(bg_color="#283751")  # subtle blue shade

# Accessibility: High Contrast
high_contrast = ctk.BooleanVar(value=False)
def toggle_contrast():
    if high_contrast.get():
        app.configure(bg_color="#fffacd")
        chat_box.configure(fg_color="#000", bg_color="#fff")
    else:
        app.configure(bg_color="#283751")
        chat_box.configure(fg_color="#fff", bg_color="#283751")
contrast_switch = ctk.CTkSwitch(app, text="High Contrast", variable=high_contrast, command=toggle_contrast)
contrast_switch.grid(row=0, column=3, padx=16, pady=12)

# Anonymous Mode
anonymous_mode = ctk.BooleanVar(value=False)
anonymous_switch = ctk.CTkSwitch(app, text="Anonymous Mode", variable=anonymous_mode)
anonymous_switch.grid(row=0, column=0, padx=16, pady=12)

# Chatbox
chat_box = ctk.CTkTextbox(app, width=700, height=420, wrap="word", font=("Arial", 16), bg_color="#283751")
chat_box.grid(row=1, column=0, columnspan=4, padx=18, pady=18, sticky="nsew")
chat_box.insert("end", "🤖 Chatbot Ready! Type or speak a message.\n\n")

# Entry Box
entry = ctk.CTkEntry(app, width=500, font=("Arial", 15), placeholder_text="Type your message or use Voice...")
entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Text-to-Speech Toggle
tts_enabled = ctk.BooleanVar(value=True)
def toggle_tts():
    state = tts_enabled.get()
    if state:
        chat_box.insert("end", "🔊 Bot voice enabled.\n\n")
    else:
        chat_box.insert("end", "🔇 Bot voice disabled.\n\n")
    chat_box.see("end")
tts_switch = ctk.CTkSwitch(app, text="Bot Voice", variable=tts_enabled, command=toggle_tts)
tts_switch.grid(row=2, column=2, padx=12, pady=10)

# Resource Suggestions
def show_resources():
    chat_box.insert("end", (
        "🧠 Mental Health Resources:\n"
        "- Mindfulness: Headspace app\n"
        "- Therapist Directory: https://therapyroute.com/in\n"
        "- Indian Helplines: 022-2772 6771\n"
        "- Meditation: https://www.calm.com\n\n"
    ))
    chat_box.see("end")
resources_btn = ctk.CTkButton(app, text="Show Resources", command=show_resources)
resources_btn.grid(row=2, column=3, padx=10, pady=10)

# AI Reply
def get_ai_reply(user_text):
    user_text_lower = user_text.lower()
    # Step 1: Critical negative words
    if any(word in user_text_lower for word in critical_negative_words):
        sentiment_label = "NEGATIVE"
        bot_response = (
            "⚠️ It seems you might be in danger or having harmful thoughts. "
            "Please seek help immediately! Contact a trained professional or call a helpline.\n"
            "For India, call: 022-2772 6771 or 022-2754 6669\n"
            "Additionally, an alert has been sent to your trusted contact for support."
        )
        send_alert_sms(user_text)
    else:
        # Step 2: Regular sentiment analysis
        sentiment = sentiment_analyzer(user_text)[0]
        sentiment_label = sentiment['label']
        # Recommendations
        if sentiment_label == "NEGATIVE":
            bot_response = (
                "😊 It seems you're feeling low. Try a walk, music, or deep breathing. "
                "You can also check 'Show Resources' for helpful options."
            )
        elif sentiment_label == "POSITIVE":
            bot_response = (
                "🎉 That's great! Keep up the positivity. Maybe try something creative or productive!"
            )
        else:
            bot_response = (
                "🙂 Thanks for sharing. Keep going! You might enjoy learning something new or taking a break."
            )

    # Display in chat
    user_name = "You (Anonymous)" if anonymous_mode.get() else "You"
    chat_box.insert("end", f"{user_name}: {user_text}\n")
    chat_box.insert("end", f"Sentiment: {sentiment_label}\n")
    chat_box.insert("end", f"Bot: {bot_response}\n\n")
    chat_box.see("end")

    # Speak bot response if TTS enabled
    if tts_enabled.get():
        engine.say(bot_response)
        engine.runAndWait()

# Send Button
def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    entry.delete(0, "end")
    threading.Thread(target=get_ai_reply, args=(user_text,)).start()
send_btn = ctk.CTkButton(app, text="Send", command=send_message)
send_btn.grid(row=3, column=0, padx=8, pady=10)

# Voice Input
def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        chat_box.insert("end", "🎤 Listening...\n")
        chat_box.see("end")
        audio = r.listen(source)
    try:
        user_text = r.recognize_google(audio)
        chat_box.insert("end", f"You (Voice): {user_text}\n")
        threading.Thread(target=get_ai_reply, args=(user_text,)).start()
    except:
        chat_box.insert("end", "❌ Sorry, I could not understand your voice.\n")

voice_btn = ctk.CTkButton(app, text="🎤 Speak", command=lambda: threading.Thread(target=voice_input).start())
voice_btn.grid(row=3, column=1, padx=8, pady=10)

# Grid row & column config for resizing
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

app.mainloop()
