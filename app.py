from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import datetime

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'omkarpatange77@gmail.com'
app.config['MAIL_PASSWORD'] = 'bepr halo unhk ycsz'
app.config['MAIL_DEFAULT_SENDER'] = ('Omkar Portfolio', 'omkarpatange77@gmail.com')

mail = Mail(app)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = [
        {'title': 'Getting Started with Flask', 'date': '2025-10-10', 'content': 'Learn Flask basics and routing.'},
        {'title': 'Deploy Flask Apps', 'date': '2025-10-12', 'content': 'Guide to deploying Flask on Render and Heroku.'}
    ]
    return render_template('blog.html', posts=posts)

@app.route('/projects')
def projects():
    projects = [
        {'title': 'Photography Management System',
         'Duration': '02/2025 - 05/2025',
         'desc': 'Developed a comprehensive photography management system using Flask and SQLite. Integrated AWS EC2 and CloudWatch for scalable hosting and monitoring.',
         'link': 'https://github.com/Omkarpatange010/Wedding-Photography'},
        {'title': 'Fashion Hub E-commerce Platform',
         'Duration': '06/2024 - 01/2025',
         'desc': 'Created a responsive e-commerce site for fashion products with HTML, CSS, and JS — implemented cart and product management.',
         'link': 'https://github.com/Omkarpatange010/omkar-devops-private-repo'},
        {'title': 'Spotify & Netflix Clones',
         'Duration': '02/2025 - 05/2024',
         'desc': 'Built interactive UI clones using HTML, CSS, and JS.',
         'link': 'https://github.com/Omkarpatange010/spotify-clone-minimal/tree/main/Spotify'},
        {'title': 'My Portfolio Suite',
         'Duration': '06/2025 - 10/2025',
         'desc': 'Full-stack portfolio website built using Flask, integrated with email alerts, and hosted on AWS.',
         'link': 'https://github.com/Omkarpatange010/Portfolio-By-Omkar'}
    ]
    return render_template('projects.html', projects=projects)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        message_body = request.form.get("message", "")

        # Save message
        with open("messages.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {name} ({email}): {message_body}\n")

        try:
            msg = Message(
                subject=f"Portfolio Contact: {name}",
                recipients=['omkarpatange77@gmail.com'],
                body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
            )
            mail.send(msg)
            flash("✅ Message sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error sending email: {e}", "danger")

        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
