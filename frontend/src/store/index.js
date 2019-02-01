import thunkMiddleware from "redux-thunk";
import { createBrowserHistory } from "history";
import { applyMiddleware, compose, createStore } from "redux";
import { createLogger } from "redux-logger";
import { routerMiddleware } from "connected-react-router";
import createRootReducer from "@reducers";

export const history = createBrowserHistory();

const loggerMiddleware = createLogger();

const configureStore = preloadedState =>
  createStore(
    createRootReducer(history),
    preloadedState,
    compose(
      applyMiddleware(
        thunkMiddleware,
        loggerMiddleware,
        routerMiddleware(history)
      )
    )
  );

export default configureStore;
