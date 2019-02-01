import LocalizedStrings from "react-localization";

export const strings = new LocalizedStrings({
  en: {
    labels: {
      submit: "Submit",
      signIn: "Sign In",
      signOut: "Sign Out",
      signUp: "Sign Up",
      forgotPassword: "Forgot password?",
      alreadyRegistered: "Already have an account?",
      changePassword: "Change Password",
      confirmPin: "Confirmation Code",
      confirmPinMessage:
        "We've sent a code to your email address. Please enter it below."
    },

    errors: {
      invalidPin: "Invalid Pin. Please check your email and try again.",
      rejectedToken:
        "Your link is invalid or expired. Please try resetting password again."
    },

    forms: {
      usernameEmail: "Username or email",
      username: "Username",
      email: "Email",
      password: "Password",
      repeatPassword: "Repeat password"
    }
  },
  rus: {
    // TODO: add Russian
  },
  ua: {
    //// TODO: add ukrainian
  }
});

export const LOGIN_START = "login-start";
export const LOGIN_SUCCESS = "login-success";
export const LOGIN_FAILURE = "login-failure";
export const REGISTER_START = "register-start";
export const REGISTER_SUCCESS = "register-success";
export const REGISTER_FAILURE = "register-failure";
export const SIGN_OUT = "sign-out";
export const VERIFY_TOKEN_START = "verify-token-start";
export const VERIFY_TOKEN_SUCCESS = "verify-token-success";
export const VERIFY_TOKEN_FAILURE = "verify-token-failure";
export const RESET_PASSWORD_START = "reset-password-start";
export const RESET_PASSWORD_SUCCESS = "reset-password-success";
export const RESET_PASSWORD_FAILURE = "reset-password-failure";
export const REQUEST_PASSWORD_RESET_START = "request-password-reset-start";
export const REQUEST_PASSWORD_RESET_SUCCESS = "request-password-reset-success";
export const REQUEST_PASSWORD_RESET_FAILURE = "request-password-reset-failure";
