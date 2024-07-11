"use client";
import React from "react";

interface ChatMessageProps {
  message: string;
  isUser: boolean;
}

export const ChatMessage = ({ message, isUser }: ChatMessageProps) => {
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-2`}>
      <div
        className={`max-w-xs px-4 py-2 rounded-lg ${
          isUser ? "bg-blue-500 text-white" : "bg-gray-300 text-black"
        }`}
      >
        <div className="text-sm">{isUser ? "You" : "Bot"}</div>
        <div className="text-base">{message}</div>
      </div>
    </div>
  );
};
