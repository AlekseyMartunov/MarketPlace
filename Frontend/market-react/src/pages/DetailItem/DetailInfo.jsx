import React from 'react';
import style from "./DetailItem.module.css"
const DetailInfo = ({item}) => {
    return (
        <div>
            <div className={style.info_conteiner}>
                ЦЕНА: {item.price}
            </div>
            <div className={style.info_conteiner}>
                КОЛИЧЕСТВО: {item.amount}
            </div>
            <div className={style.info_conteiner}>
                <p>МАГАЗИН:</p> {item.shop_name}
            </div>
            <div className={style.info_conteiner}>
                rating
            </div>
            <div className={style.info_conteiner}>
                <p>ТОВАР ОПУБЛИКОВАН:</p>
                {item.created_time}
            </div>
        </div>
    );
};

export default DetailInfo;