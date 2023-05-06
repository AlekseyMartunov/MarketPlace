import React from 'react';
import styles from "./Login.module.css";
import {useNavigate} from "react-router-dom";

const Registration = () => {
    const navigate = useNavigate()
     function authorization() {
        navigate("/authorization")
     }

    return (
        <div className={styles.content}>
            <p className={styles.text}>Создайте аккаунт</p>
            <div className={styles.input_field}>
                <input
                    type="text"
                    placeholder="Имя пользователя">
                </input>
            </div>
            <div className={styles.input_field}>
                <input
                    type="password"
                    placeholder="Пароль">
                </input>
            </div>
            <div className={styles.input_field}>
                <input
                    type="password"
                    placeholder="Пароль еще раз">
                </input>
            </div>
            <div className={styles.input_field}>
                <input
                    type="email"
                    placeholder="Email">
                </input>
            </div>
            <button className={styles.button}>Создать профиль</button>
            <button
                className={styles.button}
                onClick={authorization}
            >Есть аккаунт? Войдите
            </button>
        </div>
    );
};

export default Registration;