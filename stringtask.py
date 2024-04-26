first_name=" JoHn "
last_name=" Doe "
first_name=first_name.strip().capitalize().title()
last_name=last_name.strip().capitalize().title()
full_name=first_name+" "+last_name

print(full_name)
print(len(first_name))
email='gafagah@gmail.com'
print(email.count('@')==1)
st="this is my book"
print(type(st.split(" ")))
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph'
print(sentence_two[16:30])
sentence_three='The lazy dog; ran so fast; it hit the wall.'
print(sentence_three.split(';'))
#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
firstname="  Joh.n"
lastname="   Do,e"
firstname=firstname.strip().replace('.','').capitalize()
lastname=lastname.strip().replace(',','').capitalize()
fullname=firstname+' '+lastname
print(fullname)
#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r=["E","W","C"]
s=''.join(r)
print(s)
name = 'John Doe'
print(name[::0])