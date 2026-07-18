// Paste the config object from Firebase console (Project settings > General > Your apps > SDK setup)
// Make sure "databaseURL" is included -- that only shows up once you've created a Realtime Database.
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDTx6hopDgTmqg3sYJZzt_2d8_ryu4ogzo",
  authDomain: "wc26-stickers.firebaseapp.com",
  databaseURL: "https://wc26-stickers-default-rtdb.firebaseio.com",
  projectId: "wc26-stickers",
  storageBucket: "wc26-stickers.firebasestorage.app",
  messagingSenderId: "1096919061369",
  appId: "1:1096919061369:web:d1ea60757ede442a0ad5a8"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);