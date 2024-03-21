#
# from flask import Flask, render_template,request
# from flask import render_template, redirect, url_for
# from flask_wtf import FlaskForm
# from flask import Flask
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your-secret-key-here'
# from app import app
# from forms import QuestionnaireForm
# from wtforms import StringField, SubmitField  # 或者其他需要的字段类型
# from wtforms.validators import DataRequired
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your-secret-key-here'  # 你应该生成一个随机密钥
#
#
# @app.route('/')
# def welcome():
#     motto="The motto of the University of Glasgow: The way, the Truth, and the life"
#     return render_template('welcome.html',motto=motto)
#
# # 如果您有其他页面，也可以这样来渲染它们
# @app.route('/information')
#
# def information():
#     return render_template(
#         'information.html',
#         page_title='Reasons for Collecting Data on Student Progress at GIC',
#         declaration='1. Information is collected only to improve the quality of education and provide a better learning environment for students. 2. The privacy of all data will be protected by the University and will be used only for research purposes',
#         purposes=[
#             'Improve the quality of education at GIC',
#             'Enhance the overall student experience',
#             'Support personalized learning and academic success',
#             'Enable data-driven decision making for curriculum adjustments'
#         ],
#         benefits=[
#             'Provides insights into individual student progress and learning needs',
#             'Facilitates personalized support and interventions for students',
#             'Helps identify areas of improvement in curriculum and teaching methods',
#             'Enables evidence-based decision making for educational policies'
#         ]
#     )
#
# # 定义表单类
# class DataForm(FlaskForm):
#     # 定义字段
#     riqi = StringField('Data', validators=[DataRequired()])
#     first_name = StringField('First name', validators=[DataRequired()])
#     last_name = StringField('Last name', validators=[DataRequired()])
#     student_number = StringField('Student-number', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired()])
#     grade = StringField('Grade', validators=[DataRequired()])
#     satisfaction = StringField('Satisfaction', validators=[DataRequired()])
#     difficulty = StringField('difficulty', validators=[DataRequired()])
#     recommendations = StringField('recommendations')  # 假设这是一个可选字段
#     submit = SubmitField('submit')
#
# @app.route('/data', methods=['GET', 'POST'])
# def data():
#     form = DataForm()  # 创建表单实例
#     if request.method == 'POST' and form.validate_on_submit():
#         # 处理表单数据
#         data = form.data
#         print(data)  # 仅作为例子，实际中应该有更安全的数据处理方式
#         # 这里可以添加逻辑来保存数据或返回响应
#         # 重定向到其他页面或显示提交确认信息
#         return redirect(url_for('some_function'))  # 重定向到其他页面
#     # 如果是 GET 请求或者 POST 但未通过验证，则渲染 data.html 模板并传递 form
#     return render_template('data.html', form=form)
#
# @app.route('/questionnaire', methods=['GET', 'POST'])
# def questionnaire():
#     form = QuestionnaireForm()
#     if form.validate_on_submit():
#         # 在这里处理表单数据
#         selected_time_periods = form.time_periods.data
#         return redirect(url_for('success'))  # 假设你有一个名为 'success' 的视图函数
#     return render_template('questionnaire.html', form=form)
# @app.route('/success')
# def success():
#     return render_template('success.html')
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import QuestionnaireForm  # 确保这个类在 forms.py 中被定义

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# 定义 DataForm 类
# class DataForm(FlaskForm):
#     riqi = StringField('Date', validators=[DataRequired()])
#     first_name = StringField('First name', validators=[DataRequired()])
#     last_name = StringField('Last name', validators=[DataRequired()])
#     student_number = StringField('Student number', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired()])
#     grade = StringField('Grade', validators=[DataRequired()])
#     satisfaction = StringField('Satisfaction', validators=[DataRequired()])
#     difficulty = StringField('Difficulty', validators=[DataRequired()])
#     recommendations = StringField('Recommendations')  # 假设这是一个可选字段
#     submit = SubmitField('Submit')

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
        # 处理表单数据
        # ... 在这里添加您的数据处理逻辑

        return redirect(url_for('success'))
    return render_template('data.html', form=form)

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        flash("thank you")
        messages = get_flashed_messages()
        return f"Flash messages: {messages}"  # 直接显示消息，不重定向
    return render_template('questionnaire.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)