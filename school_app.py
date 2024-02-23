from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
import json


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hank@localhost/FlaskSchool'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    subject_name = db.relationship('Subject', backref=db.backref('students'))
                              
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    subject_name = db.relationship('Subject', backref=db.backref('teachers'))
class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255))


@app.route('/students/', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = []
    for student in students:
        student_data  = OrderedDict({
            'id': student.id, 
            'first_name': student.first_name, 
            'last_name': student.last_name, 
            'age': student.age, 
            'class': {
                'subject' : student.subject_name.subject,
                'teacher': f'{student.subject_name.teachers[0].first_name} {student.subject_name.teachers[0].last_name}'
            }   
        })
        student_list.append(student_data)
        response = Response(json.dumps(student_list, sort_keys=False), mimetype='application/json') 
    return response

@app.route('/teachers/', methods = ['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    teacher_list = []
    for teacher in teachers:
        students = [f'{student.first_name} {student.last_name}' for student in teacher.subject_name.students]
        teacher_data = {
            'id' : teacher.id,
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'age' : teacher.age,
            'subject' : teacher.subject_name.subject,
            'students': students
        }
        teacher_list.append(teacher_data)
    return jsonify(teacher_list)

@app.route('/subjects/', methods = ['GET'])
def get_subjects():
    subjects = Subject.query.all()
    subject_list = []
    for subject in subjects:
        subject_data = {
            'id' : subject.id,
            'name': subject.subject
        }
        subject_list.append(subject_data)
    return jsonify(subject_list)


       
app.run(debug=True)