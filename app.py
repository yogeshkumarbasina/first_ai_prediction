from flask import Flask, render_template_string, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# =========================
# CREATE FLASK APP
# =========================

app = Flask(__name__)

# =========================
# TRAINING DATA
# =========================

texts = [

    # POSITIVE

    "I love this product",
    "This is amazing",
    "Very good experience",
    "Excellent app",
    "Fantastic work",
    "I am happy",
    "Absolutely wonderful",
    "Great customer service",
    "Very satisfied",
    "Best experience ever",
    "Highly recommended",
    "Amazing support team",
    "Perfect application",
    "Easy to use",
    "Superb performance",
    "Brilliant work",

    # NEGATIVE

    "Worst app ever",
    "I hate this",
    "Very bad service",
    "Terrible experience",
    "This is horrible",
    "I am disappointed",
    "Waste of money",
    "Worst customer support",
    "Very frustrating",
    "Awful performance",
    "This app is broken",

    # NEUTRAL

    "This is okay",
    "Average experience",
    "The app works fine",
    "Nothing special",
    "It is normal",
    "Service was acceptable",
    "It works as expected",
    "Basic functionality",
    "The app is usable",
    "The support was okay"
]

# =========================
# LABELS
# =========================

labels = [

    # POSITIVE

    "Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive",
    "Positive","Positive","Positive","Positive",

    # NEGATIVE

    "Negative","Negative","Negative","Negative",
    "Negative","Negative","Negative","Negative",
    "Negative","Negative","Negative",

    # NEUTRAL

    "Neutral","Neutral","Neutral","Neutral",
    "Neutral","Neutral","Neutral","Neutral",
    "Neutral","Neutral"
]

# =========================
# TEXT TO NUMBERS
# =========================

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

# =========================
# CREATE MODEL
# =========================

model = MultinomialNB()

# =========================
# TRAIN MODEL
# =========================

model.fit(X, labels)

# =========================
# HTML + CSS
# =========================

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>AI Sentiment Analyzer</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{

    height:100vh;

    display:flex;

    justify-content:center;

    align-items:center;

    font-family:Arial, sans-serif;

    background:linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #312e81,
        #0f172a
    );

    background-size:400% 400%;

    animation:bgAnimation 12s infinite ease;
}

@keyframes bgAnimation{

    0%{
        background-position:0% 50%;
    }

    50%{
        background-position:100% 50%;
    }

    100%{
        background-position:0% 50%;
    }
}

.container{

    width:500px;

    padding:40px;

    border-radius:25px;

    background:rgba(255,255,255,0.08);

    backdrop-filter:blur(18px);

    box-shadow:0 0 40px rgba(0,0,0,0.4);

    text-align:center;

    color:white;
}

h1{

    font-size:36px;

    margin-bottom:25px;

    color:#ffffff;
}

.subtitle{

    margin-bottom:20px;

    color:#cbd5e1;

    font-size:15px;
}

textarea{

    width:100%;

    height:140px;

    padding:15px;

    border:none;

    border-radius:15px;

    resize:none;

    outline:none;

    font-size:16px;

    background:rgba(255,255,255,0.15);

    color:white;

    transition:0.3s;
}

textarea:focus{

    box-shadow:0 0 15px #7c3aed;
}

textarea::placeholder{

    color:#dddddd;
}

button{

    width:100%;

    margin-top:20px;

    padding:15px;

    border:none;

    border-radius:15px;

    background:linear-gradient(
        135deg,
        #7c3aed,
        #2563eb
    );

    color:white;

    font-size:18px;

    font-weight:bold;

    cursor:pointer;

    transition:0.3s;
}

button:hover{

    transform:scale(1.03);

    box-shadow:0 0 20px #7c3aed;
}

.result{

    margin-top:25px;

    padding:18px;

    border-radius:15px;

    background:rgba(255,255,255,0.12);

    font-size:30px;

    font-weight:bold;
}

.positive{
    color:#22c55e;
}

.negative{
    color:#ef4444;
}

.neutral{
    color:#facc15;
}

.samples{

    margin-top:25px;

    text-align:left;

    color:#e2e8f0;

    font-size:14px;
}

.samples h3{

    margin-bottom:10px;
}

.samples p{

    margin-top:6px;
}

.footer{

    margin-top:30px;

    padding-top:15px;

    border-top:1px solid rgba(255,255,255,0.2);

    font-size:14px;

    color:#cbd5e1;

    line-height:1.8;
}

.name{

    font-size:16px;

    font-weight:bold;

    color:#ffffff;
}

</style>

</head>

<body>

<div class="container">

    <h1>🤖 AI Sentiment Analyzer</h1>

    <div class="subtitle">

        Analyze Positive, Negative and Neutral Sentiments using Machine Learning

    </div>

    <form method="POST">

        <textarea
        name="text"
        placeholder="Enter your text here..."
        required></textarea>

        <button type="submit">

            Analyze Sentiment

        </button>

    </form>

    {% if prediction %}

        <div class="result">

            {% if prediction == "Positive" %}

                <span class="positive">

                    😊 Positive

                </span>

            {% elif prediction == "Negative" %}

                <span class="negative">

                    😠 Negative

                </span>

            {% else %}

                <span class="neutral">

                    😐 Neutral

                </span>

            {% endif %}

        </div>

    {% endif %}

    <div class="samples">

        <h3>Sample Inputs</h3>

        <p>✅ I really love this app</p>
        <p>❌ Worst customer service ever</p>
        <p>😐 The application is okay</p>

    </div>

    <div class="footer">

        <div class="name">

            Developed by BASINA YOGESH KUMAR

        </div>

        📧 yogibasina07@gmail.com

    </div>

</div>

</body>

</html>

"""

# =========================
# HOME ROUTE
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""

    if request.method == "POST":

        user_text = request.form["text"]

        test_vector = vectorizer.transform([user_text])

        prediction = model.predict(test_vector)[0]

    return render_template_string(
        HTML,
        prediction=prediction
    )

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    app.run(debug=True)
