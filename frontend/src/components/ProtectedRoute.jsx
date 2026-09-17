import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function ProtectedRoute({ children }) {

  const { loggedIn } = useAuth();

  if (!loggedIn) {

    return <Navigate to="/login" replace />;

  }

  return children;

}

export default ProtectedRoute;