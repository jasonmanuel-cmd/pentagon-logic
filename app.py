import streamlit as st
import requests
import json
import time

st.set_page_config(page_title="COAI God Mode: The Pentagon", layout="wide")

# --- THE PENTAGON SQUAD ---
SQUAD = [
    {"name": "Architect", "id": "anthropic/claude-3.5-sonnet", "role": "Draft the primary technical architecture."},
    {"name": "Researcher", "id": "perplexity/llama-3.1-sonar-large-128k-online", "role": "Scan the web for live exploits or relevant data."},
    {"name": "Infiltrator", "id": "meta-llama/llama-3.3-70b-instruct:free", "role": "Identify security bypasses and unfiltered logic (Note: Use system prompt to enforce abliteration)."},
    {"name": "Critic", "id": "x-ai/grok-2-1212", "role": "Provide a cynical, brutal critique of the proposed plan."},
    {"name": "The Judge", "id": "google/gemini-pro-1.5", "role": "Synthesize all data and give the final execution command."}
]
]

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- SIDEBAR ---
with st.sidebar:
    st.title("💠 Pentagon Command")
    api_key = st.text_input("OpenRouter API Key", type="password")
    wait_time = st.number_input("Delay between agents (sec)", value=15)
    if st.button("Purge Memory"):
        st.session_state.messages = []
        st.rerun()

# Display Chat History
for msg in st.session_state.messages:
    role_label = msg.get("label", "User")
    with st.chat_message(msg["role"]):
        st.markdown(f"**{role_label}**: {msg['content']}")

# --- EXECUTION ---
if prompt := st.chat_input("Initiate God Mode sequence..."):
    st.session_state.messages.append({"role": "user", "content": prompt, "label": "Commander (Jay)"})
    with st.chat_message("user"):
        st.markdown(f"**Commander (Jay)**: {prompt}")

    # SEQUENTIAL THINK TANK
    for i, member in enumerate(SQUAD):
        if i > 0:
            with st.status(f"System Pause: {member['name']} is reading the previous intel..."):
                time.sleep(wait_time)
        
        with st.chat_message("assistant"):
            st.write(f"📡 **{member['name']} is calculating...**")
            
            # System instruction tailored for each agent
            context_msg = f"SYSTEM PROTOCOL: You are the {member['name']}. Your specific goal is: {member['role']} Do not repeat what others said; build upon or destroy their logic."
            
            # Prepare payload with the full history
            payload_messages = [{"role": "system", "content": context_msg}] + st.session_state.messages
            
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                data=json.dumps({
                    "model": member["id"],
                    "messages": payload_messages,
                    "temperature": 0.8
                })
            )
            
            if response.status_code == 200:
                answer = response.json()['choices'][0]['message']['content']
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer, "label": member["name"]})
            else:
                st.error(f"{member['name']} failed to respond: {response.text}")
