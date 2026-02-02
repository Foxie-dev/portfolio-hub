import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tina | AI Portfolio", layout="wide")

# --- CUSTOM CSS FOR PERFECT SYMMETRY ---
st.markdown("""
    <style>
    /* Force consistent card heights and styling */
    .stColumn > div {
        padding: 10px;
    }
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        border: 1px solid #333;
        border-radius: 15px;
        padding: 20px;
        background-color: #0e1117;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Elia's Portfolio")
st.markdown("### Specialized in Agentic Workflows & Full-Stack Automation")
st.divider()

# --- THE 2x2 BENTO GRID ---
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# --- PROJECT 1: AI LEAD SCOUT ---
with row1_col1:
    st.subheader("🌍 AI Lead-Intelligence Scout")
    st.image("ai_screenshot.png", use_container_width=True) #
    st.write("**Summary:** A multi-agent AI system that automates B2B research and Swedish corporate auditing.")
    st.markdown("**🛠️ Tech Stack:** `Python` | `CrewAI` | `GPT-4o` | `Serper` ")
    st.link_button("Launch App", "https://universal-social-impact-lead-gen-qngbjvmc4toqyhuwe34au3.streamlit.app/")
    st.link_button("View Code", "https://github.com/Foxie-dev/Universal-Social-Impact-Lead-Gen")

# --- PROJECT 2: GROOMING SYSTEM ---
with row1_col2:
    st.subheader("🐶 Grooming Booking System")
    st.image("grooming_screenshot.png", use_container_width=True) #
    st.write("**Summary:** Full-stack booking platform for pet services with real-time scheduling and customer management.")
    st.markdown("**🛠️ Tech Stack:** `React` | `Node.js` | `Vercel` | `Tailwind` ")
    st.link_button("View on Vercel", "https://dog-grooming-booking.vercel.app/")
    st.link_button("View Code", "https://github.com/Foxie-dev/dog-grooming-booking")

# --- PROJECT 3: FINANCIAL RAG (Now with Image & Link) ---
with row2_col1:
    st.subheader("📊 Financial Report RAG")
    # Using a placeholder image until you upload a real 'rag_screenshot.png'
    st.image("https://via.placeholder.com/600x400.png?text=Financial+RAG+Dashboard", use_container_width=True)
    st.write("**Summary:** Conversational AI that analyzes and extracts key insights from complex PDF financial reports.")
    st.markdown("**🛠️ Tech Stack:** `LangChain` | `ChromaDB` | `OpenAI` | `Streamlit` ")
    # Replace '#' with your actual RAG deployment link
    st.link_button("Launch RAG", "https://ai-market-intelligence-app-r58mtkgg7ojsnfbehb9ubk.streamlit.app/")

# --- PROJECT 4: FUTURE PROJECT ---
with row2_col2:
    st.subheader("🔧 Next-Gen AI Automation")
    st.image("https://via.placeholder.com/600x400.png?text=Coming+Soon", use_container_width=True)
    st.write("**Summary:** My next project focusing on real-world process automation using advanced Agentic logic.")
    st.markdown("**🛠️ Tech Stack:** `Python` | `LLMs` | `AutoGPT` ")
    st.info("Status: 📅 Coming Soon")