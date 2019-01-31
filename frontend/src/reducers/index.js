import { combineReducers } from "redux";
import auth from "./authReducer";
import practice from "./practiceReducer";
import reset from "./resetReducer";

export default combineReducers({
  auth,
  reset,
  practice
});
