
#----------------------------

def read_file(name) :

  # a variavel chamada 'set'
  # é criada como um novo conjunto
  # através da função set()
  data = set()

  with open(name) as file:
    for line in file :
      words = line.split()
      
      for word in words:
        data.add(word)
        put_word_in_repository(word)

  database.append(data)

#----------------------------

def run_files(file):
  with open(file) as file_of_files:
    for filename in file_of_files :
      read_file(name =  filename.rstrip())

#----------------------------

def print_words(set):
    for word in set:
      print(f'|> {word}')

#----------------------------

def print_sets(database):
    for i in range(len(database)):
      print(f'Conjunto de palavras #{i+1}')
      print_words(set = database[i])

#----------------------------

def put_word_in_repository(word) :

  if not is_word_in_repository(word) :
    repository[word] = 0

  repository[word] += 1

#----------------------------

def is_word_in_repository(word) :
  if word in repository : return True
  else : return False

#----------------------------

database = []
repository = {}

run_files( file = input('insert the file with filenames to run: ') )
print_sets( database = database )

print('------------------')

# supor que não existe maior
greatest = None

for key, value in repository.items() :
  if greatest == None or value > greatest['value']: 
    greatest = {'key' : key , 'value' : value}

print(greatest)

print('------------------')

