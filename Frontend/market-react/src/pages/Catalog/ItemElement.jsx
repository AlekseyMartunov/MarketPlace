import React from 'react';
import styles from './Catalog.module.css'
import MyButton from "../../components/myButton/MyButton";
import Images from "./Images";
import Description from "./Description";
import Rating from "./Rating";

const ItemElement = (props) => {
    return (
        <div className={styles.Item_element}>
            <Images photos={'http://127.0.0.1:8000/media/photos/2023/02/24/some_image.jpg'}/>
            <Description item={props.item}/>
            <Rating/>
            <MyButton>Подробнее...</MyButton>
        </div>
    );
};

export default ItemElement;

