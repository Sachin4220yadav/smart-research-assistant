from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def answer_question(document, user_question):
    sentences = document.split('. ')
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
    question_embedding = model.encode(user_question, convert_to_tensor=True)

    scores = util.cos_sim(question_embedding, sentence_embeddings)[0]
    best_match_index = scores.argmax()
    return sentences[best_match_index], best_match_index

def generate_logic_questions(text):
    return [
        "What is the main objective of this document?",
        "Mention one important detail discussed.",
        "What conclusion or summary does the document provide?"
    ]

