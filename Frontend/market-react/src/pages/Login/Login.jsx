import React, {useState} from 'react';
import styles from "./Login.module.css"
import Registration from "./Registration";
import Authorization from "./Authorization";

const Login = () => {
    const [hasAccount, setHasAccount] = useState(false)

    return (
        <div className={styles.content}>
            <p className={styles.text}>У вас уже есть аккаунт ? </p>
            <p>
                <button className={styles.button}
                        onClick={(e) => setHasAccount(true)}
                >
                    ДА
                </button>
                <button className={styles.button}
                        onClick={(e) => setHasAccount(false)}
                >
                    НЕТ
                </button>
            </p>
            {
                hasAccount ? (
                    <Authorization/>
                ) : (
                    <Registration/>
                )
            }
        </div>
    );
};

export default Login;