class Employer:
	raise_amt = 1.04

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.email = first+'_'+last+'@company.pe'
		self.pay = pay

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employer):
	raise_amt = 1.5

	def __init__(self,first,last,pay,prog_lang):
		Employer.__init__(self,first,last,pay)
		self.prog_lang = prog_lang

class Manager(Employer):
	raise_amt=1.8

	def __init__(self,first,last,pay,prog_lang,employ=None):
		Employer.__init__(self,first,last,pay)
		self.prog_lang = prog_lang
		if employ is None:
			self.employ = []
		else:
			self.employ = employ

	def add_emp(self,emp):
		if emp not in self.employ:
			self.employ.append(emp)

	def delete_emp(self,emp):
		if emp in self.employ:
			self.employ.remove(emp)

	def print_emps(self):
		for person in self.employ:
			print(person.fullname())		

dev1 = Developer("Edge","rated",600,"Java")
dev2 = Developer("Christian","Poo",900,"Python")
dev3 = Developer("Jeff","Stan",9600,"Ruby")


mr_mcman = Manager("Sr","Mcman","60000","Go",[dev1,dev2])

print(dev1.fullname())
dev1.apply_raise()
print(f'{dev1.pay} {dev1.prog_lang}')


mr_mcman.add_emp(dev3)
mr_mcman.print_emps()