from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Message
from app import app, mail
import logging

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        if not all([name, email, message]):
            flash('All fields are required.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Create email message
        msg = Message(
            subject=f'Portfolio Contact from {name}',
            recipients=[app.config['MAIL_USERNAME']],
            body=f'''
            New contact form submission:
            
            Name: {name}
            Email: {email}
            Message: {message}
            '''
        )
        
        # Send email if mail is configured
        if app.config['MAIL_USERNAME']:
            mail.send(msg)
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        else:
            # Log the message if email isn't configured
            logging.info(f'Contact form submission - Name: {name}, Email: {email}, Message: {message}')
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        
    except Exception as e:
        logging.error(f'Error sending contact form: {str(e)}')
        flash('There was an error sending your message. Please try again.', 'error')
    
    return redirect(url_for('index') + '#contact')

@app.route('/download-resume')
def download_resume():
    return redirect('/static/assets/resume.pdf')
