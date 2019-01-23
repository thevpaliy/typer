import { Sessions } from "@requests";

const fetchWords = () => dispatch => {
  dispatch({ type: "fetch-words-start" });
};

const saveSession = sessionData => dispatch => {
  dispatch({ type: "saving-session" });
  Sessions.save(sessionData).then(response => {
    dispatch({});
  });
};

export { fetchWords, saveSession };
