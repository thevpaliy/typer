import React from 'react'
import ForgotPasswordForm from './ForgotPasswordForm'
import ResetConfirmation from './ResetConfirmation'
import { connect } from "react-redux";

const ForgotPasswordController = ({ pinCode }) => (
  pinCode ? <ResetConfirmation /> : <ForgotPasswordForm />
)

const mapStateToProps = state => ({
  pinCode: state.reset.pinCode,
});

export default connect(
  mapStateToProps,
)(ForgotPasswordController);
