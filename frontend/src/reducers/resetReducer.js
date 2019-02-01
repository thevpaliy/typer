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
      return { ...state, isLoading: true };
    case REQUEST_PASSWORD_RESET_SUCCESS:
      return {
        ...initialState,
        resetToken: action.resetToken,
        pinCode: action.pinCode
      };
    case VERIFY_TOKEN_SUCCESS:
      return {
        ...initialState,
        confirmed: action.confirmed
      };
    case REQUEST_PASSWORD_RESET_FAILURE:
    case RESET_PASSWORD_FAILURE:
    case VERIFY_TOKEN_FAILURE:
      return { ...state, error: action.error, isLoading: false };
    default:
      return state;
  }
};

export default resetReducer;
