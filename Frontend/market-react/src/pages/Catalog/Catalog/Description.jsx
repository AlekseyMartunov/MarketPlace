import React from 'react';
import styles from './Catalog.module.css'
const Description = ({item}) => {
    return (
        <div>
            <div className={styles.Description__name}>{item.name}</div>
            <div className={styles.Description__content}>
                <div className={styles.Description__element}>Продавец:</div>
                <div className={styles.Description__element}>{item.shop}</div>
            </div>
            <div className={styles.Description__content}>
                <div className={styles.Description__element}>Осталось:</div>
                <div className={styles.Description__element}>{item.amount}</div>
            </div>
            <div className={styles.Description__content}>
                <div className={styles.Description__element}>Цена:</div>
                <div className={styles.Description__element}>{item.price}</div>
            </div>
        </div>
    );
};

export default Description;

