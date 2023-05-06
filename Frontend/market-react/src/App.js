import React, {useEffect, useState} from "react";
import AppRouter from "./router/AppRouter";
import { BrowserRouter } from "react-router-dom";
import Navbar from "./components/navbar/Navbar";
import {AuthContext} from "./context";


function App() {
    const [isShopOwner, setShopOwner] = useState(true)
    const [userName, setUserName] = useState("7585")

    useEffect(() => {
        checkValues()
    }, [])

    function checkValues() {
        const name = localStorage.getItem("userName")
        if (name !== "") {
            setUserName(name)
        }
    }

  return (
      <AuthContext.Provider value ={{
          shop: [isShopOwner, setShopOwner],
          name: [userName, setUserName]
      }}>
          <BrowserRouter>
              <Navbar/>
              <AppRouter/>
          </BrowserRouter>
      </AuthContext.Provider>
  );
}

export default App;
