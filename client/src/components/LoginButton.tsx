import { signInWithPopup } from "firebase/auth";
import { auth, googleProvider } from "../firebase";

export default function LoginButton() {
  const handleLogin = async () => {
    try {
      await signInWithPopup(auth, googleProvider);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const handleLogout = () => {
    auth.signOut();
  };

  return (
    <div>
      {auth.currentUser ? (
        <button onClick={handleLogout}>Logout</button>
      ) : (
        <button onClick={handleLogin}>Sign in with Google</button>
      )}
    </div>
  );
}