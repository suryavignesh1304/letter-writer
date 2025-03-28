import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyANbOkJiX7kFeuntSvVjP5X6_y5KarmKp4",
    authDomain: "login-app-290e6.firebaseapp.com",
    projectId: "login-app-290e6",
    storageBucket: "login-app-290e6.firebasestorage.app",
    messagingSenderId: "867895472462",
    appId: "1:867895472462:web:d68d2034d3b3a1efd1ae1f",
    measurementId: "G-PTC0NCJ9ST"
  };

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const googleProvider = new GoogleAuthProvider();
googleProvider.addScope("https://www.googleapis.com/auth/drive.file");