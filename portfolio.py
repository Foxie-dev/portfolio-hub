import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Tina | AI Portfolio", layout="wide")

# 2. Sidebar / About Me
with st.sidebar:
    st.title("Tina")
    st.subheader("AI Solutions Architect")
    st.write("Building the bridge between complex data and simple, powerful AI tools.")
    st.divider()
    st.write("📧 contact@yourdomain.com")
    st.write("[LinkedIn](#) | [GitHub](#)")

# 3. Hero Section
st.title("Project Portfolio")
st.write("Explore my latest AI agents and web applications.")

# 4. Project Gallery (The Grid)
col1, col2 = st.columns(2)

with col1:
    st.container(border=True)
    # This line now looks for the file in your folder!
    st.image("ai_screenshot.png") 
    st.subheader("Market Intelligence AI")
    st.write("A RAG-powered assistant analyzing financial reports with citations.")
    # Add your real live app URL here
    st.link_button("Launch AI App", "https://ai-market-intelligence-app-r58mtkgg7ojsnfbehb9ubk.streamlit.app/")


# 5. Coming Soon Section
st.divider()
st.subheader("🚀 Coming Soon")
st.info("AI Lead-Gen Agent: Automatically researching competitors and generating sales decks.")