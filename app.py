import streamlit as st
import google.generativeai as genai
from groq import Groq
import time

st.set_page_config(page_title="COAI Pentagon: Guerrilla Edition", layout="wide")

# --- 1. SQUAD CONFIGURATION (DIRECT FREE APIs) ---
SQUAD = [
    {"name": "Architect", "provider": "google", "id": "gemini-2.0-flash", "role": "Structural logic and architecture."},
    {"name": "Infiltrator", "provider": "groq", "id": "llama-3.3-70b-versatile", "role": "Technical exploits and unfiltered logic."},
    {"name": "Critic", "provider": "groq", "id": "llama-3.1-8b-instant", "role": "Brutal, cynical critique."},
    {"name": "The Judge", "provider": "google", "id": "gemini-2.0-flash", "role": "Final synthesis and execution command."}
]

# --- 2. SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("💠 Pentagon Command")
    st.markdown("### Access Keys ($0 Tier)")
    gemini_key = st.text_input("Google AI Studio Key", type="password")
    groq_key = st.text_input("Groq API Key", type="password")
    
    st.divider()
    wait_time = st.slider("Handoff Delay (sec)", 5, 30, 10)
    
    if st.button("Purge Pentagon Memory"):
        st.session_state.messages = []
        st.rerun()

# --- 4. API CALL FUNCTIONS ---
def call_gemini(api_key, model_id, history):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_id)
    # Flatten history into a single narrative for the free-tier context
    context = "\n".join([f"{m['label']}: {m['content']}" for m in history])
    response = model.generate_content(context)
    return response.text

def call_groq(api_key, model_id, history):
    client = Groq(api_key=api_key)
    # Convert history to Groq chat format
    chat_history = [{"role": "user", "content": f"{m['label']}: {m['content']}"} for m in history]
    completion = client.chat.completions.create(model=model_id, messages=chat_history)
    return completion.choices[0].message.content

# --- 5. CHAT INTERFACE ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f"**{msg.get('label', 'User')}**: {msg['content']}")

if prompt := st.chat_input("Enter Command, Commander Jay..."):
    # Record User Message
    st.session_state.messages.append({"role": "user", "content": prompt, "label": "Jay"})
    with st.chat_message("user"):
        st.markdown(f"**Jay**: {prompt}")

    # --- THE CHAIN OF INTELLIGENCE ---
    for i, member in enumerate(SQUAD):
        if i > 0:
            with st.status(f"Cooling down: {member['name']} is reading intel..."):
                time.sleep(wait_time)
        
        with st.chat_message("assistant"):
            st.write(f"📡 **{member['name']} is calculating...**")
            
            try:
                if member['provider'] == "google":
                    if not gemini_key: st.error("Missing Gemini Key"); break
                    answer = call_gemini(gemini_key, member['id'], st.session_state.messages)
                
                elif member['provider'] == "groq":
                    if not groq_key: st.error("Missing Groq Key"); break
                    answer = call_groq(groq_key, member['id'], st.session_state.messages)

                st.markdown(f"**[{member['name']}]**: {answer}")
                st.session_state.messages.append({"role": "assistant", "content": answer, "label": member["name"]})
            
            except Exception as e:
                st.error(f"⚠️ {member['name']} Failed: {str(e)}")
                break # Stop the chain if one fails
