import streamlit as stimport streamlit as st
import pandas as pd
import plotly.express as px

# --- App Settings ---
st.set_page_config(page_title="Shera Fitness Pro", page_icon="🏋️‍♂️", layout="wide")

# --- Simple Styling (Error Free) ---
st.markdown("### 🏃 Tera Personal Fitness Tracker")

# --- Sidebar: User Profile ---
st.sidebar.header("👤 Tera Profile")
naam = st.sidebar.text_input("Naam:", "Shera")
weight = st.sidebar.number_input("Wazan (kg):", 40, 200, 75)
height = st.sidebar.number_input("Height (cm):", 100, 250, 175)
goal_steps = st.sidebar.slider("Steps Goal:", 2000, 20000, 10000)

# BMI Logic
bmi = weight / ((height/100)**2)
st.sidebar.info(f"Tera BMI: {bmi:.1f}")

# --- Main Dashboard ---
st.title(f"🚀 {naam}'s Fitness Command Center")

# Row 1: Quick Stats
col1, col2, col3 = st.columns(3)

with col1:
    steps = st.number_input("Steps Chale:", 0, 50000, 5000)
    st.metric("Total Steps", f"{steps}", f"{steps - goal_steps} vs Goal")

with col2:
    water = st.slider("Glass Paani (250ml):", 0, 20, 8)
    st.metric("Water Intake", f"{water * 0.25}L")

with col3:
    calories_burned = steps * 0.04
    st.metric("Burned", f"{calories_burned:.0f} kcal")

# --- Progress Graph ---
st.subheader("📊 Pichle 7 Din ki Mehnat")
chart_data = pd.DataFrame({
    'Din': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [7200, 9100, 11500, 5000, 8800, 13000, steps]
})
st.line_chart(chart_data.set_index('Din'))

# --- Food Logger ---
st.divider()
st.subheader("🍎 Khane Peene ka Hisaab")
food_item = st.text_input("Kya khaya?", "Ande aur Bread")
if st.button("Add Meal ➕"):
    st.success(f"{food_item} save ho gaya!")

if steps >= goal_steps:
    st.balloons()
    st.success("Bhai tune toh phod diya! Goal Poora! 🎉")
import pandas as pd
import plotly.express as px

# --- App Styling ---
st.set_page_config(page_title="Shera Fitness Pro", page_icon="🏋️‍♂️", layout="wide")

# Custom CSS for look and feel
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_label_with_html=True)

# --- Sidebar: User Profile ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/236/236831.png", width=100)
st.sidebar.header("👤 Tera Profile")
naam = st.sidebar.text_input("Naam:", "Shera")
weight = st.sidebar.number_input("Wazan (kg):", 40, 200, 75)
height = st.sidebar.number_input("Height (cm):", 100, 250, 175)
goal_steps = st.sidebar.slider("Steps Goal:", 2000, 20000, 10000)

# BMI Logic
bmi = weight / ((height/100)**2)
st.sidebar.info(f"Tera BMI: {bmi:.1f}")

# --- Main Dashboard ---
st.title(f"🚀 {naam}'s Fitness Command Center")
st.divider()

# Row 1: Quick Stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    steps = st.number_input("Steps Chale:", 0, 50000, 5000)
    st.metric("Total Steps", steps, delta=f"{steps - goal_steps} vs Goal")

with col2:
    water = st.slider("Glass Paani (250ml):", 0, 20, 8)
    st.metric("Water Intake", f"{water * 0.25}L")

with col3:
    calories_burned = steps * 0.04
    st.metric("Burned", f"{calories_burned:.0f} kcal", "🔥")

with col4:
    sleep = st.number_input("Sleep (Hours):", 0, 24, 8)
    st.metric("Recovery", f"{sleep} hrs", "😴")

# --- Progress Graph ---
st.divider()
st.subheader("📊 Pichle 7 Din ki Mehnat")

# Sample Data for Graph
chart_data = pd.DataFrame({
    'Din': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [7200, 9100, 11500, 5000, 8800, 13000, steps],
    'Target': [goal_steps] * 7
})

fig = px.line(chart_data, x='Din', y=['Steps', 'Target'], 
              title="Step Trend vs Goal", markers=True,
              color_discrete_map={"Steps": "#00CC96", "Target": "#EF553B"})
st.plotly_chart(fig, use_container_width=True)

# --- Food Logger Section ---
st.divider()
st.subheader("🍎 Khane Peene ka Hisaab")
c1, c2 = st.columns(2)

with c1:
    meal = st.selectbox("Kaunsa Meal?", ["Breakfast", "Lunch", "Snacks", "Dinner"])
    food_item = st.text_input("Kya khaya?", "Ande aur Bread")
    calories_in = st.number_input("Calories (Approx):", 0, 2000, 300)
    if st.button("Add Meal ➕"):
        st.success(f"{food_item} add ho gaya!")

with c2:
    # Macro Pie Chart (Visual representation)
    macros = pd.DataFrame({
        'Nutrient': ['Protein', 'Carbs', 'Fats'],
        'Value': [30, 50, 20]
    })
    fig_pie = px.pie(macros, values='Value', names='Nutrient', title="Macros Balance", hole=.3)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- Motivational Quote ---
st.divider()
st.info("💡 **Tip:** Bhai, consistent rehna hi asli fitness hai. Kal fir milte hain!")

if steps >= goal_steps:
    st.balloons()
