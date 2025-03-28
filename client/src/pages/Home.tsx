import { useEffect, useState } from "react";
import Editor from "../components/Editor";
import LoginButton from "../components/LoginButton";
import { auth } from "../firebase";

export default function Home() {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((user) => setUser(user));
    return unsubscribe;
  }, []);

  const handleSave = async (content: string) => {
    if (!user) {
      alert("Please sign in first!");
      return;
    }
    const token = await user.getIdToken();
    const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/save`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ content }),
    });
    const data = await response.json();
    console.log("Saved:", data);
  };

  return (
    <div>
      <LoginButton />
      {user && <Editor onSave={handleSave} />}
    </div>
  );
}