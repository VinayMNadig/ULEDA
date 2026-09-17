import { useState } from "react";
import "./OTPModal.css";

function OTPModal({
    open,
    requestId,
    onVerify,
    onCancel,
}) {
    const [otp, setOtp] = useState("");
    const [loading, setLoading] = useState(false);

    if (!open) return null;
const verifyOTP = async () => {

    if (!otp.trim()) {

        alert("Please enter OTP");

        return;

    }

    setLoading(true);

    try {

        const result = await onVerify(otp);

        if (result.success) {

            setOtp("");

        } else {

            alert(result.answer || "Verification Failed");

        }

    } catch (error) {

        console.error(error);

        if (error.response?.data?.answer) {

            alert(error.response.data.answer);

        } else if (error.response?.data?.detail) {

            alert(error.response.data.detail);

        } else {

            alert("Something went wrong.");

        }

    } finally {

        setLoading(false);

    }


    };

    return (

        <div className="otp-overlay">

            <div className="otp-modal">

                <h2>🔐 Permission Required</h2>

                <p>
                    OTP has been sent to the Database Administrator.
                </p>

                <p>
                    Request ID :
                    <strong> {requestId}</strong>
                </p>

                <input
                    type="text"
                    placeholder="Enter OTP"
                    value={otp}
                    maxLength={6}
                    onChange={(e) =>
                        setOtp(e.target.value)
                    }
                />

                <div className="otp-buttons">

                    <button
                        className="cancel-btn"
                        onClick={onCancel}
                    >
                        Cancel
                    </button>

                    <button
                        className="verify-btn"
                        onClick={verifyOTP}
                        disabled={loading}
                    >
                        {loading
                            ? "Verifying..."
                            : "Verify OTP"}
                    </button>

                </div>

            </div>

        </div>

    );
}

export default OTPModal;