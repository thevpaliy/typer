from app.models import DailyStats, WeeklyStats, MonthlyStats

def _get_formatted_stats(cls, user_id):
  def _format(data):
    return [dict(zip(('time', 'value'), (t, v)))
        for t, v in data.items()
    ]

  chars = cls.get_chars(user_id)
  words = cls.get_words(user_id)
  accuracy = cls.get_accuracy(user_id)
  return {
    'chars': _format(chars),
    'words': _format(words),
    'accuracy': _format(accuracy)
  }


def get_formatted_weekly_stats(id):
  stats = _get_formatted_stats(WeeklyStats, id)
  return {'weekly': stats }


def get_formatted_monthly_stats(id):
  stats = _get_formatted_stats(MonthlyStats, id)
  return {'monthly': stats }


def get_formatted_daily_stats(id):
  stats = _get_formatted_stats(DailyStats, id)
  return {'daily': stats }


def get_formatted_stats(id):
  stats = get_formatted_daily_stats(id)
  stats.update(get_formatted_weekly_stats(id))
  stats.update(get_formatted_monthly_stats(id))
  return stats


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
    'statistics': get_formatted_stats(user.id)
  }
