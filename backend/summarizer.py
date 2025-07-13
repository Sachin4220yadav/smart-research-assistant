from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_summary(text):
    text = text[:4000]  # Limit text length to avoid overload
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

