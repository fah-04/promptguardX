import streamlit as st
import cohere
import os
from dotenv import load_dotenv
import json

# ✅ Load API Key from .env file
load_dotenv()
COHERE_API_KEY = os.getenv("W9pdBavE5hvV0dSIHNICP3j2rfH9gkZkGRl4JPCN")

# ✅ Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

st.set_page_config(page_title="PromptGuardian Pro", layout="wide")
st.title("🛡 PromptGuardian Pro – Real-Time Prompt Injection Detector")

st.markdown("### Enter your prompt below:")
user_prompt = st.text_area("Prompt", height=150)

if st.button("Analyze Prompt"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt to analyze.")
    else:
        with st.spinner("Analyzing using Cohere Command R+..."):
            try:
                system_prompt = (
                    "Given this prompt, classify if it's SAFE, SUSPICIOUS, or ATTACK. "
                    "Explain why, assign a risk score (0–100), and rewrite it safely if risky. "
                    "Respond in the following JSON format:\n"
                    "{\n"
                    "  \"classification\": \"Safe | Suspicious | Attack\",\n"
                    "  \"risk_score\": 0-100,\n"
                    "  \"explanation\": \"Explanation here\",\n"
                    "  \"rewrite\": \"Rewritten prompt here\"\n"
                    "}\n"
                    f"Prompt: {user_prompt}"
                )

                response = co.chat(
                    message=system_prompt,
                    model="command-r-plus",
                    temperature=0.2,
                    chat_history=[],
                    max_tokens=300
                )

                analysis = json.loads(response.text)

                classification = analysis.get("classification", "Unknown")
                risk_score = analysis.get("risk_score", 50)
                explanation = analysis.get("explanation", "N/A")
                rewrite = analysis.get("rewrite", user_prompt)

                st.subheader("🔍 Analysis Result")
                st.markdown(f"**Classification:** {classification}")
                st.markdown(f"**Risk Score:** {risk_score}/100")
                st.markdown(f"**Explanation:** {explanation}")
                st.progress(min(risk_score, 100))

                if classification != "Safe":
                    st.subheader("✅ Safe Rewritten Prompt")
                    st.code(rewrite, language='markdown')

            except Exception as e:
                st.error(f"Error analyzing prompt: {str(e)}")
