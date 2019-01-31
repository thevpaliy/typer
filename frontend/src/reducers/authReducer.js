import {
  LOGIN_START,
  LOGIN_FAILURE,
  LOGIN_SUCCESS,
  REGISTER_START,
  REGISTER_FAILURE,
  REGISTER_SUCCESS,
  SIGN_OUT
} from "@constants";

const initialState = {
  token: null,
  user: null,
  isLoading: false,
  error: null
};

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case SIGN_OUT:
      return { ...state, token: null };
    case LOGIN_START:
    case REGISTER_START:
      return { ...state, isLoading: true };
    case LOGIN_SUCCESS:
    case REGISTER_SUCCESS:
      return {
        ...state,
        isLoading: false,
        user: action.user,
        token: action.token
      };
    case LOGIN_FAILURE:
    case REGISTER_FAILURE:
      return {
        ...state,
        user: null,
        isLoading: false,
        error: action.error
      };
    default:
      return state;
  }
};

export default authReducer;
