import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";
import { connect } from "react-redux";
import { actions } from "@actions";
import { strings } from "@constants";
import ErrorMessage from "Components/ErrorMessage";
import LoadingButton from "Components/LoadingButton";
import ResetPasswordForm from "./ResetPasswordForm";
import Forbidden from "../errors/Forbidden"

class ResetPasswordController extends React.Component {
  componentWillMount() {
    const { match, verifyToken } = this.props;
    verifyToken(match.params.token);
  }
  render() {
    const { error, token } = this.props;
    if (error) {
      return <Forbidden />;
    }
    return token ? <ResetPasswordForm /> : null;
  }
}

const mapStateToProps = state => ({
  token: state.auth.token,
  error: state.auth.error
});

const mapDispatchToProps = dispatch => ({
  verifyToken: token => dispatch(actions.verifyToken(token))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ResetPasswordController);
