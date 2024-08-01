class person():
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        from datetime import date
        today = date.today()
        dob = self.dob.split("-")
        age = today.year - int(dob[0])
        return age
p = person("John", "USA", "1990-01-01")
print("Name:", p.name)
print("Country:", p.country)
print("Date of Birth:", p.dob)
print("Age:", p.age())
