from app.models import Session, Scores
from app.models import DailyStats, WeeklyStats, MonthlyStats

def get_formatted_scores(user_id):
  return  {
    'words': Scores.get_average_words_score(user_id),
    'chars': Scores.get_average_chars_score(user_id),
    'accuracy': Scores.get_average_accuracy_score(user_id)
  }


def _get_formatted_stats(cls, user_id):
  def _prepare(data):
    return [dict(zip(('time', 'value'), (t, v)))
        for t, v in data.items()
    ]

  chars = cls.get_chars(user_id)
  words = cls.get_words(user_id)
  accuracy = cls.get_accuracy(user_id)
  return {
    'chars': _prepare(chars),
    'words': _prepare(words),
    'accuracy': _prepare(accuracy)
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
  return {
    'id': user.id,
    'username': user.username,
    'average': get_formatted_scores(user.id),
    'statistics': get_formatted_stats(user.id)
  }
