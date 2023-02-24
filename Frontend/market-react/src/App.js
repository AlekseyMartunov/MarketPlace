import React from "react";
import AppRouter from "./router/AppRouter";
import { BrowserRouter } from "react-router-dom";
import Navbar from "./components/navbar/Navbar";


function App() {
  return (
      <BrowserRouter cla>
          <Navbar/>
          <AppRouter/>
      </BrowserRouter>

  );
}

export default App;
