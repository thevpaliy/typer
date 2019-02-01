import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";
import auth from "./authReducer";
import practice from "./practiceReducer";
import reset from "./resetReducer";

export default (history) => combineReducers({
  router: connectRouter(history),
  auth,
  reset,
  practice
})
