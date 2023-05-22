import React from 'react';
import style from "./DetailItem.module.css"
import AddInbacket from "./AddInbacket";

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
                РЕЙТИНГ: {item.rating}
            </div>
            <div className={style.info_conteiner}>
                <p>ТОВАР ОПУБЛИКОВАН:</p>
                {item.created_time}
            </div>
            <AddInbacket item={item}/>

        </div>
    );
};

export default DetailInfo;