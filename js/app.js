'use strict'

const SPACE = 32;
const BACKSPACE = 8;

var dictionary = document.getElementById('dictionary')
var inputBox = document.getElementById('input-box')
var typedWords = document.getElementById('typed-words')
var queue = [];

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

function createSpanWithText(text) {
  let span = document.createElement('span');
  span.innerHTML = text;
  return span;
}

function loadWords() {
  let array = getWords();
  for (let word of array) {
    let span = createSpanWithText(word);
    queue.push({
      'word': word,
      'element': span
    });
    dictionary.appendChild(span);
  }
  dictionary.removeChild(dictionary.firstChild);
}

function markAsWrong(element) {
  if (!element.classList.contains('wrong-input')) {
    element.classList.add('wrong-input')
  }
}

function markAsCorrect(element) {
  if (element.classList.contains('wrong-input')) {
    element.classList.remove('wrong-input')
  }
}

function handleSpace(userInput, targetWord) {
  let span = createSpanWithText(userInput);
  dictionary.removeChild(queue.shift().element);
  if (userInput != targetWord) {
    markAsWrong(span);
  }
  typedWords.insertBefore(span, inputBox);
  inputBox.innerHTML = null;
}

function type(event) {
  let current = queue[0];
  let userInput = inputBox.innerHTML.trim();
  let targetWord = current.word;

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
      userInput += event.key;
  }
  if (targetWord.startsWith(userInput)) {
    markAsCorrect(inputBox);
    current.element.innerHTML = targetWord.slice(userInput.length);
  } else {
    markAsWrong(inputBox);
  }
  return true;
}

inputBox.focus();
inputBox.onkeydown = type;
document.body.onclick = ()=> {
  inputBox.focus();
}
