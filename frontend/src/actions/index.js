import { fetchWords, saveSession } from "./practiceActions";
import { login, register, forgotPassword, signOut } from "./authActions";

export const actions = Object.assign({
  login,
  register,
  forgotPassword,
  signOut,
  fetchWords,
  saveSession
});
