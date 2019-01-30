import React from "react";
import { Route, Switch } from "react-router-dom";
import { connect } from "react-redux";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import ForgotPasswordForm from "./ForgotPassword";
import ResetPasswordForm from "./ResetPassword";

const AuthPage = () => (
  <Switch>
    <Route exact path="/login" component={LoginForm} />
    <Route exact path="/register" component={RegisterForm} />
    <Route exact path="/reset" component={ForgotPasswordForm} />
    <Route exact path="/reset/:token" component={ResetPasswordForm} />
  </Switch>
);

export default AuthPage;
