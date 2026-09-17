export const saveChats = (chats) => {
  localStorage.setItem("uleda_chats", JSON.stringify(chats));
};

export const loadChats = () => {
  const chats = localStorage.getItem("uleda_chats");

  if (!chats) {
    return [
      {
        title: "New Chat",
        messages: [],
      },
    ];
  }

  return JSON.parse(chats);
};