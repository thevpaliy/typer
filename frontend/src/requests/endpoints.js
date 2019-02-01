import Promise from "bluebird";
import { authPlugin } from "./auth";
import requests, { baseUrl } from "./requests";
import SessionManager from "@storage/session";

export const Auth = {
  login: (username, password) =>
    requests.post("/api/users/login", { username, password }).then(authPlugin),

  register: (email, username, password) =>
    requests
      .post("/api/users/register", {
        email,
        username,
        password
      })
      .then(authPlugin),

  signOut: () => SessionManager.clear()
};

export const ResetPassword = {
  requestReset: username =>
    requests.post("/api/users/reset-request", {
      username,
      callback_url: `${baseUrl}/reset/`
    }),

  verifyToken: token =>
    requests.post(`/api/users/reset-verify/${token}`).then(authPlugin),

  changePassword: password => requests.post("/api/users/reset", { password })
};

export const Sessions = {
  save: sessionData => requests.post("/api/sessions/", { sessionData })
};
