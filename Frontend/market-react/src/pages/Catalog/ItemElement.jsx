import React from 'react';
import styles from './Catalog.module.css'
import ItemsList from "./ItemsList";

const ItemElement = (props) => {
    return (
        <div className={styles.content}>
            <img className={styles.img} src='http://127.0.0.1:8000/media/photos/2023/02/24/some_image.jpg'/>
            <div className={styles.text}>
                <div className={styles.name}>{props.item.name}</div>
                <div className={styles.info_box}>
                    <div className={styles.info_right}>Продавец: </div>
                    <div className={styles.info_left}>{props.item.shop}</div>
                </div>
                <div className={styles.info_box}>
                    <div className={styles.info_right}>Товаров осталось: </div>
                    <div className={styles.info_left}>{props.item.amount}</div>
                </div>

                <div>ТУТ БУДЕТ Информация о покупках</div>
                <div>ТУТ БУДЕТ РЕЙТИНГ</div>
            </div>
            <button className={styles.button}>Подробнее...</button>


        </div>
    );
};

export default ItemElement;

// "images": [{
//     "photos": "/media/photos/2023/02/24/some_image.jpg"
// }]