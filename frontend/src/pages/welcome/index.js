import React from "react";
import { Route, Switch } from "react-router-dom";
import { connect } from "react-redux";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import ForgotPassword from "./ForgotPassword";
import ResetPassword from "./ResetPassword";
import styled from "styled-components";
import NotFoundPage from "../errors/NotFound";

const Wrapper = styled(Switch)`
  display: flex;
  height: 100vh;
  align-items: center;
`;

const AuthPage = () => (
  <Wrapper>
    <Route exact path="/login" component={LoginForm} />
    <Route exact path="/register" component={RegisterForm} />
    <Route exact path="/reset" component={ForgotPassword} />
    <Route exact path="/reset/:token" component={ResetPassword} />
    <Route component={NotFoundPage} />
  </Wrapper>
);

export default AuthPage;
