from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import datetime
import os
import logging

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-me-in-prod")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Email Configuration (read from environment for deployment safety)
# Set these environment variables in your deployment platform (GCP, AWS, Render, etc.)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
# Flask-Mail expects boolean values; environment variables are strings so check common truthy values
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'True').lower() in ('1', 'true', 'yes')
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL', 'False').lower() in ('1', 'true', 'yes')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = (
    os.environ.get('MAIL_DEFAULT_NAME', 'Portfolio Contact'),
    os.environ.get('MAIL_DEFAULT_SENDER', app.config.get('MAIL_USERNAME', ''))
)

# Helpful dev option: when True, sending is suppressed (useful for CI/local)
app.config['MAIL_SUPPRESS_SEND'] = os.environ.get('MAIL_SUPPRESS_SEND', 'False').lower() in ('1', 'true', 'yes')

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
            if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
                # Do not attempt to send if credentials are missing
                logger.warning("Mail credentials not configured; skipping send.")
                flash("Message saved — email not sent because mail is not configured.", "warning")
            else:
                msg = Message(
                    subject=f"Portfolio Contact: {name}",
                    recipients=[os.environ.get('CONTACT_RECIPIENT', app.config.get('MAIL_USERNAME'))],
                    body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
                )
                mail.send(msg)
                flash("✅ Message sent successfully!", "success")
        except Exception as e:
            # Log full traceback server-side, but show a friendly message to the user
            logger.exception("Error sending email")
            flash("❌ Error sending email. The message was saved locally.", "danger")

        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == "__main__":
    # Allow turning debug on with env var for local testing
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ('1', 'true', 'yes')
    # Optional test route only available in debug mode
    @app.route('/_email_test')
    def _email_test():
        # Endpoint to trigger a test email; only available in debug or when explicitly allowed in prod
        allow = debug_mode or os.environ.get('ALLOW_EMAIL_TEST', 'False').lower() in ('1', 'true', 'yes')
        if not allow:
            return ("Not allowed", 403)
        if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
            return ("Mail not configured", 400)
        try:
            m = Message(subject="Test email from Portfolio",
                        recipients=[os.environ.get('CONTACT_RECIPIENT', app.config.get('MAIL_USERNAME'))],
                        body='This is a test email from your portfolio app')
            mail.send(m)
            return ("Test email sent", 200)
        except Exception as e:
            logger.exception('Failed to send test email')
            return (f"Error sending test email: {e}", 500)

    app.run(host='0.0.0.0', debug=debug_mode)
