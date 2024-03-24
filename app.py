
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from forms import QuestionnaireForm
import os
from flask import Flask, render_template, request
from forms import QuestionnaireForm  # Import form class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'



@app.route('/')
def welcome():
    motto = "The motto of the University of Glasgow: The way, the Truth, and the life"
    return render_template('welcome.html', motto=motto)

@app.route('/information')
def information():
    return render_template(
        'information.html',
        page_title='Reasons for Collecting Data on Student Progress at GIC',
        declaration='1. Information is collected only to improve the quality of education and provide a better learning environment for students. 2. The privacy of all data will be protected by the University and will be used only for research purposes',
        purposes=[
            'Improve the quality of education at GIC',
            'Enhance the overall student experience',
            'Support personalized learning and academic success',
            'Enable data-driven decision making for curriculum adjustments'
        ],
        benefits=[
            'Provides insights into individual student progress and learning needs',
            'Facilitates personalized support and interventions for students',
            'Helps identify areas of improvement in curriculum and teaching methods',
            'Enables evidence-based decision making for educational policies'
        ]
    )

@app.route('/data', methods=['GET', 'POST'])
def data():
    form = QuestionnaireForm()
    if request.method == 'POST' and form.validate_on_submit():        
        return redirect(url_for('success'))
    return render_template('data.html', form=form)


# Defines a  function that converts form data to a string and then saves it to a text file
def save_to_file(form_data):
    filename = 'questionnaire_data.txt'#Define the file that save data of questionnaire
    with open(filename, 'a') as file:  # Additional content
        for field in form_data:
            if field == 'csrf_token':
                continue
            if field == 'time_periods':  # Converts the values in the time_periods list directly to strings separated by commas
                time_periods = form_data[field]
                time_periods_str = ', '.join(time_periods)
                file.write(f'{field}: {time_periods_str}\n')
            else:
                file.write(f'{field}: {form_data[field]}\n')
        file.write('\n')  # separating character
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        save_to_file(form.data)  # Save form data to a text file
        flash("thank you")
        messages = get_flashed_messages()
        return redirect(url_for('success'))  #show information when submit
    return render_template('questionnaire.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
