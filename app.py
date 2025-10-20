from flask import Flask, render_template, request, redirect, url_for, flash

from flask_mail import Mail, Message
import datetime

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'login':
            username = request.form.get('username')
            password = request.form.get('password')
            # (Validate credentials here)
            if username == 'admin' and password == 'password':
                return redirect(url_for('index'))
            else:
                error = 'Invalid username or password'
        elif action == 'signup':
            return redirect(url_for('signup'))
        elif action == 'forgot':
            return redirect(url_for('forgot_password'))
    return render_template('login.html', error=error)

@app.route('/signup')
def signup():
    return "Sign Up page here"

@app.route('/forgot_password')
def forgot_password():
    return "Forgot Password page here"

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)
app.secret_key = "mysecretkey"

# --------------------------
# Email Configuration
# --------------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'omkarpatange77@gmail.com'   # your Gmail ID
app.config['MAIL_PASSWORD'] = 'bepr halo unhk ycsz'        # Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = ('Omkar Portfolio', 'omkarpatange77@gmail.com')

mail = Mail(app)

# --------------------------
# Routes
# --------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    projects = [
        {
            'title': 'Photography Management System',
            'desc': 'Developed a comprehensive photography management system using Flask and SQLite. Integrated AWS EC2 and CloudWatch for scalable hosting and monitoring.'
        },
        {
            'title': 'Fashion Hub E-commerce Platform',
            'desc': 'Created a responsive e-commerce site for fashion products with HTML, CSS, and JS — implemented cart and product management.'
        },
        {
            'title': 'Spotify & Netflix Clones',
            'desc': 'Built interactive UI clones of popular streaming platforms to enhance frontend skills using HTML, CSS, and JS.'
        }
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
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        message_body = request.form.get("message", "")

        # ✅ Save to local log file
        with open("messages.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {name} ({email}): {message_body}\n")

        # ✅ Send Email
        try:
            msg = Message(
                subject=f"Portfolio Contact: {name}",
                recipients=['omkarpatange77@gmail.com'],  # receive here
                body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
            )
            mail.send(msg)
            flash("✅ Message sent successfully! I'll get back to you soon.", "success")
        except Exception as e:
            flash(f"❌ Error sending email: {e}", "danger")

        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
