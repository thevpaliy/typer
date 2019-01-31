import { fetchWords, saveSession } from "./practiceActions";
import { login, register, signOut } from "./authActions";
import { requestReset, verifyToken, changePassword } from "./resetActions";

export const actions = Object.assign({
  login,
  register,
  signOut,
  fetchWords,
  saveSession,
  requestReset,
  verifyToken,
  changePassword
});
