# app.py
# DecodeLabs - Batch 2026 | Full Fixed Version

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from groq import Groq
import random
import os
import re

# ── SETUP ────────────────────────────────────────
load_dotenv()
app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── KNOWLEDGE BASE ──────────────────────────────
responses = {
    "hello":        ["Hi there! How can I help you?", "Hey! Good to see you!", "Hello! What can I do for you?"],
    "hi":           ["Hey!", "Hi there!", "Greetings!"],
    "hey":          ["Hey! How can I help?", "Hey there!", "Hello!"],
    "how are you":  ["I'm running at 100% efficiency!", "All systems operational!", "Doing great, thanks for asking!"],
    "what is ai":   ["AI is machines simulating human intelligence.", "AI is the science of making machines think!", "Artificial Intelligence — the field I was born from!"],
    "who made you": ["I was built by a DecodeLabs engineer — you!", "A brilliant DecodeLabs intern created me!", "You did! Pretty cool, right?"],
    "help":         ["I can answer: hello, hi, how are you, what is ai, who made you."],
    "what is your name": ["I am DecoBot!", "They call me DecoBot!", "DecoBot at your service!"],
    "what is python":    ["Python is the language I was built with.", "Python — the best language for AI!", "A powerful programming language used in AI and data science."],
    "who are you":       ["I am an AI chatbot built by a DecodeLabs intern!", "DecoBot — your rule-based assistant!", "I am your first AI creation!"],
    "what can you do":   ["I can answer questions, remember your name, and use Groq AI for anything else!", "I am a hybrid chatbot — rules for speed, AI for flexibility!"],
    "what is decobot":   ["DecoBot is a rule-based AI chatbot built from scratch by a DecodeLabs intern!", "I am DecoBot — fast, smart, and always in control!"],
    "what is this app":  ["This is DecoBot — a rule-based AI chatbot built with Python and Flask!", "DecoBot is an AI assistant that uses rules for fast replies and Groq AI for complex questions!"],
}

# ── MEMORY & HISTORY ─────────────────────────────
memory = {}
conversation_history = []

# ── MEMORY DETECTION ─────────────────────────────
def check_memory(clean_input):
    if "my name is" in clean_input:
        name = clean_input.split("my name is")[-1].strip()
        memory["name"] = name.capitalize()
        return f"Nice to meet you, {memory['name']}! I will remember that."

    if "what is my name" in clean_input or "do you remember my name" in clean_input:
        if "name" in memory:
            return f"Of course! Your name is {memory['name']}."
        else:
            return "You haven't told me your name yet!"

    return None

# ── RULE-BASED REPLY ─────────────────────────────
GREETINGS = ["hi", "hello", "hey"]

def get_reply(clean_input):
    # exact match for short greeting words only
    if clean_input in GREETINGS:
        return random.choice(responses.get(clean_input, responses["hello"]))

    # partial match for longer keys only (skip short greeting words)
    for key in responses:
        if key in GREETINGS:
            continue
        if re.search(r'\b' + re.escape(key) + r'\b', clean_input):
            reply = random.choice(responses[key])
            if "name" in memory:
                reply = f"{memory['name']}, " + reply
            return reply

    return None

# ── LLM FALLBACK (GROQ + HISTORY) ────────────────
def get_llm_reply(clean_input):
    conversation_history.append({"role": "user", "content": clean_input})
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=200,
            messages=[
                {"role": "system", "content": "You are DecoBot, a helpful and friendly AI assistant. Keep answers short and clear — max 2 sentences."},
                *conversation_history
            ]
        )
        reply = chat_completion.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return "Sorry, I am having trouble connecting right now. Please try again!"

# ── ROUTES ───────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower().strip()

    # priority 1: memory
    memory_reply = check_memory(user_message)
    if memory_reply:
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": memory_reply})
        return jsonify({"reply": memory_reply})

    # priority 2: rule-based
    rule_reply = get_reply(user_message)
    if rule_reply:
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": rule_reply})
        return jsonify({"reply": rule_reply})

    # priority 3: LLM fallback
    llm_reply = get_llm_reply(user_message)
    return jsonify({"reply": llm_reply})

# ── START ────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)