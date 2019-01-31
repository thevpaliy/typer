import React from "react";
import { Route, Switch } from "react-router-dom";
import { connect } from "react-redux";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import ForgotPasswordForm from "./ForgotPassword";
import ResetPasswordController from "./ResetPasswordController";
import ResetConfirmation from "./ResetConfirmation";
import styled from "styled-components";
import NotFoundPage from '../errors/NotFound'


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
    <Route exact path="/reset/:token" component={ResetPasswordController} />
    <Route exact path="/reset-confirm/" component={ResetConfirmation} />
    <Route component={NotFoundPage} />
  </Wrapper>
);

export default AuthPage;
