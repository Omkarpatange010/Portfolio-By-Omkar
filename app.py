from flask import Flask, render_template, request, redirect, url_for, flash
import datetime

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects = [
        {'name': 'Weather App', 'desc': 'Displays live weather data using OpenWeather API.'},
        {'name': 'Expense Tracker', 'desc': 'Track your daily expenses and generate reports.'},
        {'name': 'Chat App', 'desc': 'Simple chat app using Python sockets.'}
    ]
    return render_template('projects.html', projects=projects)

@app.route('/blog')
def blog():
    posts = [
        {'title': 'Getting Started with Flask', 'date': '2025-10-10', 'content': 'Learn Flask basics and routing.'},
        {'title': 'Deploy Flask Apps', 'date': '2025-10-12', 'content': 'Guide to deploying Flask on Render and Heroku.'}
    ]
    return render_template('blog.html', posts=posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with open("messages.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {name} ({email}): {message}\n")

        flash("Thank you for contacting me! I’ll get back to you soon.")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
