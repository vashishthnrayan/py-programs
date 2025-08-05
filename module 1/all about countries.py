class India:
    def capital(self):
        print("Capital of India is New Delhi")
    def language(self):
        print("Official language of India is Hindi")    
    def currency(self):
        print("Currency of India is Indian Rupee")
class USA:
    def capital(self):
        print("Capital of USA is Washington D.C.")
    def language(self):
        print("Official language of USA is English")
    def currency(self):
        print("Currency of USA is US Dollar")   


obj_ind = India()   
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.currency()
print()