import requests

class Employee:

    raise_amt = 5.0

    def __init__(self,firstname,lastname,pay):
        self.first = firstname
        self.last =  lastname
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    def checkWebpage(self):
        response = requests.get(f'https://www.google.com/')
        if response.ok:
            return response.text
        else:
            return 'Bad Response'


#E = Employee('Balraj','Bemainboina', 500)
#print(E.email)
#print(E.fullname)
#E.apply_raise()
