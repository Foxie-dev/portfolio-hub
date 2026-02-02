import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Portfolio Hub", layout="wide")

# --- CUSTOM CSS FOR MODERN LOOK ---
st.markdown("""
    <style>
    .stContainer {
        background-color: #1e1e1e;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #333;
    }
    .stHeader {
        color: #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🚀 Elia's AI Portfolio")
st.markdown("### Specialized in Agentic Workflows & Full-Stack Automation")
st.write("Welcome to my hub. Here I showcase my journey in building intelligent systems.")
st.divider()

# --- THE BENTO GRID (2x2) ---
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# --- PROJECT 1: AI LEAD SCOUT ---
with row1_col1:
    with st.container(border=True):
        st.subheader("🌍 AI Lead-Intelligence Scout")
        st.image("ai_screenshot.png") # Make sure this file exists in your repo!
        st.write("**One-liner:** A multi-agent system that automates corporate scouting and financial auditing for social impact.")
        st.markdown("**🛠️ Tech Stack:** `Python` | `CrewAI` | `GPT-4o` | `Serper` | `Streamlit`")
        st.link_button("Launch Agent", "https://universal-social-impact-lead-gen-qngbjvmc4toqyhuwe34au3.streamlit.app/")
        st.link_button("View Code", "https://github.com/Foxie-dev/Universal-Social-Impact-Lead-Gen")

# --- PROJECT 2: GROOMING SYSTEM ---
with row1_col2:
    with st.container(border=True):
        st.subheader("🐶 Grooming Booking System")
        st.image("grooming_screenshot.png") # This exists in your repo!
        st.write("**One-liner:** A full-stack booking platform for pet services with real-time scheduling and customer management.")
        st.markdown("**🛠️ Tech Stack:** `React` | `Node.js` | `Vercel` | `Tailwind CSS`")
        st.link_button("View on Vercel", "https://dog-grooming-booking.vercel.app/")

# --- PROJECT 3: FINANCIAL RAG (Placeholder) ---
with row2_col1:
    with st.container(border=True):
        st.subheader("📊 Financial Report RAG")
        st.write("**One-liner:** A conversational AI assistant that extracts and analyzes deep insights from complex PDF financial reports.")
        st.markdown("**🛠️ Tech Stack:** `LangChain` | `ChromaDB` | `OpenAI` | `Streamlit`")
        st.info("Status: 🚧 Under Construction")

# --- PROJECT 4: FUTURE AGENT (Placeholder) ---
with row2_col2:
    with st.container(border=True):
        st.subheader("🔧 Next-Gen AI Automation")
        st.write("**One-liner:** My next project focusing on real-world process automation using advanced Agentic logic.")
        st.markdown("**🛠️ Tech Stack:** `TBD` | `Python` | `LLMs`")
        st.info("Status: 📅 Coming Soon")