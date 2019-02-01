import React from "react";
import ReactDOM from "react-dom";
import { Route, Switch } from 'react-router' // react-router v4
import { ConnectedRouter } from "connected-react-router";
import { Provider } from "react-redux";
import PropTypes from "prop-types";
import App from "./pages/App";
import configureStore, { history } from "./store";

const store = configureStore();

const Root = () => (
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <Switch>
        <Route path="/" component={App} />
      </Switch>
    </ConnectedRouter>
  </Provider>
);

Root.propTypes = {
  store: PropTypes.object.isRequired
};

ReactDOM.render(<Root />, document.getElementById("root"));
