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


# Create two columns for your two projects
col1, col2 = st.columns(2)

with col1:
    st.container(border=True)
    st.image("ai_screenshot.png")
    st.subheader("Market Intelligence AI")
    st.write("A RAG-powered assistant for financial report analysis.")
    # Use your real Streamlit RAG link here
    st.link_button("Launch AI App", "https://your-real-rag-link.streamlit.app")

with col2:
    with st.container(border=True): # Added 'with' so items stay inside
        st.image("grooming_screenshot.png") 
        st.subheader("Grooming Booking System")
        st.write("A full-stack booking platform for pet grooming services.")
        # Ensure these are aligned with the st.write above
        st.link_button("View on Vercel", "https://dog-grooming-booking.vercel.app/")

# 5. Project 3 Section (Replacing Coming Soon)
st.divider()
st.subheader("🌍 AI Lead-Intelligence Scout")

with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # You can add a screenshot here later
        st.image("https://images.unsplash.com/photo-1551288049-bbda38a5f85d?auto=format&fit=crop&q=80&w=400") 
        
    with col2:
        st.write("""
        A multi-agent AI system built with **CrewAI** that automates B2B research. 
        - **Financial Auditing:** Scrapes Allabolag.se for real-time Swedish revenue data.
        - **Contact Discovery:** Finds names/titles for CEOs and Sustainability Managers.
        - **Alignment Analysis:** Summarizes how companies fit specific social impact missions.
        """)
        
        # Replace with your actual live Streamlit link
st.link_button("Launch AI Scout", "https://universal-social-impact-lead-gen-qngbjvmc4toqyhuwe34au3.streamlit.app/")
        st.link_button("View Code", "https://github.com/Foxie-dev/Universal-Social-Impact-Lead-Gen")