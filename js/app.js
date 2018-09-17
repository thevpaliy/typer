$(document).ready(function() {
  'use strict'

  const SPACE = 32;
  const BACKSPACE = 8;

  var dictionary = $('#dictionary');
  var inputBox = $('#input-box');
  var typedWords = $('#typed-words');
  var wordsPerSession = $('#wps-metric');
  var charsPerSession = $('#cps-metric');
  var accuracyMetric = $('#accuracy-metric');
  var timer = $('#timer')

// TODO: perhaps there is a way to perfom lazy initialization
  var session = null;

  function Session(queue) {
    if (!(this instanceof Session)) {
      return new Session(queue);
    }
    this.queue = queue;
    this.total = 0;
    this.correct = 0;
    this.chars = 0;
    this.isTimerStarted = false;
  }

  Object.defineProperty(Session.prototype, 'currentWord', {
    get: function() { return this.queue[0].word; }
  })

  Object.defineProperty(Session.prototype, 'currentElement', {
    get: function() { return this.queue[0].element; }
  })

  Object.defineProperty(Session.prototype, 'accuracy', {
    get: function() {
       return Math.round((this.correct / this.total) * 100);
    }
  })

  Session.prototype.startTimerIfNeeded = function() {
      if (!this.isTimerStarted) {
        this.isTimerStarted = true;
        timer.text('60');
        let timerInterval = setInterval(()=> {
          if (timer.text() <= 0) {
            clearInterval(timerInterval);
            this.isTimerStarted = false;
            this.finishSession();
          } else {
            let previous = timer.text();
            timer.text(previous - 1);
          }
        }, 1000);
      }
  }

  Session.prototype.finishSession = function() {
    // TODO: present a pop-up to the user
  }

  Session.prototype.finishCurrentWith = function(word) {
    if (this.queue[0].word == word) {
      this.correct++;
      this.chars += word.length;
    }
    this.total++;
    this.queue.shift();
  }

  // TODO: remove this thing
  var wordList = [
      "fine", "took", "certain", "rain", "fly", "eat", "unit", "room",
      "lead", "friend", "cry", "began", "dark", "idea", "machine", "fish",
      "note", "mountain", "wait", "north", "plan", "once", "figure", "base",
      "star", "hear", "box", "horse", "noun", "cut", "field", "sure",
      "rest", "watch", "correct", "color", "able", "face", "pound", "wood",
      "done", "main", "beauty", "enough", "drive", "plain", "stood", "girl",
      "contain", "usual", "front", "young", "teach", "ready", "week",
      "above", "final", "ever", "gave", "red", "green", "list", "oh",
      "though", "quick", "feel", "develop", "talk", "sleep", "bird", "warm",
      "soon", "free", "body", "minute", "dog", "strong", "family",
      "special", "direct", "mind", "pose", "behind", "leave", "clear",
      "song", "tail", "measure", "produce", "state", "fact", "product",
      "street", "black", "inch", "short", "lot", "numeral", "nothing",
      "class", "course", "wind", "stay", "question", "wheel", "happen",
      "full", "complete", "force", "ship", "blue", "area", "object", "half",
      "decide", "rock", "surface", "order", "deep", "fire", "moon", "south",
      "island", "problem", "foot", "piece", "yet", "told", "busy", "knew",
      "test", "pass", "record", "farm", "boat", "top", "common", "whole",
      "gold", "king", "possible", "size", "plane", "heard", "age", "best",
      "dry", "hour", "wonder", "better", "laugh", "true", "thousand",
      "during", "ago", "hundred", "ran", "am", "check", "remember", "game",
      "step", "shape", "early", "yes", "hold", "hot", "west", "miss",
      "ground", "brought", "interest", "heat", "reach", "snow", "fast",
      "bed", "five", "bring", "sing", "sit", "listen", "perhaps", "six",
      "fill", "table", "east", "travel", "weight", "less", "language",
      "the", "name", "of", "very", "to", "through", "and", "just", "a",
      "form", "in", "much", "is", "great", "it", "think", "you", "say",
      "that", "help", "he", "low", "was", "line", "for", "before", "on",
      "turn", "are", "cause", "with", "same", "as", "mean", "I", "differ",
      "his", "move", "they", "right", "be", "boy", "at", "old", "one",
      "too", "have", "does", "this", "tell", "from", "sentence", "or",
      "set", "had", "three", "by", "want", "hot", "air", "but", "well",
      "some", "also", "what", "play", "there", "small", "we", "end", "can",
      "put", "out", "home", "other", "read", "were", "hand", "all", "port",
      "morning", "among"
    ];

  // TODO: this function should generate random words
  function getWords() {
    return wordList;
  }

  function createSession() {
    let array = getWords();
    let spans = [];
    let queue = [];
    for (let word of array) {
      let span = $('<span>').text(word)
      spans.push(span);
      queue.push({
        'word': word,
        'element': span
      });
    }
    dictionary.append(spans);
    return new Session(queue);
  }

  function handleSpace(userInput, targetWord) {
    let span = $('<span>').text(userInput);
    dictionary.find('span').first().remove();
    if (userInput != targetWord) {
      span.addClass('wrong-input');
    }
    session.finishCurrentWith(userInput);
    wordsPerSession.text(session.correct);
    charsPerSession.text(session.chars)
    accuracyMetric.text(session.accuracy);
    inputBox.before(span);
    inputBox.empty();
  }

  function onTyped(event) {
    let userInput = inputBox.html().trim();
    let targetWord = session.currentWord;
    let currentElement = session.currentElement;

    switch (event.keyCode) {
      case SPACE:
        if (userInput) {
          handleSpace(userInput, targetWord);
        }
        return false;
      case BACKSPACE:
        userInput = userInput.substring(0, userInput.length - 1);
        break;
      default:
        if (event.key.length == 1) {
          userInput += event.key;
        }
    }
    if (targetWord.startsWith(userInput)) {
      inputBox.removeClass('wrong-input')
      currentElement.html(
        targetWord.slice(userInput.length));
    } else {
      inputBox.removeClass('wrong-input')
    }
    return true;
  }

  inputBox.keydown(function(event) {
    session.startTimerIfNeeded();
    return onTyped(event);
  });

  $(document).click(()=> {
    inputBox.focus();
  })

  session = createSession();
})
