import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Load environment variables
load_dotenv()

def LLM_Setup(prompt):
    """Sets up the LLM model and generates a response based on the prompt."""
    model = ChatGroq(
        model="llama-3.2-1b-preview",
        groq_api_key=os.getenv('Classroom')
    )
    parser = StrOutputParser()
    output = model | parser
    output = output.invoke(prompt)
    return output

# Streamlit App
st.title('Comprehensive Lesson Plan Generator')
st.markdown(
    """
    Welcome to the **Comprehensive Lesson Plan Generator**! 
    Input your subject, topic, grade, and other details, and get a **complete, self-sufficient lesson plan** 
    designed to be used directly for teaching or self-study.
    """
)

# Input fields
subject = st.text_input(label='Subject (e.g., Science, Math)', placeholder='Enter the subject here...')
topic = st.text_input(label='Topic (e.g., The Solar System, Fractions)', placeholder='Enter the topic here...')
grade = st.text_input(label='Grade (e.g., 5th, 10th)', placeholder='Enter the grade level...')
duration = st.text_input(label='Duration (e.g., 1 hour, 90 minutes)', placeholder='Enter duration...')
learning_objectives = st.text_area(
    label='Learning Objectives',
    placeholder='E.g., Students will understand the properties of planets, their order, and key features.'
)
customization = st.text_area(
    label='Customization (Optional)',
    placeholder='E.g., Add diagrams, real-life examples, interactive activities, or quizzes.'
)

if st.button('Generate Complete Lesson Plan'):
    if not subject or not topic or not grade or not duration or not learning_objectives:
        st.warning('Please fill out all required fields to generate the lesson plan.')
    else:
        # Enhanced and structured prompt for LLM
        prompt = (
            f"Generate a detailed, structured, and **self-sufficient lesson plan** for teaching '{topic}' "
            f"in '{subject}' for grade {grade}. "
            f"Ensure the lesson is designed for a duration of {duration}. "
            f"The lesson should be comprehensive enough for students to fully understand the topic without needing "
            f"additional resources. "
            f"\n\nThe lesson plan should include the following sections:"
            f"\n\n1. **Introduction**: Start with an engaging activity, real-world connection, or question to introduce the topic."
            f"\n2. **Learning Objectives**: Clearly outline what students will learn."
            f"\n3. **Detailed Explanation**: A step-by-step, in-depth explanation of the topic in simple language."
            f"\n4. **Interactive Activities**: Include exercises, experiments, or group tasks to reinforce learning."
            f"\n5. **Examples and Practice**: Provide examples and questions with step-by-step solutions."
            f"\n6. **Assessment**: Include a short quiz or exercises to evaluate understanding."
            f"\n7. **Conclusion**: Summarize the topic with a real-life application or thought-provoking question."
            f"\n\nCustomization requested: {customization}."
            f"Format the response in Markdown for easy reading."
        )

        # Generate the output
        llm_output = LLM_Setup(prompt)
        st.markdown("### Generated Comprehensive Lesson Plan:")
        st.markdown(llm_output)


