from flask import Flask, request, jsonify
from utils import read_pdf, read_txt
from summarizer import get_summary
from qa_engine import answer_question, generate_logic_questions

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename.endswith('.pdf'):
        text = read_pdf(file)
    else:
        text = read_txt(file)

    summary = get_summary(text)
    return jsonify({"summary": summary, "text": text})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    doc = data['doc']
    question = data['question']
    answer, idx = answer_question(doc, question)
    return jsonify({
        "answer": answer,
        "justification": f"This answer is based on sentence #{idx + 1}."
    })

@app.route('/challenge', methods=['POST'])
def challenge_mode():
    data = request.json
    doc = data['doc']
    questions = generate_logic_questions(doc)
    return jsonify({"questions": questions})

if __name__ == '__main__':
    app.run(debug=True)

