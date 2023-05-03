import React, {useState} from 'react';
import styles from "./Login.module.css"
import Server from "../../API/Server";

const Authorization = () => {
    const [userName, setUserName] = useState("")
    const [password, setPassword] = useState("")

    function authorization() {
        let userData = {}
        userData['password'] = password
        userData['username'] = userName
        const data = Server.authorization(userData)
        // localStorage.setItem('token_refresh')
        // localStorage.setItem('token_access')
        console.log(data)
    }

    return (
        <div>
            <div className={styles.input_field}>
                <input
                    onChange={(e) => setUserName(e.target.value)}
                    type="text"
                    placeholder="Имя пользователя">
                </input>
            </div>
            <div className={styles.input_field}>
                <input
                    onChange={(e) => setPassword(e.target.value)}
                    type="password"
                    placeholder="Пароль">
                </input>
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