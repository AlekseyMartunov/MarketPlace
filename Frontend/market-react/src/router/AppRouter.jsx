import React, {useContext} from 'react';
import {Route, Routes} from "react-router-dom";
import {routes, routesAuthorized} from "./index";
import {AuthContext} from "../context";


const AppRouter = () => {
    const {isAuth, setIsAuth} = useContext(AuthContext)

    return (
        <Routes>
            {
                isAuth ? (
                    routesAuthorized.map((route, indx) =>
                        <Route
                            key={indx}
                            path={route.link}
                            element={route.component}
                        />)
                ) : (
                    routes.map((route, indx) =>
                    <Route
                        key={indx}
                        path={route.link}
                        element={route.component}
                    />)
                )
            }
        </Routes>
    );
};

export default AppRouter;


