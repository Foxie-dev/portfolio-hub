import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tina | AI Portfolio", layout="wide")

# --- HEADER ---
st.title("🚀 Tina's Portfolio")
st.markdown("### AI Automation & Full-Stack Development")
st.write("Professional hub showcasing agentic workflows and intelligent applications.")
st.divider()

# --- THE BENTO GRID (2x2) ---
# Creating columns for a neat, symmetrical boxing style
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# --- PROJECT 1: AI LEAD SCOUT ---
with row1_col1:
    with st.container(border=True):
        st.subheader("🌍 AI Lead-Intelligence Scout")
        # POINTING TO YOUR NEW SCREENSHOT
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

# --- PROJECT 3: FINANCIAL REPORT RAG (PDF Assistant) ---
with row2_col1:
    with st.container(border=True):
        st.subheader("📊 Financial Report RAG")
        # This is where the RAG assistant image should actually go
        st.image("https://via.placeholder.com/600x400.png?text=RAG+PDF+Assistant", use_container_width=True)
        st.write("**Summary:** Conversational AI assistant designed to extract insights from complex PDF financial reports.")
        st.markdown("**🛠️ Tech:** `LangChain` | `ChromaDB` | `OpenAI` | `Streamlit` ")
        # Add your actual RAG link below when ready
        st.link_button("Launch RAG Assistant", "https://your-rag-link.streamlit.app")

# --- PROJECT 4: FUTURE AUTOMATION ---
with row2_col2:
    with st.container(border=True):
        st.subheader("🔧 Next-Gen AI Automation")
        st.image("https://via.placeholder.com/600x400.png?text=Coming+Soon", use_container_width=True)
        st.write("**Summary:** My next project focusing on real-world process automation using advanced Agentic logic.")
        st.markdown("**🛠️ Tech:** `Python` | `LLMs` | `AutoGPT` ")
        st.info("📅 Status: Coming Soon")