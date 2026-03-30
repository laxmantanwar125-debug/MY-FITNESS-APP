import streamlit as st
import pandas as pd

# App ka Title
st.title("🏃 Shera Fitness Tracker")

# User Input
naam = st.sidebar.text_input("Tera Naam:", "Shera")
steps = st.number_input("Aaj kitne steps chale?", min_value=0, value=5000)

# Calculation
calories = steps * 0.04
goal = 10000
progress = min(steps / goal, 1.0)

# Display Metrics
st.metric("Steps", steps)
st.metric("Calories Burned", f"{calories:.1f} kcal")

# Progress Bar
st.write(f"Goal Progress: {int(progress * 100)}%")
st.progress(progress)

# Graph
st.subheader("📊 Weekly Progress")
data = pd.DataFrame({
    'Din': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [7000, 8500, 11000, 6000, 9500, 12000, steps]
})
st.line_chart(data.set_index('Din'))

if steps >= goal:
    st.balloons()
    st.success("Mubarak ho bhai! Goal Poora! 🎉")
