import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";
import { connect } from "react-redux";
import { actions } from "@actions";
import { strings } from "@constants";
import ErrorMessage from "Components/ErrorMessage";
import LoadingButton from "Components/LoadingButton";
import AuthFooter from "Components/AuthFooter";
import { Header, Form, Input, Page } from "./style";

class ResetPasswordForm extends React.Component {
  state = {
    isButtonEnabled: false,
    password: null,
    repeatedPassword: null
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

    const { password, repeatedPassword } = this.state;

    if (password === repeatedPassword) {
      this.props.onSubmit(password);
    }
  };

  onFieldChange = event => {
    const target = event.target;
    const field = target.name;
    const value = target.value;

    this.setState({
      [field]: value,
      isButtonEnabled:
        Object.keys(this.state)
          .filter(key => !["isButtonEnabled", field].includes(key))
          .map(key => this.state[key])
          .every(v => v === value) && value
    });
  };

  render() {
    return (
      <Page>
        <Header>{strings.labels.changePassword}</Header>
        <Form onSubmit={this.onSubmit}>
          <Input
            type="password"
            name="password"
            value={this.state.password}
            onChange={this.onFieldChange}
            placeholder={strings.forms.password}
          />
          <Input
            type="password"
            name="repeatedPassword"
            value={this.state.repeatedPassword}
            onChange={this.onFieldChange}
            placeholder={strings.forms.repeatPassword}
          />
          <LoadingButton
            title={strings.labels.submit}
            isLoading={this.props.isLoading}
            isEnabled={this.state.isButtonEnabled}
          />
        </Form>
        <ErrorMessage error={this.props.error} />
        <AuthFooter path="/login" text={strings.labels.backToSignIn} />
      </Page>
    );
  }
}

const mapStateToProps = state => ({
  isLoading: state.reset.isLoading,
  errors: state.reset.error
});

const mapDispatchToProps = dispatch => ({
  onSubmit: password => dispatch(actions.changePassword(password))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ResetPasswordForm);
