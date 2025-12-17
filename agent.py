from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

def create_study_plan(subject, exam_date, weak_topics):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-8b-8192"
    )

    prompt = PromptTemplate(
        input_variables=["subject", "exam_date", "weak_topics"],
        template="""
You are an AI Study Buddy.

Create a focused exam-day study plan for:
Subject: {subject}
Exam Date: {exam_date}
Weak Topics: {weak_topics}

Include:
1. Time-blocked study plan
2. Revision and break schedule
3. Last-minute exam tips
"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "subject": subject,
        "exam_date": exam_date,
        "weak_topics": weak_topics
    })

    return response.content

