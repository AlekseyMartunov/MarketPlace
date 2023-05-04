import React, {useState} from 'react';
import styles from "./Login.module.css"
import Server from "../../API/Server";
import {useNavigate} from "react-router-dom";

const Authorization = () => {
    const navigate = useNavigate()
    const [userName, setUserName] = useState("")
    const [password, setPassword] = useState("")

    async function authorization() {
        try {
            let userData = {}
            userData['password'] = password
            userData['username'] = userName
            const response = await Server.authorization(userData)
            localStorage.setItem('token_refresh', response.data.refresh)
            localStorage.setItem('token_access', response.data.access)
            navigate(`/catalog`)
        } catch (e) {
            console.log(e.response)
        }
    }

    return (
        <div>
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
        </div>
    );
};

export default Authorization;