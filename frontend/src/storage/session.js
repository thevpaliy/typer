import Storage from "./storage";

const TOKENS_KEY = "auth-tokens";

class SessionManager {
  static save(authData) {
    Storage.put(TOKENS_KEY, JSON.stringify(authData));
  }

  static hasValidTokens() {
    return Storage.contains(TOKENS_KEY) && !this.hasExpiredTokens();
  }

  static hasExpiredTokens() {
    const authData = this.getAuthDataJSON();
    if (authData) {
      const time = new Date().getTime();
      return authData.expires < time;
    }
    return false;
  }

  static clear() {
    Storage.remove(TOKENS_KEY);
  }

  static getAccessToken() {
    const authData = this.getAuthDataJSON();
    return authData.access_token;
  }

  static getRefreshToken() {
    const authData = this.getAuthDataJSON();
    return authData.refresh_token;
  }

  static getAuthDataJSON() {
    const authData = Storage.get(TOKENS_KEY);
    return JSON.parse(authData) || {};
  }
}

export default SessionManager;
