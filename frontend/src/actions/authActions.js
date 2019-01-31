import { Auth } from "@requests";
import {
  LOGIN_START,
  LOGIN_FAILURE,
  LOGIN_SUCCESS,
  REGISTER_START,
  REGISTER_FAILURE,
  REGISTER_SUCCESS,
  SIGN_OUT
} from "@constants";

const login = (username, password) => dispatch => {
  dispatch({ type: LOGIN_START });
  Auth.login(username, password)
    .then(response => {
      dispatch({
        type: LOGIN_SUCCESS,
        token: response.token,
        user: response.user
      });
    })
    .catch(error => {
      dispatch({
        type: LOGIN_FAILURE,
        error: error.message
      });
    });
};

const register = (email, username, password) => dispatch => {
  dispatch({ type: REGISTER_START });
  Auth.register(email, username, password)
    .then(response => {
      dispatch({
        type: REGISTER_SUCCESS,
        token: response.token,
        user: response.user
      });
    })
    .catch(error => {
      dispatch({
        type: REGISTER_FAILURE,
        error: error.message
      });
    });
};

const signOut = () => dispatch => {
  Auth.signOut();
  dispatch({ type: SIGN_OUT });
};

export { login, register, forgotPassword, signOut };
