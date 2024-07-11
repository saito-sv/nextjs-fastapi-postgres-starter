"use client";

import { useState, useEffect } from "react";
import { useSocket, useSocketEvent } from "socket.io-react-hook";
import { fetchOldMessages } from "../utils/api";

interface Message {
  text: string;
  isUser: boolean;
}

const useChat = (userId: number) => {
  const socketURL = process.env.NEXT_PUBLIC_API_URL || "ws://localhost:8000";
  const { socket, error } = useSocket(socketURL, {
    transports: ["websocket"],
  });
  const [messages, setMessages] = useState<Message[]>([]);

  const { lastMessage } = useSocketEvent<{ message: string }>(
    socket,
    "response",
  );

  useEffect(() => {
    if (lastMessage) {
      if (lastMessage.message && typeof lastMessage.message === "string") {
        setMessages((prev) => [
          ...prev,
          { text: lastMessage.message, isUser: false },
        ]);
      } else {
        console.error("Invalid message format:", lastMessage);
      }
    }
  }, [lastMessage]);

  useEffect(() => {
    const loadOldMessages = async () => {
      try {
        const oldMessages = await fetchOldMessages(userId);
        setMessages(
          oldMessages.flatMap((msg: any) => [
            { text: msg.user_message, isUser: true },
            { text: msg.bot_response, isUser: false },
          ]),
        );
      } catch (error) {
        console.error("Failed to load old messages:", error);
      }
    };

    loadOldMessages();
  }, [userId]);

  const sendMessage = (message: string) => {
    socket.emit("message", { user_id: userId, message });
    setMessages((prev) => [...prev, { text: message, isUser: true }]);
  };

  return { messages, sendMessage, error };
};

export default useChat;
