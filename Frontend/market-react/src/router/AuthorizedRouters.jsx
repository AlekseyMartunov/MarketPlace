import React from 'react';
import {Route, Routes, redirect} from "react-router-dom";
import { routesAuthorized} from "./index";

const AuthorizedRouters = () => {
    return (
        <Routes>
            {
                routesAuthorized.map((route, indx) =>
                <Route
                    key={indx}
                    path={route.link}
                    element={route.component}
                />)
            }
        </Routes>
    );
};

export default AuthorizedRouters;