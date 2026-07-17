!pip -q install google-genai gradio

from google import genai
import gradio as gr

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(api_key="")

# -----------------------------
# Blog Generator Function
# -----------------------------
def generate_blog(topic, audience, tone, words, language):

    prompt = f"""
You are a professional blog writer.

Write a {words}-word blog in {language}.

Topic: {topic}

Target Audience: {audience}

Tone: {tone}

The blog should include:

1. An engaging title
2. Introduction
3. Main Content
4. Real-world examples (if applicable)
5. Interesting facts
6. Tips or best practices
7. Conclusion
8. A motivational closing statement

The blog should be informative, easy to read, and well-formatted using headings and bullet points where appropriate.
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
    fn=generate_blog,

    inputs=[
        gr.Textbox(
            label="Blog Topic",
            placeholder="Example: Artificial Intelligence"
        ),

        gr.Textbox(
            label="Target Audience",
            placeholder="Example: Students, Developers, Beginners"
        ),

        gr.Dropdown(
            ["Professional", "Casual", "Technical", "Inspirational", "Funny"],
            value="Professional",
            label="Writing Tone"
        ),

        gr.Slider(
            minimum=200,
            maximum=1500,
            value=500,
            step=100,
            label="Word Count"
        ),

        gr.Dropdown(
            ["English", "Telugu", "Hindi", "Tamil", "Kannada", "Malayalam"],
            value="English",
            label="Language"
        )
    ],

    outputs=gr.Markdown(),

    title="📝 AI Blog Generator",

    description="Generate high-quality blogs using Gemini AI."
)

demo.launch()
