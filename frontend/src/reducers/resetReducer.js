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
  isLoading: false,
  resetToken: null,
  pinCode: null,
  error: null,
  confirmed: false
};

const resetReducer = (state = initialState, action) => {
  switch (action.type) {
    case RESET_PASSWORD_START:
    case REQUEST_PASSWORD_RESET_START:
    case VERIFY_TOKEN_START:
      return { isLoading: true, ...state };
    case REQUEST_PASSWORD_RESET_SUCCESS:
      return {
        resetToken: action.resetToken,
        pinCode: action.pinCode,
        ...initialState
      };
    case VERIFY_TOKEN_SUCCESS:
      return {
        confirmed: action.confirmed,
        ...initialState
      };
    case REQUEST_PASSWORD_RESET_FAILURE:
    case RESET_PASSWORD_FAILURE:
    case VERIFY_TOKEN_FAILURE:
      return { error: action.error, isLoading: false, ...state };
    default:
      return state;
  }
};

export default resetReducer;
