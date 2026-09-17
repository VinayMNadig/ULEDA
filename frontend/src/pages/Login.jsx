import "./Dashboard.css";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import Sidebar from "../components/Sidebar/Sidebar";
import ChatPage from "../components/ChatPage/ChatPage";
import OTPModal from "../components/OTPModal";

const API = "http://127.0.0.1:8000";

function getStoredUser() {

    const raw = localStorage.getItem("user");

    if (!raw || raw === "undefined" || raw === "null") {
        return null;
    }

    try {
        return JSON.parse(raw);
    } catch (e) {
        return null;
    }
}

function Dashboard() {

    const navigate = useNavigate();

    const user = getStoredUser();

    useEffect(() => {

        if (!user) {

            localStorage.removeItem("user");
            localStorage.removeItem("access_token");

            navigate("/login");

        }

    }, [user, navigate]);

    const [messages, setMessages] = useState([
        {
            sender: "assistant",
            text:
                "👋 Hello! Welcome to ULEDA.\n\nI'm your Universal LLM Database Assistant.\n\nHow can I help you today?"
        }
    ]);

    const [loading, setLoading] = useState(false);

    const [showOTPModal, setShowOTPModal] = useState(false);

    const [requestId, setRequestId] = useState(null);

    const [pendingQuestion, setPendingQuestion] = useState("");

    const [pendingSQL, setPendingSQL] = useState("");

    //--------------------------------------------------
    // SEND MESSAGE
    //--------------------------------------------------

    const sendMessage = async (question) => {

        if (!question.trim()) return;

        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text: question
            }
        ]);

        setLoading(true);

        try {

           const response = await axios.post(
    `${API}/chat`,

                {
                    question,
                    approve: false,
                    sql: "",
                    user_id: user?.id
                }

            );

            const data = response.data;

            //--------------------------------------
            // OTP REQUIRED
            //--------------------------------------

            if (!data) {

    setMessages(prev => [
        ...prev,
        {
            sender: "bot",
            text: "Server returned an empty response."
        }
    ])

    return
}

if (data.requires_permission) {
                setPendingQuestion(question);

                setPendingSQL(data.sql);

                setRequestId(data.request_id);

                setShowOTPModal(true);

                setMessages(prev => [

                    ...prev,

                    {

                        sender: "assistant",

                        text: "🔐 OTP verification required.",

                        sql: data.sql,

                        data: []

                    }

                ]);

            }

            //--------------------------------------
            // NORMAL RESPONSE
            //--------------------------------------

            else {

                setMessages(prev => [

                    ...prev,

                    {

                        sender: "assistant",

                        text: data.answer,

                        sql: data.sql,

                        data: data.data

                    }

                ]);

            }

        }

        catch (err) {

            console.log(err);

            setMessages(prev => [

                ...prev,

                {

                    sender: "assistant",

                    text:
                        err.response?.data?.detail ||
                        "❌ Server Error"

                }

            ]);

        }

        finally {

            setLoading(false);

        }

    };

    //--------------------------------------------------
    // VERIFY OTP
    //--------------------------------------------------

    const handleOTPVerify = async (otp) => {

        try {

            setLoading(true);

            const response = await axios.post(

                `${API}/approval/verify`,

                {

                    request_id: requestId,

                    otp: otp

                }

            );

            const data = response.data;

            setMessages(prev => [

                ...prev,

                {

                    sender: "assistant",

                    text: data.answer,

                    sql: data.sql,

                    data: data.data

                }

            ]);

            setShowOTPModal(false);

            setPendingQuestion("");

            setPendingSQL("");

            setRequestId(null);

            return data;

        }

        catch (err) {

            console.log(err);

            return err.response?.data || {

                success: false,

                answer: "OTP Verification Failed"

            };

        }

        finally {

            setLoading(false);

        }

    };

    //--------------------------------------------------
    // CANCEL OTP
    //--------------------------------------------------

    const handleOTPCancel = () => {

        setShowOTPModal(false);

        setPendingQuestion("");

        setPendingSQL("");

        setRequestId(null);

    };

    //--------------------------------------------------
    // LOGOUT
    //--------------------------------------------------

    const logout = () => {

        localStorage.removeItem("user");

        localStorage.removeItem("access_token");

        navigate("/login");

    };

    //--------------------------------------------------
    // UI
    //--------------------------------------------------

    return (

        <>

            <div className="dashboard-layout">

                <Sidebar logout={logout} />

                <div className="dashboard-content">

                    <ChatPage

                        messages={messages}

                        loading={loading}

                        sendMessage={sendMessage}

                    />

                </div>

            </div>

            <OTPModal

                open={showOTPModal}

                requestId={requestId}

                onVerify={handleOTPVerify}

                onCancel={handleOTPCancel}

            />

        </>

    );

}

export default Dashboard;