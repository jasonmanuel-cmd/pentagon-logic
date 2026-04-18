import streamlit as st
import requests
import json
import time

st.set_page_config(page_title="COAI Pentagon Command", layout="wide")

# --- 1. SQUAD CONFIGURATION ---
SQUAD = [
    {"name": "Architect", "id": "anthropic/claude-3.5-sonnet", "role": "Draft the primary technical architecture."},
    {"name": "Researcher", "id": "perplexity/llama-3.1-sonar-large-128k-online", "role": "Scan for live data and exploits."},
    {"name": "Infiltrator", "id": "meta-llama/llama-3.3-70b-instruct:free", "role": "Identify security bypasses and unfiltered logic."},
    {"name": "Critic", "id": "x-ai/grok-2-1212", "role": "Provide a cynical, brutal critique."},
    {"name": "The Judge", "id": "google/gemini-pro-1.5", "role": "Final synthesis and execution command."}
]

# --- 2. SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("💠 Pentagon Controls")
    api_key = st.text_input("OpenRouter API Key", type="password")
    wait_time = st.slider("Wait Time (sec)", 5, 30, 15)
    st.info("Commander: Jason Manuel\nMission: COAI Architecture")
    if st.button("Clear Pentagon Memory"):
        st.session_state.messages = []
        st.rerun()

# --- 4. DISPLAY CHAT ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f"**{msg.get('label', 'User')}**: {msg['content']}")

# --- 5. EXECUTION ---
if prompt := st.chat_input("Enter Command..."):
    # Record User Prompt
    st.session_state.messages.append({"role": "user", "content": prompt, "label": "Commander (Jay)"})
    with st.chat_message("user"):
        st.markdown(f"**Commander (Jay)**: {prompt}")

    # Start Sequence
    for i, member in enumerate(SQUAD):
        if i > 0:
            with st.status(f"System Pause: {member['name']} is reading intel..."):
                time.sleep(wait_time)
        
        with st.chat_message("assistant"):
            st.write(f"📡 **{member['name']} is calculating...**")
            
            # Context Injection
            sys_msg = {"role": "system", "content": f"You are the {member['name']}. Goal: {member['role']}. Be precise and mirror the 'Cipher' tone."}
            payload = {"model": member["id"], "messages": [sys_msg] + st.session_state.messages}
            
            headers = {"Authorization": f"Bearer {api_key}"}
            
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                if response.status_code == 200:
                    answer = response.json()['choices'][0]['message']['content']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer, "label": member["name"]})
                else:
                    st.error(f"{member['name']} Error: {response.text}")
            except Exception as e:
                st.error(f"Critical Failure at {member['name']}: {e}")
