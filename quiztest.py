import random, copy

# First option in the dictionary is the correct answer
original_questions = {
 #Format is 'question':[options]
 'Taj Mahal':['Agra','New Delhi','Mumbai','Chennai'],
 'Great Wall of China':['China','Beijing','Shanghai','Tianjin'],
 'Petra':['Ma\'an Governorate','Amman','Zarqa','Jerash'],
 'Machu Picchu':['Cuzco Region','Lima','Piura','Tacna'],
 'Egypt Pyramids':['Giza','Suez','Luxor','Tanta'],
 'Colosseum':['Rome','Milan','Bari','Bologna'],
 'Christ the Redeemer':['Rio de Janeiro','Natal','Olinda','Betim']
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
    '''Shuffle the questions.'''
    selected_keys = []
    i = 0
    while i < len(q):
      current_selection = random.choice(list(q.keys()))
      if current_selection not in selected_keys:
        selected_keys.append(current_selection)
        i = i+1
    return selected_keys

questions_shuffled = shuffle(questions)

for i in questions_shuffled:
  random.shuffle(questions[i])
  print(
     f'''
    Where is {i} located?
    {questions[i]}
    Correct answer is {original_questions[i][0]}
    '''
  )