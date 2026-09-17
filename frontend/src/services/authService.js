import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// ==========================
// Register User
// ==========================

export const registerUser = async (userData) => {
  const response = await API.post(
    "/auth/register",
    userData
  );

  return response.data;
};

// ==========================
// Login User
// ==========================

export const loginUser = async (userData) => {
  const response = await API.post(
    "/auth/login",
    userData
  );

  return response.data;
};

// ==========================
// Save Token
// ==========================

export const saveToken = (token) => {
  localStorage.setItem(
    "access_token",
    token
  );
};

// ==========================
// Get Token
// ==========================

// ==========================
// Get Token
// ==========================

export const getToken = () => {
  return localStorage.getItem("access_token");
};

// ==========================
// Logout
// ==========================

export const logoutUser = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("user");
};

// ==========================
// Is Logged In
// ==========================

export const isLoggedIn = () => {
  return !!localStorage.getItem(
    "access_token"
  );
};