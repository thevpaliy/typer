
def get_formatted_summary(user):
  average = {
    'words': user.words_score,
    'chars': user.chars_score,
    'accuracy': user.accuracy_score,
  }
  return {
    'id': user.id,
    'username': user.username,
    'average': average,
    'statistics': None
  }
