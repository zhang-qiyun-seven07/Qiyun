print("Title of program: Book Recommendation bot")
print()
while True:
  description = input("Could you describe what genre do you prefer in a sentence?")

  list_of_words = description.split()

  genre_list = []
  recommendation_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "fantasy":
      genre_list.append("sad")
      recommendation_list.append("The Land of Stories, The Lord of the Rings, The Chronicles of Narnia and The Inheritance Cycle")
      counter += 1
    if each_word == "mystery":
      genre_list.append("mystery")
      recommendation_list.append("The Hound of the Baskervilles and Hercule Poirot's Christmas")
      counter += 1
    if each_word == "romance":
      genre_list.append("romance")
      recommendation_list.append("A Walk to Remember, The Notebook, Safe Haven")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are interested in " + genre_list[0] + ". Some good books to consider are "+ recommendation_list[0] + ". Hope you enjoy reading :DD"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
