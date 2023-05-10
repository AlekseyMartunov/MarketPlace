import React from 'react';
import {Route, Routes} from "react-router-dom";
import {routes, } from "./index";

const NoAuthorizedRouters = () => {
    return (
        <Routes>
            {
                routes.map((route, indx) =>
                    <Route
                        key={indx}
                        path={route.link}
                        element={route.component}
                    />)
            }

        </Routes>
    );
};

export default NoAuthorizedRouters;