from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for resume form submission
@app.route('/build', methods=['POST'])
def build_resume():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    summary = request.form['summary']
    experience = request.form['experience']

    # Render the resume template with the provided data
    return render_template('resume.html', name=name, email=email, phone=phone, summary=summary, experience=experience)

if __name__ == '__main__':
    app.run(debug=True)
