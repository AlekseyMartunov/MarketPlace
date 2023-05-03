import React from 'react';
import styles from "./Login.module.css";

const Registration = () => {
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
        </div>
    );
};

export default Registration;