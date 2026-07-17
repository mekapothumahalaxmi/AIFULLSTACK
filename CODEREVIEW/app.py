!pip -q install google-genai gradio

from google import genai
import gradio as gr

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(api_key="")

# -----------------------------
# Code Review Function
# -----------------------------
def review_code(language, code):

    prompt = f"""
You are an expert Software Engineer and Code Reviewer.

Review the following {language} code.

Code:
{code}

Provide your review in the following format:

1. Overall Rating (out of 10)

2. Summary

3. Strengths

4. Issues Found
   - Syntax Errors
   - Logic Errors
   - Performance Issues
   - Security Issues
   - Code Smells

5. Best Practices

6. Suggestions for Improvement

7. Optimized Version of the Code

8. Final Verdict
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# -----------------------------
# Gradio Interface
# -----------------------------
demo = gr.Interface(
    fn=review_code,

    inputs=[
        gr.Dropdown(
            [
                "Python",
                "Java",
                "C",
                "C++",
                "JavaScript",
                "HTML",
                "CSS",
                "SQL",
                "Go",
                "Rust"
            ],
            value="Python",
            label="Programming Language"
        ),

        gr.Textbox(
            lines=20,
            label="Paste Your Code Here",
            placeholder="Paste your source code..."
        )
    ],

    outputs=gr.Markdown(),

    title="💻 AI Code Review Assistant",

    description="Review your code using Gemini AI. Get bug detection, optimization suggestions, best practices, and an improved version of your code."
)

demo.launch()
