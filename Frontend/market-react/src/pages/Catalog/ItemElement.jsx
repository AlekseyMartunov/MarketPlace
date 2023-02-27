import React from 'react';
import styles from './Catalog.module.css'
import MyButton from "../../components/myButton/MyButton";
import Images from "./Images";
import Description from "./Description";
import Rating from "./Rating";

const ItemElement = (props) => {
    return (
        <div className={styles.Item_element}>
            <Images photos={props.item.images}/>
            <Description item={props.item}/>
            <Rating/>
            <MyButton>Подробнее...</MyButton>
        </div>
    );
};

export default ItemElement;

