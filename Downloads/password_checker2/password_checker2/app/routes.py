from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.model_loader import load_model
from app.utils import evaluate_password

app = Blueprint('routes', __name__)
model = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        strength, suggestions = evaluate_password(password, model)

        if strength == 'Weak':
            flash("Password too weak! Suggestions: " + ', '.join(suggestions), 'danger')
            return render_template('login.html')
        elif strength == 'Medium':
            flash("Password is okay, but could be stronger. Suggestions: " + ', '.join(suggestions), 'warning')
            return render_template('login.html')
        else:
            return redirect(url_for('routes.result', status='strong'))

    return render_template('login.html')

@app.route('/result')
def result():
    status = request.args.get('status', 'unknown')
    return render_template('result.html', status=status)
