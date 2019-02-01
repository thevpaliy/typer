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
    const { error, confirmed } = this.props;
    if (error) {
      return <Forbidden />;
    }
    return confirmed ? <ResetPasswordForm /> : null;
  }
}

const mapStateToProps = state => ({
  confirmed: state.reset.confirmed,
  error: state.reset.error
});

const mapDispatchToProps = dispatch => ({
  verifyToken: token => dispatch(actions.verifyToken(token))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ResetPasswordController);
