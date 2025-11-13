# 🧑‍💻 Portfolio Website (Flask + Cloud Deployment)

📘 Overview

This project is a personal portfolio website built using the Flask framework (Python).
It showcases your skills, projects, certifications, blog, and includes a contact form integrated with email functionality.
The application demonstrates modern web development practices along with optional cloud hosting using AWS EC2 .

# 🧩 Features 
✅ Home Page with Navigation
A clean, responsive landing page that introduces the user to your portfolio.
Includes an intuitive navigation bar linking to all major sections — About, Projects, Blog, and Contact.

✅ About Me Page
Provides a detailed overview of your background, education, cloud expertise, and DevOps skills.
Built as a separate HTML page using Flask routing (/about) to ensure modularity and scalability.

✅ Projects Showcase
Displays your personal and academic projects with titles, short descriptions, and key technologies used.
Each project entry demonstrates your practical skills in Flask, AWS, and web development.

✅ Blog Section
A dynamic section where you can publish short technical articles or learning reflections.
Helps you demonstrate your writing, documentation, and conceptual understanding of IT topics.

✅ Contact Form (with Email or File Storage Option)
Interactive form for visitors to reach out directly.
Uses Flask-Mail for automated email delivery or stores messages locally in a text file (messages.txt) as backup.

✅ Certification Section (with Swiper.js)
Visually engaging slider to display professional certificates such as AWS, Python, and Node.js.
Implemented using Swiper.js, a responsive and touch-friendly JavaScript library for smooth transitions.

✅ Cloud Deployment-Ready
The project can be easily deployed on AWS EC2, Render, or Vercel.
Demonstrates your understanding of real-world hosting environments and scalable infrastructure setup.

✅ Responsive and Simple Design
Designed with mobile-first principles using clean CSS.
Ensures compatibility across all devices and browsers while maintaining readability and aesthetics.

| Category                 | Tools / Technologies                               |
| ------------------------ | -------------------------------------------------- |
| **Language**             | Python, HTML, CSS, JavaScript                      |
| **Framework**            | Flask                                              |
| **Templating Engine**    | Jinja2                                             |
| **Styling**              | Custom CSS, Swiper.js (for certification carousel) |
| **Backend Mail Service** | Flask-Mail                                         |
| **Database (Optional)**  | SQLite                                             |
| **Cloud Deployment**     | AWS EC2, Render, or Vercel                         |
| **Version Control**      | Git, GitHub, Bitbucket                             |
| **DevOps Practices**     | CI/CD, Cloud Hosting, Version Control              |

## 📁 Project Structure

Portfolio-By-Omkar/ <br>
│ <br>
├── app.py <br>
├── requirements.txt<br>
├── README.md<br>
│<br>
├── templates/<br>
│   ├── index.html<br>
│   ├── about.html<br>
│   ├── projects.html<br>
│   ├── contact.html<br>
│   └── blog.html<br>
│<br>
├── static/<br>
│   ├── css/<br>
│   │   └── style.css<br>
│   └── img/<br>
│       ├── NodeJs.jpg<br>
│       ├── Python.jpg<br>
│       ├── AWS.jpg<br>
│       └── profile.jpg<br>
│
└── messages.txt   (optional - stores contact messages)

⚙️ Installation & Setup Steps
Step 1: Clone the repository
git clone https://github.com/Omkarpatange010/Portfolio-By-Omkar.git
cd FlaskPortfolio

Step 2: Create a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For Linux/Mac

Step 3: Install dependencies
pip install flask flask-mail

Step 4: Run the Flask app
python app.py

Step 5: Open in browser

Go to → http://127.0.0.1:5000

📧 Contact Form Setup (Optional Email Sending)
To enable email functionality:

Enable 2-Step Verification in your Gmail.
Create an App Password in Gmail settings.
Add it to your app.py configuration:

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', 'your_email@gmail.com')


Then test by sending a message from the Contact page.
☁️ Cloud Hosting (AWS / Render)
🟢 Deploy on AWS EC2:
Create an EC2 instance (Ubuntu).
SSH into your instance.
Install Python and Flask:

        sudo apt update<br>
        sudo apt install python3-pip<br>
        pip install flask flask-mail<br>
        Transfer your project files using SCP or Git clone.<br>

### Run the app: 
python3 app.py<br>
Access via EC2 public IP (http://<ec2-ip>:5000).

## Deploy on AWS EC2 :
Push your code to GitHub.
Login to AWS.com
Create a new Web Service → connect GitHub repo → set start command:
python app.py

