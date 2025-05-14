import streamlit as st

# ---------- BACKEND DATA (EDIT HERE) ----------
your_name = "Neduri Sri Ramya"
bio = "A Python Developer passionate about building helpful tools and web apps."
about = (
    "I'm a self-driven developer who enjoys crafting solutions that improve daily life. "
    "From emotional journaling tools to family tribute websites, my work is all about blending utility with empathy."
)
skills = ["Python", "Streamlit", "SQLite", "CSV Automation", "HTML/CSS", "CMD Tools","Data stuctures and algorithms","Database management systems"]

projects = [
    {
        "title": "Chitti Scheme Assistant",
        "desc": "A smart assistant for managing local chitti schemes with reminders and status tracking.",
        "link": "https://chitti-scheme-eynj3ianbye6qr4sijnwcm.streamlit.app/"
    },
    {
        "title": "Mother’s Day Tribute Website",
        "desc": "A heartfelt platform to honor moms with AI-generated captions, a wisdom wall, and digital keepsakes.",
        "link": "https://mothertributewebsite-edjfhg5kvuutne5en74mdq.streamlit.app/"
    },
    {
        "title": "Unspoken – Emotional Letter Vault",
        "desc": "A private journal-style app to write unshared, encrypted letters categorized by emotion.",
        "link": "https://unspoken-jscvegxhuhw3azpg4amuvg.streamlit.app/"
    }
]

email = "nedurisriramya@gmail.com"
linkedin = "https://www.linkedin.com/in/neduri-sri-ramya-4bb097257/"
github = "https://github.com/ramya231-tech"
# ------------------------------------------------


# ---------- STREAMLIT FRONTEND ----------
st.set_page_config(page_title="My Portfolio", page_icon="🧑‍💻", layout="wide")

# --- Header ---
with st.container():
    st.title(f"Hi, I'm {your_name} 👋")
    st.write(f"### {bio}")

# --- About Me ---
with st.container():
    st.subheader("About Me")
    st.write(about)

# --- Skills ---
with st.container():
    st.subheader("Skills")
    st.write(", ".join(skills))

# --- Projects ---
with st.container():
    st.subheader("Projects")
    st.write("Here are a few featured projects I've built using Python and Streamlit:")
    for proj in projects:
        st.markdown(f"**[{proj['title']}]({proj['link']})**  \n{proj['desc']}  \n")

# --- Contact ---
with st.container():
    st.subheader("Contact Me")
    st.write("Feel free to connect or reach out via the following channels:")
    st.write(f"📧 Email: {email}")
    st.write(f"🔗 LinkedIn: [{linkedin}]({linkedin})")
    st.write(f"💻 GitHub: [{github}]({github})")

# --- Footer ---
st.markdown("---")
st.caption(f"© 2025 {your_name}. All rights reserved.")
