import streamlit as st
import PyPDF2
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# ✅ Use cache to avoid re-downloading models every time
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@st.cache_resource
def load_qa_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# Load models
summarizer = load_summarizer()
qa_model = load_qa_model()

# Page config
st.set_page_config(page_title="Smart Research Assistant", layout="centered")
st.title("📄 Smart Research Assistant")

st.info("✅ App loaded successfully. Upload a document to begin.")

# 🧾 Read text from PDF or TXT
def read_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages)
    else:
        return file.read().decode("utf-8")

# 📝 Summarize the text
def get_summary(text):
    text = text[:4000]  # limit to avoid model overload
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

# ❓ Find best matching answer
def get_best_answer(document, question):
    sentences = document.split('. ')
    sentence_embeddings = qa_model.encode(sentences, convert_to_tensor=True)
    question_embedding = qa_model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(question_embedding, sentence_embeddings)[0]
    best_index = scores.argmax().item()
    return sentences[best_index], best_index

# 🎯 Logic-based questions
def generate_challenge_questions():
    return [
        "What is the main objective of this document?",
        "Mention one important detail discussed.",
        "What conclusion or summary does the document provide?"
    ]

# 📁 Upload Document
uploaded_file = st.file_uploader("📁 Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Reading document..."):
        full_text = read_text(uploaded_file)
        st.session_state["doc"] = full_text
        summary = get_summary(full_text)
        st.session_state["summary"] = summary

    st.subheader("📝 Auto Summary")
    st.success(summary)

# 🧠 Ask Anything Mode
if "doc" in st.session_state:
    st.subheader("🧠 Ask Anything")
    user_question = st.text_input("Ask a question based on the document:")

    if user_question:
        with st.spinner("Searching for the answer..."):
            answer, idx = get_best_answer(st.session_state["doc"], user_question)
            st.markdown(f"**Answer:** {answer}")
            st.caption(f"📌 Based on sentence #{idx + 1}")

# 🧪 Challenge Me Mode
if "doc" in st.session_state:
    st.subheader("🎯 Challenge Me")
    if st.button("Generate 3 Logic-Based Questions"):
        questions = generate_challenge_questions()
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Q{i}: {q}**")
            st.text_input(f"Your Answer {i}:", key=f"user_ans_{i}")
            st.caption("💡 Reflect and compare your answer manually.")
