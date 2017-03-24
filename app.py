from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from database import db_session
from database import init_db
from models import *

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__, template_folder='templates/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def main():
	departments = Department.query.all()
	for department in departments:
		print (department.vac)
	return render_template('index.html', departments=departments)

@app.route("/create_department")
def create_department():
	return render_template('create_department.html')


@app.route("/show_can")
def show_can():
	candidates = Candidate.query.all()
	return render_template('can.html', candidates = candidates)


@app.route("/create_department_action/", methods=['POST'])
def create_department_action():
	if request.method == 'POST':
		department_name = request.form['dname']
		department_description = request.form['ddesc']
		new_department = Department()
		new_department.name = department_name
		new_department.description = department_description
		db_session.add(new_department)
		db_session.commit()
		return redirect(url_for('main'))
	else:
		return "Something is wrong"

@app.route("/look_at_vacancies/")
def show_vanacies():
	vacancies = Vacancy.query.all()
	return render_template('vacancies.html', vacancies = vacancies )

@app.route("/show_workers/")
def show_workers():
	workers = Worker.query.all()
	return render_template('workers.html', workers = workers )

@app.route("/create_vacancy/")
def create_vacancy():
	return render_template('create_vacancy.html')

@app.route("/addcan/")
def addcan():
	if request.method == 'POST':
		candidate_name = request.form['name']
		candidate_vacancy = request.form['vacancy']
		candidate_email= request.form['email']
		candidate_phone = request.form['phone']
	else:
		return render_template('addcan.html')

@app.route("/create_vacancy_action/", methods=['POST'])
def create_vacancy_action():
	if request.method == 'POST':
		vacancy_name = request.form['vname']
		department_name = request.form['dname']
		vacancy_description = request.form['vdesc']
		new_vacancy = Vacancy()
		new_vacancy.name = vacancy_name
		new_vacancy.description = vacancy_description
		new_vacancy.department = Department(name=department_name)
		db_session.add(new_vacancy)
		db_session.commit()
		return redirect(url_for('show_vanacies'))
	else:
		return "Something is wrong"

@app.route("/add_candidate_as_worker/", methods=['POST'])
def add_candidate_as_worker():
	if request.method == 'POST':
		candidate_name = request.values['name']
		candidate_vacancy = request.values['vacancy']
		
		new_worker = Worker()
		new_worker.name = candidate_name
		# new_vacancy.vacancy = Vacancy(name=candidate_vacancy)
		db_session.add(new_worker)
		# can_to_delete = Candidate(name=candidate_name)
		Candidate(name=candidate_name).query.delete()
		# if can_to_delete:
		# 	can_to_delete.delete()
		db_session.commit()
		return redirect(url_for('show_workers'))
	else:
		return "Something is wrong"



if __name__ == '__main__':
	init_db()
	app.run()