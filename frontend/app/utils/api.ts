"use client";
const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export const fetchOldMessages = async (user_id: number) => {
  const response = await fetch(`${apiUrl}/chats?user_id=${user_id}`);
  if (!response.ok) {
    throw new Error("Failed to fetch old messages");
  }
  return response.json();
};

export const fetchUser = async () => {
  const response = await fetch(`${apiUrl}/users/me`);
  if (!response.ok) {
    throw new Error("Failed to fetch user");
  }
  return response.json();
};
