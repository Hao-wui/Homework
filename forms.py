from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, RadioField, TextAreaField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, Length




class QuestionnaireForm(FlaskForm):
    riqi = DateField('Date', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    student_number = StringField('Student Number', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    grade = StringField('Grade', validators=[DataRequired(), Length(max=20)])
    satisfaction = SelectField('Course Satisfaction', choices=[
        ('Very satisfied', 'Very satisfied'),
        ('satisfied', 'satisfied'),
        ('somewhat satisfied', 'somewhat satisfied'),
        ('average', 'average'),
        ('need improvement', 'need improvement')
    ])
    difficulty = RadioField('Course Difficulty Evaluation', choices=[
        ('Large', 'Large'),
        ('Medium', 'Medium'),
        ('Small', 'Small')
    ])

    time_periods = SelectMultipleField(
        'Expected course period',
        choices=[('morning', 'Morning'), ('noon', 'Noon'), ('afternoon', 'Afternoon')],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        # validators=[DataRequired()],
        coerce=str
    )




    recommendations = TextAreaField('Recommendations for Improvement', validators=[DataRequired()])

    submit = SubmitField('Submit')
