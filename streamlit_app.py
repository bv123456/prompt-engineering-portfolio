import streamlit as st
import openai

st.set_page_config(page_title="Resume Optimizer", page_icon="📝")

st.title("📝 AI Resume Optimizer")
st.markdown("Use GPT-4 to rewrite raw experience into strong resume bullet points.")

# Input API key
openai_api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# Input resume content
raw_experience = st.text_area("Paste your raw job experience:", height=200, placeholder="e.g. Worked at ABC Corp. Did sales, hit goals, talked to clients...")

# Prompt logic
def optimize_resume(raw_text, api_key):
    prompt = (
        "You're a professional resume writer. Given the raw experience below, "
        "write a clean resume bullet point using active verbs and metrics where possible. "
        "Keep the tone formal.

"
        f"Raw experience:
{raw_text}"
    )
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Generate result
if st.button("Optimize Resume"):
    if not openai_api_key or not raw_experience.strip():
        st.warning("Please enter both your API key and some raw experience.")
    else:
        result = optimize_resume(raw_experience, openai_api_key)
        st.subheader("Optimized Bullet Point:")
        st.success(result)
