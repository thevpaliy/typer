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

const initialState = {
  resetToken: null,
  pinCode: null,
  error: null
};

const resetReducer = (state = initialState, action) => {
  switch (action.type) {
    default:
      return state;
  }
};

export default resetReducer;
