import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tina | AI Engineer", layout="wide")

# --- CUSTOM CSS FOR SYMMETRY ---
st.markdown("""
    <style>
    /* Force all project cards to have consistent spacing */
    [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        margin-bottom: 0px;
    }
    .project-card {
        border: 1px solid #333;
        border-radius: 15px;
        padding: 25px;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 Elia's Portfolio")
st.markdown("#### Senior AI Automation & Full-Stack Engineer")
st.write("Building agentic systems that bridge the gap between complex data and actionable insights.")
st.divider()

# --- THE 2x2 SYMMETRICAL GRID ---
row1_left, row1_right = st.columns(2)
row2_left, row2_right = st.columns(2)

# --- ROW 1, LEFT: AI LEAD SCOUT ---
with row1_left:
    with st.container(border=True):
        st.subheader("🌍 AI Lead Scout")
        st.image("ai_screenshot.png", use_container_width=True) # Placeholder for symmetry
        st.write("**Summary:** Multi-agent system automating Swedish B2B research and financial auditing.")
        st.markdown("**🛠️ Tech:** `CrewAI` • `GPT-4o` • `Serper` • `Python`")
        st.link_button("Launch Agent", "https://universal-social-impact-lead-gen-qngbjvmc4toqyhuwe34au3.streamlit.app/")

# --- ROW 1, RIGHT: DOG GROOMING ---
with row1_right:
    with st.container(border=True):
        st.subheader("🐶 Grooming System")
        st.image("grooming_screenshot.png", use_container_width=True)
        st.write("**Summary:** Full-stack booking platform with real-time scheduling and customer management.")
        st.markdown("**🛠️ Tech:** `React` • `Node.js` • `Vercel` • `Tailwind`")
        st.link_button("View on Vercel", "https://dog-grooming-booking.vercel.app/")

# --- ROW 2, LEFT: FINANCIAL RAG (NOW LIVE) ---
with row2_left:
    with st.container(border=True):
        st.subheader("📊 Financial Report RAG")
        # Ensure you have an image or use a colored placeholder for symmetry
        st.write("**Summary:** Conversational AI for extracting deep insights from complex PDF financial statements.")
        st.markdown("**🛠️ Tech:** `LangChain` • `ChromaDB` • `OpenAI` • `Streamlit`")
        # Replace the '#' with your actual RAG link below!
        st.link_button("Launch RAG App", "https://ai-market-intelligence-app-r58mtkgg7ojsnfbehb9ubk.streamlit.app/")

# --- ROW 2, RIGHT: FUTURE AUTOMATION ---
with row2_right:
    with st.container(border=True):
        st.subheader("🔧 Next-Gen AI Agent")
        st.write("**Summary:** Advanced Agentic logic focused on real-world industrial process automation.")
        st.markdown("**🛠️ Tech:** `AutoGPT` • `LangGraph` • `Python` • `FastAPI`")
        st.button("In Development", disabled=True)