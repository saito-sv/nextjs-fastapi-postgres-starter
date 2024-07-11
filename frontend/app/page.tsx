"use client";
import React, { useEffect, useState } from "react";
import Chat from "./components/Chat";
import { fetchUser } from "./utils/api";
import { IoProvider } from "socket.io-react-hook";

const Home: React.FC = () => {
  const [user, setUser] = useState<{ id: string; username: string } | null>(
    null,
  );

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const userData = await fetchUser();
        setUser(userData);
      } catch (error) {
        console.error("Failed to fetch user", error);
      }
    };

    fetchUserData();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <IoProvider>
      <div className="flex items-center justify-center h-screen">
        <div className="w-full max-w-2xl border rounded shadow-lg">
          <Chat userId={Number(user.id)} />
        </div>
      </div>
    </IoProvider>
  );
};

export default Home;
