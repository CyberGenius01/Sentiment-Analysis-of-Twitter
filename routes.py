from flask import render_template, redirect, flash, request, url_for
from model import app
from model.forms import SentimentForm
from model.NLP import sentimentAnalysis

@app.route('/')
def main_page():
    return render_template('base.html')

@app.route('/documentation')
def doc_page():
    return render_template('doc.html')

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    form = SentimentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_string = form.user_string.data
            return redirect(url_for('result_page', user_string=user_string))
    return render_template('home.html', form=form)

@app.route('/sentiment?', methods=['GET', 'POST'])
def result_page():
    user_string = str(request.args.get('user_string'))
    sentiment, clean_string = sentimentAnalysis(user_string)
    return render_template('result.html', sentiment=sentiment, clean_string=clean_string)