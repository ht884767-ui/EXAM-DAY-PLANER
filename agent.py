from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
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

Output should include:
1. Time-blocked study plan (morning to night)
2. Revision + break schedule
3. Last-minute exam tips

Keep it clear and student-friendly.
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(
        subject=subject,
        exam_date=exam_date,
        weak_topics=weak_topics
    )
