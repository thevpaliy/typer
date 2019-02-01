import { push } from "connected-react-router";
import { ResetPassword } from "@requests";
import { strings } from "@constants";
import {
  RESET_PASSWORD_START,
  RESET_PASSWORD_SUCCESS,
  RESET_PASSWORD_FAILURE,
  REQUEST_PASSWORD_RESET_START,
  REQUEST_PASSWORD_RESET_FAILURE,
  REQUEST_PASSWORD_RESET_SUCCESS,
  VERIFY_TOKEN_START,
  VERIFY_TOKEN_SUCCESS,
  VERIFY_TOKEN_FAILURE
} from "@constants";

const changePassword = password => dispatch => {
  dispatch({ type: RESET_PASSWORD_START });
  ResetPassword.changePassword(password)
    .then(response => {
      dispatch({
        type: RESET_PASSWORD_SUCCESS
      });
    })
    .catch(error => {
      dispatch({
        type: RESET_PASSWORD_FAILURE,
        error: error.message
      });
    });
};

const requestReset = username => dispatch => {
  dispatch({ type: REQUEST_PASSWORD_RESET_START });
  ResetPassword.requestReset(username)
    .then(response => {
      dispatch({
        type: REQUEST_PASSWORD_RESET_SUCCESS,
        pinCode: response.pin,
        resetToken: response.token
      });
    })
    .catch(error => {
      dispatch({
        type: REQUEST_PASSWORD_RESET_FAILURE,
        error: error.message
      });
    });
};

const verifyToken = token => dispatch => {
  dispatch({ type: VERIFY_TOKEN_START });
  ResetPassword.verifyToken(token)
    .then(response => {
      dispatch({
        type: VERIFY_TOKEN_SUCCESS,
        user: response.user,
        auth: response.auth,
        confirmed: response.auth !== undefined
      });
    })
    .catch(error => {
      dispatch({
        type: VERIFY_TOKEN_FAILURE,
        error: strings.errors.rejectedToken
      });
    });
};

export { changePassword, requestReset, verifyToken };
