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

  function load() {
    $.get('words.txt', (data, status)=> {
      let words = data.match(/\b(\w+)\b/g);
      session = createSession(shuffleWords(words));
    })
  }

  function shuffleWords(words) {
    for (let i = words.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [words[i], words[j]] = [words[j], words[i]];
    }
    return words;
  }

  function createSession(words) {
    let spans = [];
    let queue = [];
    for (let word of words) {
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

  load();
})
