#1
#«Прізвище»-«оцінка»
#biology = {
#    "Petro": 3,
#    "Dima": 4,
#    "Anna": 5,
#    "Adam": 5,
#    "Halia Lebedeva": 4
#}
#biology["Vladislav Petrenko"] = 5
#print(biology)
#a = input("Do you want add the student and his score?")
#if a == "Yes" "yes" "Ok" "ok":
 #   add_student = input("Ener the new student #you can add only one student,and his score ")
#    add_score =  int(input("Enter this student score from 1 to 5 "))
#    score = 1, 2, 3, 4, 5
#    if add_score not in score:
 #       print(f"Eror, we don't care your number! ")
#    else:
##        biology[add_student] = add_score
 #       print(biology)
#else:
#    print("OK let's move on! ")

#good_grades = dict()

#for student_name, grade in biology.items():
  #  if grade >= 4:
  #      good_grades[student_name] = grade
  #      print(good_grades)
#print(biology)

#2
#weather = {
#    "Kyiv": 19,
#    "Odessa": 20,
#    "Donetsk": 29,
#    "Ivano-Frankivsk": 30
#}


#total_temperature = 0
#count = len(weather)

#for temp in weather.values():
#    total_temperature += temp

#print(f'Avg of temperatures = {total_temperature/count}')
#===============================

#prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
#if 3 in prime_numbers:
#    print("Ok")
#else:
#    print("There none 3")
#================
#User {name}, age - {age}
#name surname
#print(user["name"])
#=======
post_ukr = {'Київ', 'Фастів', 'Ірпінь', 'Боярка'}

post_new = {'Київ', 'Фастів', 'Кагарлик', 'Узин', 'Ірпінь', 'Гатне', 'Боярка', 'Гостомель'}
city =("Enter your city ")
if city in post_ukr and  city in post_new:
    choose = ("Choose or ukr post or new post (1-ukr post 2-new post)")
    if choose == "1":
        print("This is a new post")
    elif choose == "2":
        print("You choose new post")
elif city in post_ukr:
    print("We cansend")


