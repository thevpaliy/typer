from flask import jsonify
from app.api import api
from app.models import User, \
  DailyStats, WeeklyStats, MonthlyStats, Scores

@api.route('/summary/<int:id>')
def get_summary(id):
  user = User.query.get_or_404(id)
  statistics, summary = {}, {}
  # get all stats
  for type, stat in zip(['daily', 'weekly', 'monthly'],
        [DailyStats, WeeklyStats, MonthlyStats]):
    statistics[type] = stat.all_to_dict(id)
  # get all average metrics
  words, chars, accuracy = Scores.get_all_average(user)
  summary = {
    'average_words': words,
    'average_chars': chars,
    'average_accuracy': accuracy
  }
  return jsonify({
    'username': user.username,
    'summary': summary,
    'statistics': statistics,
  })
