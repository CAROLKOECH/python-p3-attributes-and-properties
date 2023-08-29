APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC",
    "Production", "Legal", "Finance", "Sales", "General Management",
    "Research & Development", "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = name
        self._job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (len(value) <= 25):
            print("Name must be a string under 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
