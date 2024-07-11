"use client";

import React, { useEffect, useRef } from "react";
import { ChatMessage } from "./ChatMessage";
import { ChatInput } from "./ChatInput";
import useChat from "../hooks/useChat";

const Chat = ({ userId }: { userId: number }) => {
  const { messages, sendMessage, error } = useChat(userId);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg.text} isUser={msg.isUser} />
        ))}
        <div ref={messagesEndRef} />
      </div>
      <ChatInput sendMessage={sendMessage} />
    </div>
  );
};

export default Chat;
