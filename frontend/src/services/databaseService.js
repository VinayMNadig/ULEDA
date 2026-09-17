import axios from "axios";

const API = "http://127.0.0.1:8000/database";

// ==========================================
// Upload Database
// ==========================================

export const uploadDatabase = async (formData) => {

    const response = await axios.post(

        `${API}/upload`,

        formData,

        {

            headers: {

                "Content-Type": "multipart/form-data",

            },

        }

    );

    return response.data;

};

// ==========================================
// List Databases
// ==========================================

export const getDatabases = async () => {

    const response = await axios.get(

        `${API}/list`

    );

    return response.data.databases;

};

// ==========================================
// Connect Database
// ==========================================

export const connectDatabase = async (databaseName) => {

    const response = await axios.post(

        `${API}/connect/${databaseName}`

    );

    return response.data;

};

// ==========================================
// Active Database
// ==========================================

export const getActiveDatabase = async () => {

    const response = await axios.get(

        `${API}/active`

    );

    return response.data;

};

// ==========================================
// Disconnect Database
// ==========================================

export const disconnectDatabase = async () => {

    const response = await axios.post(

        `${API}/disconnect`

    );

    return response.data;

};

// ==========================================
// Delete Database
// ==========================================

export const deleteDatabase = async (databaseName) => {

    const response = await axios.delete(

        `${API}/delete/${databaseName}`

    );

    return response.data;

};