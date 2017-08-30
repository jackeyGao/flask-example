# -*- coding: utf-8 -*-
import sys
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import Flask
from flask import render_template
from db import Student

reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route("/")
def index():
    students = Student.select()
    return render_template('index.html', students=students)


@app.route("/add")
def add():
    try:
        student = Student(
            name=request.args.get('name'),
            gender=request.args.get('gender'),
            teacher=request.args.get('teacher'),
            grade=int(request.args.get('grade')),
        )
        student.save()
        flash("%s 已增加" % student.name)
    except Exception as e:
        flash(str(e))
    
    return redirect(url_for('index'))

@app.route("/rm")
def rm():
    try:
        pk = int(request.args.get('id'))
        
        student = Student.get(id=pk)
        student.delete_instance()
        flash("%s 已删除" % student.name)
    except Exception as e:
        flash(str(e))

    return redirect(url_for('index'))
