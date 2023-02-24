import React from 'react';
import {Route, Routes} from "react-router-dom";
import {routes} from "./index";


const AppRouter = () => {
    return (
        <Routes>
            {routes.map(route =>
                <Route
                    path={route.link}
                    element={route.component}
                />
            )}
        </Routes>
    );
};

export default AppRouter;

