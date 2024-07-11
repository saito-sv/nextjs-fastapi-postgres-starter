"use client";

import React, { useState } from "react";

interface ChatInputProps {
  sendMessage: (messsage: string) => void;
}

export const ChatInput = ({ sendMessage }: ChatInputProps) => {
  const [message, setMessage] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim()) {
      sendMessage(message);
      setMessage("");
    }
  };
  return (
    <form onSubmit={handleSubmit} className="flex p-2 border-t">
      <input
        type="text"
        className="flex-1 p-1 border rounded text-black"
        placeholder="I need to reschedule"
        value={message}
        onChange={(e) => {
          setMessage(e.target.value);
        }}
      />
      <button
        type="submit"
        className="p-2 ml-2 border rounded bg-blue-500 text-white"
      >
        Send
      </button>
    </form>
  );
};
