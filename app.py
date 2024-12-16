from flask import Flask, render_template, request, redirect, flash
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

logging.info('Flask server started')

# Data storage using dictionaries
data = {"reviews": [], "positive": 0, "negative": 0}

@app.route("/")
def index():
    logging.info('========== Open home page ============')
    return render_template('index.html', data=data)

@app.route("/", methods=['POST'])
def my_post():
    text = request.form.get('text', '').strip()
    if not text:
        flash("Please enter a review!", "warning")
        logging.warning('Empty input received')
        return redirect(request.url)

    logging.info(f'Text : {text}')
    
    try:
        preprocessed_txt = preprocessing(text)
        logging.info(f'Preprocessed Text : {preprocessed_txt}')
        
        vectorized_txt = vectorizer(preprocessed_txt)
        logging.info(f'Vectorized Text : {vectorized_txt}')
        
        prediction = get_prediction(vectorized_txt)
        logging.info(f'Prediction : {prediction}')
        
        if prediction == 'negative':
            data['negative'] += 1
        else:
            data['positive'] += 1
        
        data['reviews'].insert(0, text)
        
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        flash("An error occurred during processing. Please try again.", "danger")
        return redirect(request.url)
    
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
