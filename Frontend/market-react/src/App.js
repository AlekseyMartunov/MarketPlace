import React, {useEffect, useState} from "react";
import AppRouter from "./router/AppRouter";
import { BrowserRouter } from "react-router-dom";
import Navbar from "./components/navbar/Navbar";
import {AuthContext} from "./context";


function App() {
    const [isAuth, setIsAuth] = useState(false)

    useEffect(() => {
        checkValue()
    }, [])

    function checkValue() {
        if (localStorage.getItem('userName') !== null) {
            setIsAuth(true)
        }
    }

    return (
      <AuthContext.Provider value={{
          isAuth,
          setIsAuth
      }}>
          <BrowserRouter>
              <Navbar/>
              <AppRouter/>
          </BrowserRouter>
      </AuthContext.Provider>
    );
}

export default App;
