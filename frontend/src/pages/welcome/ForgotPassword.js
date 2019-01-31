import React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { actions } from "@actions";
import { strings } from "@constants";
import ErrorMessage from "Components/ErrorMessage";
import LoadingButton from "Components/LoadingButton";
import AuthFooter from "Components/AuthFooter";
import { Header, Page, Form, Input } from "./style";
import styled from "styled-components";

class ForgotPasswordForm extends React.Component {
  state = {
    isButtonEnabled: false,
    username: null
  };

  static propTypes = {
    errors: PropTypes.string.isRequired,
    isLoading: PropTypes.bool.isRequired,
    onSubmit: PropTypes.func.isRequired
  };

  static defaultProps = {
    errors: null,
    isLoading: false,
    onSubmit: () => {}
  };

  onSubmit = event => {
    event.preventDefault();

    const { username } = this.state;
    const { onSubmit } = this.props;

    onSubmit(username);
  };

  onEmailChange = event => {
    this.setState({
      isButtonEnabled: event.target.value,
      username: event.target.value
    });
  };

  render() {
    return (
      <Page>
        <Header>{strings.labels.forgotPassword}</Header>
        <Form onSubmit={this.onSubmit}>
          <Input
            type="text"
            value={this.state.username}
            onChange={this.onEmailChange}
            placeholder={strings.forms.usernameEmail}
          />
          <LoadingButton
            title={strings.labels.submit}
            isLoading={this.props.isLoading}
            isEnabled={this.state.isButtonEnabled}
          />
        </Form>
        <ErrorMessage error={this.props.error} />
        <AuthFooter path="/login" text={strings.labels.nopeRememeber} />
      </Page>
    );
  }
}

const mapStateToProps = state => ({
  isLoading: state.auth.isLoading,
  error: state.auth.errors
});

const mapDispatchToProps = dispatch => ({
  onSubmit: username => {
    dispatch(actions.forgotPassword(username));
  }
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ForgotPasswordForm);
