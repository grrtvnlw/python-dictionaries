menu = '''
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)?
'''

phonebook = {

}

def lookup(name):
  result = print(f'Found entry for {name}: {phonebook[name]}')

  return result

def set_entry():
  name = input('Name: ')
  phone = input('Phone Number: ')
  result = print(f'Entry stored for {name}')

  phonebook[name] = phone

  return result

def delete_entry(name):
  result = print(f'Deleted entry for {name}')
  del phonebook[name]

  return result

def list_all():
  for key in phonebook.keys():
    print(f'Found entry for {key}: {phonebook[key]}')

while True:
  inp = int(input(menu))

  if inp == 1:
    name = input('Give me name: ')
    lookup(name)
  elif inp == 2:
    set_entry()
  elif inp == 3:
    name = input('Give me name: ')
    delete_entry(name)
  elif inp == 4:
    list_all()
  else:
    print('Bye.')
    break