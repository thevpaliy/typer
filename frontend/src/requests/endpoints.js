import Promise from "bluebird";
import { authPlugin } from "./auth";
import requests from "./requests";
import SessionManager from "@storage/session";

export const Auth = {
  login: (username, password) =>
    requests.post("/users/login", { username, password }).then(authPlugin),

  register: (email, username, password) =>
    requests
      .post("/users/register", {
        email,
        username,
        password
      })
      .then(authPlugin),

  recover: email => requests.post("/users/recover", { email }),

  signOut: () => SessionManager.clear()
};

export const ResetPassword = {
  requestReset: username =>
    requests.post("/api/users/reset-request", { username }),

  verifyResetToken: token => requests.post("/api/users/reset-verify", token),

  resetPassword: password => requests.post("/api/users/reset", { password })
};

export const Sessions = {
  save: sessionData => requests.post("/sessions/", { sessionData })
};
