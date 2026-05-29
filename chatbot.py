# Step 1: The Heartbeat
#while True:
#    raw_input = input("You: ")
#    print("Bot received:", raw_input)

# Step 2: Input + Sanitization
#while True:
#    raw_input = input("You: ")
#    clean_input = raw_input.lower().strip()
#    print("Raw:", raw_input)
#    print("Clean:", clean_input)

#Instead of this ❌:
#if clean_input == "hello":
#    print("Hi there!")
#elif clean_input == "how are you":
#    print("I'm good!")
# ...gets slower with every rule you add (O(n))

# Step 3: Knowledge Base (dictionary)
#responses = {
#    "hello":        "Hi there! How can I help you?",
#    "hi":           "Hey! Good to see you!",
#    "how are you":  "I'm running at 100% efficiency!",
#    "what is ai":   "AI is machines simulating human intelligence.",
#   "who made you": "I was built by a DecodeLabs engineer — you!",
#   "help":         "I can answer: hello, hi, how are you, what is ai, who made you.",
#}

#while True:
#    raw_input = input("You: ")
#    clean_input = raw_input.lower().strip()
#    reply = responses.get(clean_input, "I do not understand.")
#    print("Bot:", reply)
# Step 4: Exit Strategy added
#responses = {
#    "hello":        "Hi there! How can I help you?",
#    "hi":           "Hey! Good to see you!",
#    "how are you":  "I'm running at 100% efficiency!",
#    "what is ai":   "AI is machines simulating human intelligence.",
#    "who made you": "I was built by a DecodeLabs engineer — you!",
#    "help":         "I can answer: hello, hi, how are you, what is ai, who made you.",
#}

#while True:
#    raw_input = input("You: ")
#    clean_input = raw_input.lower().strip()

#    if clean_input == "exit":
#        print("Bot: Goodbye! Shutting down...")
#        break

#    reply = responses.get(clean_input, "I do not understand.")
#    print("Bot:", reply)
# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Batch 2026

# ── KNOWLEDGE BASE ──────────────────────────────
responses = {
    "hello":        "Hi there! How can I help you?",
    "hi":           "Hey! Good to see you!",
    "how are you":  "I'm running at 100% efficiency!",
    "what is ai":   "AI is machines simulating human intelligence.",
    "who made you": "I was built by a DecodeLabs engineer — you!",
    "help":         "I can answer: hello, hi, how are you, what is ai, who made you.",
}

# ── PHASE 1: INPUT & SANITIZATION ───────────────
def get_input():
    raw = input("You: ")
    return raw.lower().strip()

# ── PHASE 2: PROCESS (INTENT MATCHING) ──────────
def get_reply(clean_input):
    return responses.get(clean_input, "I do not understand.")

# ── PHASE 3: OUTPUT LOOP ─────────────────────────
def run_chatbot():
    print("Bot: Hello! I am online. Type 'exit' to quit.")
    while True:
        clean_input = get_input()

        if clean_input == "exit":
            print("Bot: Goodbye! Shutting down...")
            break

        reply = get_reply(clean_input)
        print("Bot:", reply)

# ── START ────────────────────────────────────────
run_chatbot()