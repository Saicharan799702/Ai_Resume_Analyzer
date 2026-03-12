import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Extract text from PDF
def extract_resume_text(file):
    reader = PdfReader(file.name)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# Evaluate resume
def evaluate_resume(resume_file, job_description):
    try:
        resume_text = extract_resume_text(resume_file)

        prompt = f"""
        You are an expert HR recruiter.

        Analyze the following resume against the job description.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Provide response strictly in this format:

        Match Score (0-100%):
        Key Strengths:
        Missing Skills:
        Improvement Suggestions:
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# UI
with gr.Blocks(title="AI Resume Matcher") as demo:

    gr.Markdown("# 🚀 AI Resume–Job Matching System")
    gr.Markdown("Upload your resume and compare with job description.")

    resume_input = gr.File(label="Upload Resume (PDF)")
    jd_input = gr.Textbox(label="Paste Job Description", lines=8)

    evaluate_btn = gr.Button("Evaluate Match")

    output = gr.Textbox(label="AI Evaluation Result", lines=15)

    evaluate_btn.click(
        evaluate_resume,
        inputs=[resume_input, jd_input],
        outputs=output
    )

demo.launch(share=True)