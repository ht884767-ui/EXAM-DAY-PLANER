import streamlit as st
from agent import create_study_plan

st.set_page_config(page_title="AI Study Buddy")

st.title("📚 AI Study Buddy – Exam Day Planner")

subject = st.text_input("Enter Subject")
exam_date = st.date_input("Exam Date")
weak_topics = st.text_area("Enter Weak Topics")

if st.button("Generate Study Plan"):
    if subject and weak_topics:
        with st.spinner("Generating study plan..."):
            result = create_study_plan(
                subject,
                str(exam_date),   # 🔥 FIX HERE
                weak_topics
            )
        st.success("Study Plan Ready!")
        st.write(result)
    else:
        st.warning("Please fill all fields.")

