from flask import Flask, render_template, request, flash, redirect, url_for
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import json
from config import get_config

app = Flask(__name__)
config = get_config()
app.config.from_object(config)

# Portfolio data (you can also use a database)
with open(app.config['PORTFOLIO_DATA_FILE'], 'r') as f:
    portfolio_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Send email (configure your SMTP settings)
        send_contact_email(name, email, message)
        flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', data=portfolio_data)

def send_contact_email(name, email, message):
    # Configure your email settings
    try:
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg['Subject'] = f"Portfolio Contact - {name}"
        msg['From'] = app.config.get('MAIL_DEFAULT_SENDER', 'your-email@gmail.com')
        msg['To'] = app.config.get('CONTACT_EMAIL', 'qurrath2809@gmail.com')
        
        # Add your SMTP configuration
        if app.config.get('MAIL_USERNAME') and app.config.get('MAIL_PASSWORD'):
            with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
                if app.config['MAIL_USE_TLS']:
                    server.starttls()
                server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
                server.send_message(msg)
    except Exception as e:
        print(f"Email error: {e}")

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
