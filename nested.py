ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

email = ramit['email']
interests = ramit['interests'][0]
jasmines_email = ramit['friends'][0]['email']
jans_interests = ramit['friends'][1]['interests'][1]

solutions = [email, interests, jasmines_email, jans_interests]

print(solutions)

def countFriends(dict):
  count = 0

  for friend in dict['friends']:
    count += 1

  dict['friends_count'] = count

  return dict

print(countFriends(ramit))