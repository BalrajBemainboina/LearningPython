import re

Example_Test = 'Jessica is 16 years old, and Daniel is 27 years, Edward is 38 years, and his grandfather Oscar is 100years'

ages = re.findall(r'\d{1,3}', Example_Test)
names = re.findall(r'[A-Z][a-z]*',Example_Test)
print(ages)
print(names)

