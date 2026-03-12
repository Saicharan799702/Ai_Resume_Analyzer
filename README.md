# AI Resume Analyzer (Resume–Job Matching System)

An AI-powered application that analyzes a candidate's resume and compares it with a given job description to evaluate how well the resume matches the job requirements.

This tool helps job seekers quickly understand their **resume match score**, identify **missing skills**, and get **actionable improvement suggestions**.

---

## Features

* Upload resume in **PDF format**
* Paste a **Job Description**
* AI analyzes the resume against the job requirements
* Generates:

  * **Match Score (0–100%)**
  * **Key Strengths**
  * **Missing Skills**
  * **Improvement Suggestions**
* Simple and interactive **Gradio Web Interface**

---

## Tech Stack

* **Python**
* **OpenAI API**
* **Gradio**
* **PyPDF**
* **Python-dotenv**

---

## 📂 Project Structure

```
AI_Resume_Analyzer/
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env (not uploaded to GitHub)
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Saicharan799702/Ai_Resume_Analyzer.git
cd Ai_Resume_Analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Setup Environment Variables

Create a `.env` file in the project root and add your OpenAI API key.

```
OPENAI_API_KEY=your_openai_api_key_here
```

**Important:**
Do NOT upload the `.env` file to GitHub.

---

## Run the Application

```
python main.py
```

The Gradio interface will launch in your browser.

---

## How It Works

1. User uploads their resume (PDF).
2. User pastes the job description.
3. The system extracts text from the resume.
4. OpenAI analyzes the resume against the job description.
5. The system returns a structured evaluation with insights.

---

## Example Output

```
Match Score: 78%

Key Strengths:
- Strong Python and SQL skills
- Experience with data analysis tools

Missing Skills:
- Cloud platforms (AWS, Azure)
- Advanced machine learning frameworks

Improvement Suggestions:
- Add cloud-related experience
- Highlight measurable project outcomes
```

---

## Use Cases

* Job seekers improving their resumes
* Resume screening tools
* HR tech prototypes
* AI-powered career tools

---

## Security Note

API keys are stored in a `.env` file and excluded from GitHub using `.gitignore`.

---

## Author

**Sai Charan**

B.Tech Computer Science Engineering Graduate
Interested in **AI, Data Analytics, and Generative AI applications**

GitHub:
https://github.com/Saicharan799702

---

## Support

If you like this project, please consider **starring the repository**.
