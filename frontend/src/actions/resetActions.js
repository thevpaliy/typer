import { Auth } from "@requests";
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
  dispatch({ type: RESET_PASSWORD_FAILURE });
  dispatch({ type: RESET_PASSWORD_SUCCESS });
};

const requestReset = username => dispatch => {
  dispatch({ type: REQUEST_PASSWORD_RESET_START });
  dispatch({ type: REQUEST_PASSWORD_RESET_FAILURE });
  dispatch({ type: REQUEST_PASSWORD_RESET_SUCCESS });
};

const verifyToken = token => dispatch => {
  dispatch({ type: VERIFY_TOKEN_START });
  dispatch({ type: VERIFY_TOKEN_SUCCESS });
  dispatch({ type: VERIFY_TOKEN_FAILURE });
};

export { changePassword, requestReset, verifyToken };
