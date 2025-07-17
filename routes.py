from flask import render_template, request, flash, redirect, url_for, jsonify
import os
import sendgrid
from sendgrid.helpers.mail import Mail as SGMail
from app import app
import logging

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    mail = SGMail(
        from_email='dasrajeeb167@gmail.com',
        to_emails='dasrajeeb167@gmail.com',
        subject=f'New Contact Form Submission from {name}',
        plain_text_content=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
    )
    try:
        response = sg.send(mail)
        if response.status_code in [200, 202]:
            flash('Your message has been sent successfully!', 'success')
        else:
            flash('An error occurred while sending your message. Please try again later.', 'danger')
            print(response.status_code, response.body)
    except Exception as e:
        print(e)
        flash('An error occurred while sending your message. Please try again later.', 'danger')
    return redirect(url_for('index'))

@app.route('/download-resume')
def download_resume():
    return redirect('/static/assets/resume.pdf')
