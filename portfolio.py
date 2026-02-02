import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tina | AI Portfolio", layout="wide")

# --- HEADER ---
st.title("🚀 Tina's Portfolio")
st.markdown("### AI Automation & Full-Stack Development")
st.write("Professional hub showcasing agentic workflows and intelligent applications.")
st.divider()

# --- THE BENTO GRID (2x2) ---
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# --- PROJECT 1: AI LEAD SCOUT ---
with col1:
    with st.container(border=True):
        st.subheader("🌍 AI Lead-Intelligence Scout")
        st.write("**Summary:** A multi-agent AI system automating corporate scouting and Swedish B2B financial auditing.")
        st.markdown("**🛠️ Tech:** `Python` | `CrewAI` | `GPT-4o` | `Serper` ")
        # CORRECTED LINK
        st.link_button("Launch Scout", "https://universal-social-impact-lead-gen-qngbjvmc4toqyhuwe34au3.streamlit.app/")
        st.link_button("View Code", "https://github.com/Foxie-dev/Universal-Social-Impact-Lead-Gen")

# --- PROJECT 2: DOG GROOMING SYSTEM ---
with col2:
    with st.container(border=True):
        st.subheader("🐶 Grooming Booking System")
        st.write("**Summary:** Full-stack booking platform for pet services with real-time scheduling and management.")
        st.markdown("**🛠️ Tech:** `React` | `Node.js` | `Vercel` | `Tailwind` ")
        st.link_button("View on Vercel", "https://dog-grooming-booking.vercel.app/")

# --- PROJECT 3: PDF RAG ASSISTANT ---
with col3:
    with st.container(border=True):
        st.subheader("📊 PDF RAG Assistant")
        st.write("**Summary:** Conversational AI assistant designed to extract and analyze insights from complex PDF reports.")
        st.markdown("**🛠️ Tech:** `LangChain` | `ChromaDB` | `OpenAI` | `Streamlit` ")
        # Ensure your RAG link is pasted here when ready
        st.link_button("Launch RAG Assistant", "https://ai-market-intelligence-app-r58mtkgg7ojsnfbehb9ubk.streamlit.app/")

# --- PROJECT 4: FUTURE AUTOMATION ---
with col4:
    with st.container(border=True):
        st.subheader("🔧 Next-Gen AI Automation")
        st.write("**Summary:** Exploring advanced agentic logic for industrial and corporate process automation.")
        st.markdown("**🛠️ Tech:** `Python` | `LLMs` | `AutoGPT` ")
        st.info("📅 Status: Coming Soon")