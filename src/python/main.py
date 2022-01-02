from lib.worker import Worker
from lib.doctor import Doctor
#from lib.engineer import Engineer

_worker = Worker("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 50000)
_worker.talk()

_doctor = Doctor("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 90000, "Generalist")
_doctor.talk()