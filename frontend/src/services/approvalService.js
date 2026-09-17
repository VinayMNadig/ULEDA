import axios from "axios";

const API = "http://127.0.0.1:8000";

// ========================================
// Send OTP Request (Optional)
// ========================================

export const requestApproval = async (
    question,
    sql,
    email
) => {

    const response = await axios.post(

        `${API}/approval/request`,

        {
            question,
            sql,
            email,
        }

    );

    return response.data;

};

// ========================================
// Verify OTP
// ========================================

export const verifyOTP = async (
    requestId,
    otp
) => {

    const response = await axios.post(

        `${API}/approval/verify`,

        {

            request_id: requestId,

            otp: otp,

        }

    );

    return response.data;

};

// ========================================
// Get Pending Requests
// ========================================

export const getPendingRequests = async () => {

    const response = await axios.get(

        `${API}/approval/pending`

    );

    return response.data;

};

// ========================================
// Get Approval History
// ========================================

export const getApprovalHistory = async () => {

    const response = await axios.get(

        `${API}/approval/history`

    );

    return response.data;

};

export default {

    requestApproval,

    verifyOTP,

    getPendingRequests,

    getApprovalHistory,

};