import axios from "axios";

const API = "http://127.0.0.1:8000";

// ===========================
// Create Chat
// ===========================

export async function createChat(chat) {

    const response = await axios.post(
        `${API}/chat-history/`,
        chat
    );

    return response.data;

}

// ===========================
// Load User Chats
// ===========================

export async function getChats(userId) {

    const response = await axios.get(
        `${API}/chat-history/${userId}`
    );

    return response.data;

}

// ===========================
// Update Chat
// ===========================

export async function updateChat(chatId, chat) {

    console.log("=================================");
    console.log("UPDATE CHAT REQUEST");
    console.log("Chat ID:", chatId);
    console.log("Body:");
    console.log(JSON.stringify(chat, null, 2));
    console.log("=================================");

    const response = await axios.put(
        `${API}/chat-history/${chatId}`,
        chat
    );

    return response.data;

}

// ===========================
// Delete Chat
// ===========================

export async function deleteChatAPI(chatId) {

    const response = await axios.delete(
        `${API}/chat-history/${chatId}`
    );

    return response.data;

}