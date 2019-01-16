const initialState = {
  words: [],
  isLoading: false,
  error: null
};

const practiceReducer = (state = initialState, action) => {
  switch (action.type) {
    case "fetch-words-start":
      return { ...state, words: [], isLoading: true };
    case "fetch-words-failed":
      return { error: action.error, words: [], isLoading: false };
    case "fetch-words-success":
      return { error: null, words: action.words, isLoading: false };
    case "save-session-failure":
      return { ...state, error: action.error };
    default:
      return state;
  }
};

export default authReducer;
