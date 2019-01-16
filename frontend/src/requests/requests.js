import superagent from "superagent";
import SessionManager from "@storage/session";
import TokenRefresher from "./auth";
import applyMiddleware from "./middleware";

const baseUrl = "http://localhost:5000/api";
const responseBody = response => response.body;

const tokenRefresher = new TokenRefresher(`${baseUrl}/refresh`);

const tokenPlugin = request => {
  if (SessionManager.hasValidTokens()) {
    const accessToken = SessionManager.getAccessToken();
    request.set("Authorization", `Token ${accessToken}`);
  }
};

const errorMessage = error => {
  const response = error.response;
  if (response && response.text) {
    const errorObject = JSON.parse(response.text);
    throw {
      name: "HTTP Request Failed",
      message: errorObject.message,
      toString: () => `${errorObject.message}`
    };
  }
  throw error;
};

const middleware = request => {
  if (SessionManager.hasExpiredTokens()) {
    const token = SessionManager.getRefreshToken();
    return tokenRefresher.refresh(token, SessionManager.save).then(request);
  }
  return request();
};

const requests = {
  post: (url, body) =>
    superagent
      .post(`${baseUrl}${url}`)
      .use(tokenPlugin)
      .send(body)
      .set("Accept", "application/json")
      .then(responseBody)
      .catch(errorMessage),

  get: (url, query = {}) =>
    superagent
      .get(`${baseUrl}${url}`)
      .use(tokenPlugin)
      .query(query)
      .set("Accept", "application/json")
      .then(responseBody)
      .catch(errorMessage),

  delete: url =>
    superagent
      .get(`${baseUrl}${url}`)
      .use(tokenPlugin)
      .then(responseBody)
      .catch(errorMessage)
};

export default applyMiddleware(middleware)(requests);
