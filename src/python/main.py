from lib.worker import Worker
from lib.doctor import Doctor
from lib.engineer import Engineer
from lib.lawyer import Lawyer
from lib.student import Student


_worker = Worker("Ana", "Ribon", "M", "5'8", 170, 22, 40, 50000)
print(_worker.first_name)

_worker.first_name ="Osvaldo"
print(_worker.first_name)
print(_worker._person_count)

_w = Worker("Juan", "Rivera", "M", "5'8", 170, 22, 40, 50000)
print(_w._person_count)

_wo = Worker("Jose", "Colon", "M", "5'8", 170, 22, 40, 50000)
print(_wo._person_count)

_wor = Worker("Jeziel", "Torres", "M", "5'8", 170, 22, 40, 50000)
print(_wor._person_count)
print(_wor._worker_count)


_worker.talk()

_doctor = Doctor("Ale", "Pagan", "M", "5'8", 170, 22, 40, 90000, "Generalist")
print(_doctor._doctor_count)
print(_doctor._person_count)

_doctor.talk()

_engineer =  Engineer("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 100000, "Computer", "Home", True)
print(_engineer._person_count)
print(_engineer._worker_count)
print(_engineer._engineer_count)
_engineer.talk()

_lawyer = Lawyer("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 100000, "Vivoni Law Office, LLC")
_lawyer.talk()
print(_lawyer._person_count)
print(_lawyer._worker_count)
print(_lawyer._lawyer_count)


_doctor1 = Doctor("Ale", "Pagan", "M", "5'8", 170, 22, 40, 90000, "Generalist")
print(_doctor1._doctor_count)
print(_doctor1._person_count)


_student = Student("Osvaldo", "Aquino", "M", "5'8", 170, 25, "UPRM", "ICOM")
_student.talk()
_student.calculate(100,80,100,100)