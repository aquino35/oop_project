from lib.worker import Worker
from lib.doctor import Doctor
from lib.engineer import Engineer
from lib.lawyer import Lawyer
from lib.student import Student


_worker = Worker("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 50000)
_worker.talk()

_doctor = Doctor("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 90000, "Generalist")
_doctor.talk()

_engineer =  Engineer("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 100000, "Computer", "Home", True)
_engineer.talk()

_lawyer = Lawyer("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 100000, "Vivoni Law Office, LLC")
_lawyer.talk()

_student = Student("Osvaldo", "Aquino", "M", "5'8", 170, 25, "UPRM", "ICOM")
_student.talk()
_student.calculate(100,80,100,100)