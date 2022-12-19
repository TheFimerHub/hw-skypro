from flask import Flask
from utils import load_candidates, load_candidate, get_by_skill

app = Flask(__name__)
@app.route("/")
def main():
    candidates = load_candidates()
    candidates_str = ''
    for candidate in candidates:
        candidate_str = f"Имя кандидата: {candidate['name']}\n" \
                        f"Позиция кандидата: {candidate['position']}\n" \
                        f"Навыки через запятую: {candidate['skills']}\n\n"
        candidates_str += candidate_str
        
    return f"<pre>{candidates_str}</pre>"


@app.route("/candidate/<int:pk>/")
def view_candidate(pk):
    candidate = load_candidate(pk)
    candidate_str = f"Имя кандидата: {candidate['name']}\n" \
                    f"Позиция кандидата: {candidate['position']}\n" \
                    f"Навыки через запятую: {candidate['skills']}\n\n"
    
    return f"<pre><img src=\"{candidate['picture']}\">\n{candidate_str}</pre>"

@app.route("/skills/<str:skill>/")
def view_candidates_skill(skill):
    candidates = get_by_skill(skill)
    candidates_str = ''
    for candidate in candidates:
        candidate_str = f"Имя кандидата: {candidate['name']}\n" \
                        f"Позиция кандидата: {candidate['position']}\n" \
                        f"Навыки через запятую: {candidate['skills']}\n\n"
        candidates_str += candidate_str
        
    return f"<pre>{candidates_str}</pre>"

app.run()
