import { combineReducers } from "redux";
import auth from "./authReducer";
import practice from "./practiceReducer";

export default combineReducers({
  auth,
  practice
});
