# string concatenation (basically means how to put strings together)

# Few Ways on how to put string together____________>

#print("Subscribe to" + variable) # using the plus sign
#print("subscribe to {}".format(variable)) # using the curly brackets with .format(varible) method which will put the variable where the curly brackest are located
#print(f"subscribe to {variable}") # using the f string, putting the letter f in front of the string and using the curly brackets and putting the variable inbetween


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"computer programing is so {adj}! It makes me so excited all the time because  i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)