import React from "react";
import { Route, Switch } from "react-router-dom";
import { connect } from "react-redux";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import ForgotPasswordForm from "./ForgotPassword";
import ResetPasswordForm from "./ResetPassword";
import ResetConfirmation from "./ResetConfirmation";
import styled from "styled-components";

const Wrapper = styled(Switch)`
  display: flex;
  height: 100vh;
  align-items: center;
`;

const AuthPage = () => (
  <Wrapper>
    <Route exact path="/login" component={LoginForm} />
    <Route exact path="/register" component={RegisterForm} />
    <Route exact path="/reset" component={ForgotPasswordForm} />
    <Route exact path="/reset/:token" component={ResetPasswordForm} />
    <Route exact path="/reset-confirm/" component={ResetConfirmation} />
  </Wrapper>
);

export default AuthPage;
