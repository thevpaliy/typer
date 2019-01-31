import React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { actions } from "@actions";
import { strings } from "@constants";
import ErrorMessage from "Components/ErrorMessage";
import ConfirmationInput from "Components/ConfirmationInput";
import AnimationBuilder from "Components/Animation";
import lockJson from "./lock.json";
import styled from "styled-components";

const Header = styled.h2`
  text-align: center;
  font-size: 20px;
  padding-top: 8px;
  padding-bottom: 8px;
  font-weight: 600;
  text-transform: uppercase;
  display: inline-block;
  margin: 0px 8px 0px 8px;
  color: #757575;
  box-sizing: content-box;
`;

const Message = styled.p`
  text-align: center;
  font-size: 14px;
  padding-top: 8px;
  padding-bottom: 8px;
  font-weight: 400;
  margin: 2px 8px 10px 8px;
  color: gray;
  box-sizing: content-box;
`;

const Page = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  -webkit-border-radius: 0.1rem;
  border-radius: 0.1rem;
  background-color: transparent;
  max-width: 420px;
  position: relative;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0, 0, 0, 0.3);
  box-shadow: 0 30px 60px 0 rgba(0, 0, 0, 0.3);
  margin-left: auto;
  margin-right: auto;
  top: 10%;
  box-sizing: content-box;
  padding: 2rem;
`;

const LockAnimation = new AnimationBuilder(lockJson)
  .withStyle({ marginTop: "1rem" })
  .withLoop(false)
  .withAutoplay(true)
  .build();

const Status = ({ error }) =>
  error ? <ErrorMessage error={error} /> : <LockAnimation />;

class ResetConfirmation extends React.Component {
  state = {
    error: null
  };

  onFinished = input => {
    const { pinCode, history, token } = this.props;
    if (pinCode != input) {
      this.setState({
        error: strings.errors.invalidPin
      });
    } else {
      history.push(`/reset/${token}`);
    }
  };

  render() {
    return (
      <Page>
        <Header>{strings.labels.confirmPin}</Header>
        <Message>{strings.labels.confirmPinMessage}</Message>
        <ConfirmationInput count={5} onFinished={this.onFinished} />
        <Status error={this.state.error} />
      </Page>
    );
  }
}

const mapStateToProps = state => ({
  pinCode: state.reset.pinCode,
  token: state.reset.token
});

export default connect(mapStateToProps)(ResetConfirmation);
