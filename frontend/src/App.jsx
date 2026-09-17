import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import DatabaseManager from "./pages/DatabaseManager";

import "./App.css";

function App() {

    const user = localStorage.getItem("user");

    return (

        <BrowserRouter>

            <Routes>

                {/* Default */}

                <Route
                    path="/"
                    element={
                        user
                            ? <Navigate to="/dashboard" replace />
                            : <Navigate to="/login" replace />
                    }
                />

                {/* Login */}

                <Route
                    path="/login"
                    element={<Login />}
                />

                {/* Register */}

                <Route
                    path="/register"
                    element={<Register />}
                />

                {/* Dashboard */}

                <Route
                    path="/dashboard"
                    element={<Dashboard page="dashboard" />}
                />

                {/* Database */}

                <Route
                    path="/database"
                    element={<Dashboard page="database" />}
                />

                {/* Analytics */}

                <Route
                    path="/analytics"
                    element={<Dashboard page="analytics" />}
                />

                {/* History */}

                <Route
                    path="/history"
                    element={<Dashboard page="history" />}
                />

                {/* Settings */}

                <Route
                    path="/settings"
                    element={<Dashboard page="settings" />}
                />

                {/* Unknown */}

                <Route
                    path="*"
                    element={<Navigate to="/" replace />}
                />

            </Routes>

        </BrowserRouter>

    );

}

export default App;