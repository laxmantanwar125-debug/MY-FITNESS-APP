import streamlit as st
import pandas as pd

# --- App Styling ---
st.set_page_config(page_title="Shera Fitness Pro", page_icon="💪")

# --- Dashboard Header ---
st.title("🏃 Shera Fitness Pro v2.0")
st.markdown("---")

# --- Sidebar: Goals & Profile ---
st.sidebar.header("🎯 Tera Target")
naam = st.sidebar.text_input("Naam:", "Shera")
goal = st.sidebar.slider("Daily Step Goal:", 5000, 20000, 10000)

# --- Today's Stats ---
col1, col2 = st.columns(2)
with col1:
    steps = st.number_input("Aaj kitne steps chale?", min_value=0, value=5000, step=100)
    st.metric("Steps Done", steps, f"{steps - goal} vs Goal")

with col2:
    calories = steps * 0.04
    st.metric("Calories Burned", f"{calories:.1f} kcal", "🔥")

# --- Progress Bar ---
progress = min(steps / goal, 1.0)
st.write(f"**Goal Progress: {int(progress * 100)}%**")
st.progress(progress)

if steps >= goal:
    st.balloons()
    st.success(f"Gazab {naam}! Tune aaj ka goal phod diya! 🎉")

# --- NEW: Workout Videos Section ---
st.markdown("---")
st.subheader("📺 Aaj ka Workout (YouTube)")
video_choice = st.selectbox("Kya exercise karni hai?", ["Full Body Workout", "Abs Workout", "Yoga for Beginners"])

if video_choice == "Full Body Workout":
    st.video("https://www.youtube.com/watch?v=ml6cT4AZdqI") # Example video
elif video_choice == "Abs Workout":
    st.video("https://www.youtube.com/watch?v=AnYl6Nk9GOA")
else:
    st.video("https://www.youtube.com/watch?v=v7AYKMP6rOE")

# --- NEW: Health Tips (Diet) ---
st.markdown("---")
st.subheader("🍎 Fitness Tips for You")
with st.expander("Diet Plan (Vajan ghatane ke liye)"):
    st.write("""
    1. **Subah:** 2-3 Ande ya Paneer sandwich.
    2. **Dopehar:** Dal, Chawal aur Salad (Salad zaroor khayein).
    3. **Shaam:** Green Tea aur thode se Makhane.
    4. **Raat:** Halki Roti aur Sabzi (Sone se 2 ghante pehle).
    """)

# --- Progress Chart ---
st.divider()
st.subheader("📊 Pichle 7 Din ki Mehnat")
data = pd.DataFrame({
    'Din': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [7000, 8500, 11000, 6000, 9500, 12000, steps]
})
st.bar_chart(data.set_index('Din'))

st.caption("Bhai, mehnat karte raho, result zaroor milega! 💪")
