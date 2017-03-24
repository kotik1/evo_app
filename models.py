from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class Department(Base):
	__tablename__ = 'department'

	id = Column(Integer, primary_key=True)
	name =  Column(String(50), unique=True)
	description = Column(String(120))
	worker = relationship("Worker")
	def __init__(self, name=None, description=None):
		self.name = name
		self.description = description

	def __repr__(self):
		return '<User %r>' % (self.name)

class Vacancy(Base):
	__tablename__ = 'vacancy'

	id = Column(Integer, primary_key=True)
	name =  Column(String(50), unique=True)
	description = Column(String(120))
	department_id = Column(Integer, ForeignKey('department.id'))
	department = relationship("Department", backref="vac")

class Worker(Base):
	__tablename__ = 'worker'

	id = Column(Integer, primary_key=True)
	name =  Column(String(50), unique=True)
	description = Column(String(120))
	department_id = Column(Integer, ForeignKey('department.id'))
	department = relationship("Department", backref="wor")

class Candidate(Base):
	__tablename__ = 'candidate'

	id = Column(Integer, primary_key=True)
	name =  Column(String(50), unique=True)
	description = Column(String(120))
	vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
	vacancy = relationship("Vacancy", backref="can")
	# department_id = Column(Integer, ForeignKey('department.id'))
	# department = relationship("Department", backref="can")





