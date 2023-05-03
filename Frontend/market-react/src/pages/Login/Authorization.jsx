import React from 'react';
import styles from "./Login.module.css"

const Authorization = () => {
    return (
        <div>
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
            <button className={styles.button}>Вход</button>
        </div>
    );
};

export default Authorization;