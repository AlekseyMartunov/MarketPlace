import React, {useContext} from 'react';
import Server from "../../API/Server";
import {AuthContext} from "../../context";

const Logout = () => {
    const {isAuth, setIsAuth} = useContext(AuthContext)
    async function logout() {
        try {
            const token_refresh = localStorage.getItem('token_refresh')
            let token = {}
            token['refresh'] = token_refresh
            const responce = await Server.logout(token)

            localStorage.removeItem('token_refresh')
            localStorage.removeItem('token_access')
            localStorage.removeItem('userName')

            setIsAuth(false)

        } catch (e) {
            console.log(e.response)
        }

    }
    return (
        <div onClick={logout}>
            LOGOUT
        </div>
    );
};

export default Logout;