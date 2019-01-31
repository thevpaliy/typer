import { fetchWords, saveSession } from "./practiceActions";
import { login, register, forgotPassword, signOut } from "./authActions";
import { requestReset, verifyToken, changePassword } from "./resetActions";

export const actions = Object.assign({
  login,
  register,
  forgotPassword,
  signOut,
  fetchWords,
  saveSession,
  requestReset,
  verifyToken,
  changePassword
});
