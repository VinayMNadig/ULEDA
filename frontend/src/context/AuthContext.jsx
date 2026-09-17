import { createContext, useContext, useState } from "react";

import {
  saveToken,
  logoutUser,
  isLoggedIn,
} from "../services/authService";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [loggedIn, setLoggedIn] = useState(isLoggedIn());

  const login = (token) => {
    saveToken(token);
    setLoggedIn(true);
  };

  const logout = () => {
    logoutUser();
    setLoggedIn(false);
  };

  return (
    <AuthContext.Provider
      value={{
        loggedIn,
        login,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}