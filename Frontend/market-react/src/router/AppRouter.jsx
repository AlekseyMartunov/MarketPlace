import React, {useContext} from 'react';
import {AuthContext} from "../context";
import AuthorizedRouters from "./AuthorizedRouters"
import NoAuthorizedRouters from "./NoAuthorizedRouters"


const AppRouter = () => {
    const {isAuth, setIsAuth} = useContext(AuthContext)

    return (
        <div>{
            isAuth ? (
                <AuthorizedRouters/>
            ) : (
                <NoAuthorizedRouters/>
            )
        }
        </div>
    );
};

export default AppRouter;


