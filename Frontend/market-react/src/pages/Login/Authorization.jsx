import React, {useContext, useState} from 'react';
import styles from "./Login.module.css"
import Server from "../../API/Server";
import {useNavigate} from "react-router-dom";
import {AuthContext} from "../../context";

const Authorization = () => {
    const navigate = useNavigate()
    const {isAuth, setIsAuth} = useContext(AuthContext)

    const [userName, setUserName] = useState("")
    const [password, setPassword] = useState("")

    function registration() {
        navigate("/registration")
    }

    async function authorization() {
        try {
            let userData = {}

            userData['password'] = password
            userData['username'] = userName
            const response = await Server.authorization(userData)

            localStorage.setItem('token_refresh', response.data.refresh)
            localStorage.setItem('token_access', response.data.access)

            const name = parseJwt(response.data.access)['name']
            localStorage.setItem('userName', name)
            setIsAuth(true)

            navigate(`/catalog`)
        } catch (e) {
            console.log(e.response)
        }
    }

    function parseJwt(token) {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace('-', '+').replace('_', '/');
        return JSON.parse(window.atob(base64));
    }

    return (
        <div className={styles.content}>
            <p className={styles.text}>Авторизуйтесь</p>
            <div className={styles.input_field}>
                <input
                    onChange={(e) => setUserName(e.target.value)}
                    type="text"
                    placeholder="Имя пользователя"
                    value={userName}
                />
            </div>
            <div className={styles.input_field}>
                <input
                    onChange={(e) => setPassword(e.target.value)}
                    type="password"
                    placeholder="Пароль"
                    value={password}
                />
            </div>
            <button
                className={styles.button}
                onClick={authorization}
            > Вход
            </button>
            <button
                className={styles.button}
                onClick={registration}
            > Нет аккаунта? Создайте
            </button>
        </div>
    );
};

export default Authorization;