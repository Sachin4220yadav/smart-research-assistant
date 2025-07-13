# smart-research-assistant



\# 🤖 Smart Research Assistant



An AI-powered assistant that can read and understand PDF/TXT documents, generate summaries, answer user questions, and create logic-based quizzes — all in your browser.



---



\## 📌 Features



\- 📄 Upload PDF/TXT files

\- 📝 Auto-generate concise summary (≤ 150 words)

\- 🧠 Ask free-form questions and get document-based answers with justification

\- 🎯 "Challenge Me" Mode: Generates 3 logic-based questions and evaluates your understanding

\- ⚡ Simple web interface using Streamlit



---



\## 🚀 How It Works



The app uses:



\- \*\*Flask\*\* backend for handling logic and document processing

\- \*\*Streamlit\*\* frontend for a responsive UI

\- \*\*Hugging Face Transformers\*\* (`facebook/bart-large-cnn`) for summarization

\- \*\*Sentence Transformers\*\* (`all-MiniLM-L6-v2`) for semantic Q\&A



---



\## 🛠️ Tech Stack



| Layer       | Tech                      |

|-------------|---------------------------|

| Frontend    | Streamlit                 |

| Backend     | Flask                     |

| NLP Models  | HuggingFace Transformers  |

| PDF Reading | PyPDF2                    |

| Q\&A Engine  | Sentence-Transformers     |



---



\## 🧪 Local Setup Instructions



1\. \*\*Clone the repo\*\*



```bash

git clone https://github.com/Sachin4220yadav/smart-research-assistant.git

cd smart-research-assistant



