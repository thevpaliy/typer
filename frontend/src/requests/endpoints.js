import Promise from "bluebird";
import { authPlugin } from "./auth";
import requests from "./requests";
import SessionManager from "Storage";

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
