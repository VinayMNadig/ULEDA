import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { FaUser, FaEnvelope, FaLock } from "react-icons/fa";

import { registerUser } from "../services/authService";

import "../App.css";

function Register() {

  const navigate = useNavigate();

  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const submitHandler = async (e) => {

    e.preventDefault();

    try {

      const response = await registerUser({

        name,

        email,

        password,

      });

      if (response.success) {

        toast.success("Registration Successful!");

        navigate("/login");

      } else {

        toast.error(response.message);

      }

    } catch (error) {

      toast.error("Registration Failed");

      console.log(error);

    }

  };

  return (

    <div className="auth-container">

      <div className="auth-card">

        <h1>ULEDA</h1>

        <h2>Register</h2>

        <form onSubmit={submitHandler}>

          <div className="input-group">

            <FaUser />

            <input
              type="text"
              placeholder="Full Name"
              value={name}
              onChange={(e)=>setName(e.target.value)}
              required
            />

          </div>

          <div className="input-group">

            <FaEnvelope />

            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e)=>setEmail(e.target.value)}
              required
            />

          </div>

          <div className="input-group">

            <FaLock />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e)=>setPassword(e.target.value)}
              required
            />

          </div>

          <button
            className="auth-btn"
            type="submit"
          >
            Register
          </button>

        </form>

        <p className="auth-link">

          Already have an account?

          <Link to="/login">
            Login
          </Link>

        </p>

      </div>

    </div>

  );

}

export default Register;