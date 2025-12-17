import streamlit as st
from agent import create_study_plan
import os

st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("📚 AI Study Buddy – Exam Day Planner")

st.write("Generate a smart study plan using AI")

subject = st.text_input("Enter Subject")
exam_date = st.date_input("Exam Date")
weak_topics = st.text_area("Enter Weak Topics (comma separated)")

if st.button("Generate Study Plan"):
    if subject and weak_topics:
        with st.spinner("Creating your study plan..."):
            result = create_study_plan(subject, exam_date, weak_topics)
        st.success("Study Plan Generated!")
        st.write(result)
    else:
        st.warning("Please fill all fields.")
