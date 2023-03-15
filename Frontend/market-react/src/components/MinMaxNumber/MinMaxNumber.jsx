import React from 'react';
import styles from "./MinMaxNumber.module.css"
const MinMaxNumber = ({name}) => {
    return (
        <div className={styles.Info}>
            <div className={styles.Name}>{name}</div>
            <div className={styles.Container}>
                <input type={"number"} className={styles.Input}/>
                <input type={"number"} className={styles.Input}/>
            </div>
            <div className={styles.Container}>
                <div>MIN</div>
                <div>MAX</div>
            </div>
        </div>
    );
};

export default MinMaxNumber;