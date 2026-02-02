import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tina | AI Portfolio", layout="wide")

# Header Section
st.title("🚀 Tina's Portfolio")
st.markdown("### AI Automation & Full-Stack Development")
st.write("Professional hub showcasing agentic workflows and intelligent applications.")
st.divider()

# --- THE BENTO GRID (2x2) ---
# We use columns to create the "boxing" style for symmetry
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# --- PROJECT 1: AI LEAD SCOUT ---
with row1_col1:
    with st.container(border=True):
        st.subheader("🌍 AI Lead-Intelligence Scout")
        # This looks for the image you just pushed
        st.image("ai_screenshot.png", use_container_width=True) 
        st.write("**Summary:** A multi-agent AI system automating corporate scouting and Swedish B2B financial auditing.")
        st.markdown("**🛠️ Tech:** `Python` | `CrewAI` | `GPT-4o` | `Serper` ")
        # CORRECTED LINK
        st.link_button("Launch Scout", "https://universal-social-impact-lead-gen-qngbjvmc4toqyhuwe34au3.streamlit.app/")
        st.link_button("View Code", "https://github.com/Foxie-dev/Universal-Social-Impact-Lead-Gen")

# --- PROJECT 2: DOG GROOMING SYSTEM ---
with row1_col2:
    with st.container(border=True):
        st.subheader("🐶 Grooming Booking System")
        st.image("grooming_screenshot.png", use_container_width=True) 
        st.write("**Summary:** Full-stack booking platform for pet services with real-time scheduling and management.")
        st.markdown("**🛠️ Tech:** `React` | `Node.js` | `Vercel` | `Tailwind` ")
        st.link_button("View on Vercel", "https://dog-grooming-booking.vercel.app/")

# --- PROJECT 3: FINANCIAL REPORT RAG ---
with row2_col1:
    with st.container(border=True):
        st.subheader("📊 Financial Report RAG")
        # Placeholder image until you have a RAG screenshot
        st.image("https://via.placeholder.com/600x400.png?text=Financial+RAG+Dashboard", use_container_width=True)
        st.write("**Summary:** Conversational AI for extracting deep insights from complex PDF financial reports.")
        st.markdown("**🛠️ Tech:** `LangChain` | `ChromaDB` | `OpenAI` | `Streamlit` ")
        # REPLACE '#' WITH YOUR ACTUAL RAG LINK BELOW
        st.link_button("Launch RAG", "https://your-rag-link.streamlit.app")

# --- PROJECT 4: FUTURE AUTOMATION ---
with row2_col2:
    with st.container(border=True):
        st.subheader("🔧 Next-Gen AI Automation")
        st.image("https://via.placeholder.com/600x400.png?text=Coming+Soon", use_container_width=True)
        st.write("**Summary:** Exploring advanced agentic logic for industrial and corporate process automation.")
        st.markdown("**🛠️ Tech:** `Python` | `LLMs` | `AutoGPT` ")
        st.info("📅 Status: Coming Soon")