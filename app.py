import streamlit as st
import speech_recognition as sr
import time

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Emergency Help System",
    page_icon="🚨",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right, #141E30, #243B55);
}

/* Title */
.main-title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:white;
    margin-top:20px;
}

/* Subtitle */
.sub-title{
    text-align:center;
    font-size:24px;
    color:#dddddd;
    margin-bottom:40px;
}

/* Card */
.card{
    background: rgba(255,255,255,0.1);
    padding:40px;
    border-radius:25px;
    backdrop-filter: blur(12px);
    box-shadow:0px 0px 20px rgba(255,255,255,0.2);
}

/* Buttons */
.stButton>button{
    width:100%;
    height:60px;
    border-radius:15px;
    background:#ff4b4b;
    color:white;
    font-size:22px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#ff1e1e;
    color:white;
}

/* Text Input */
.stTextInput>div>div>input{
    height:55px;
    font-size:20px;
    border-radius:15px;
}

/* Footer */
.footer{
    text-align:center;
    color:white;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================

st.markdown(
    '<div class="main-title">🚨 AI Voice Emergency Help System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Smart AI-Based Emergency Detection Website</div>',
    unsafe_allow_html=True
)

# =========================================
# MAIN CARD
# =========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🎤 Voice or Text Emergency Detection")

st.write("You can detect emergency using voice OR text.")

# Emergency words
emergency_words = [
    "help",
    "help me",
    "emergency",
    "danger",
    "save me",
    "attack"
]

# =========================================
# TEXT DETECTION
# =========================================

st.markdown("## ✍ Text Detection")

user_text = st.text_input("Type Emergency Word")

if st.button("🔍 Detect Text Emergency"):

    text = user_text.lower()

    found = False

    for word in emergency_words:

        if word in text:
            found = True
            break

    if found:

        st.error("🚨 EMERGENCY DETECTED 🚨")

        st.warning("Emergency Alert Activated")

    else:

        st.success("✅ No Emergency Detected")

# =========================================
# VOICE DETECTION
# =========================================

st.markdown("---")

st.markdown("## 🎙 Voice Detection")

if st.button("🎤 START VOICE DETECTION"):

    recognizer = sr.Recognizer()

    try:

        # Fake AI listening effect
        with st.spinner("🎧 AI Listening..."):

            time.sleep(5)

        # Read recorded voice file
        with sr.AudioFile("voice.wav") as source:

            audio = recognizer.record(source)

            st.info("⚡ Recognizing Voice...")

            text = recognizer.recognize_google(audio)

            text = text.lower()

            st.success(f"📝 Detected Text: {text}")

            found = False

            for word in emergency_words:

                if word in text:
                    found = True
                    break

            if found:

                st.error("🚨 EMERGENCY DETECTED 🚨")

                st.warning("Emergency Alert Activated")

                st.balloons()

            else:

                st.success("✅ No Emergency Detected")

    except FileNotFoundError:

        st.error("voice.wav file not found")

    except sr.UnknownValueError:

        st.error("Voice not recognized")

    except Exception as e:

        st.error(f"Error: {e}")

# =========================================
# CLOSE CARD
# =========================================

st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# FOOTER
# =========================================

st.markdown(
    '<div class="footer">Developed using Streamlit + AI + Speech Recognition</div>',
    unsafe_allow_html=True
)