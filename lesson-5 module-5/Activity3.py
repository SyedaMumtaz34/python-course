class India():
    def Capital(self):
        print("New Delhi is the capital of India .")
    def language(self):
        print("Hindi is the most spoken language of India. ")
    def type (self):
        print("India is developing country. ")
class Pakistan():
    def Capital(self):
        print("Islamabad is a capital of pakistan .")
    def language(self):
        print("Urdu is the most sopken language of Pakistan, ")
    def type(self):
        print("Pakistan is developing country .")
obj_India =India()
obj_Pakistan=Pakistan()
for country in (obj_India,obj_Pakistan):
    country.Capital()
    country.language()
    country.type()