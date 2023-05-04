import React from 'react';
import styles from './Catalog.module.css'
import ImageSlider from "./ImageSlider";
import Description from "./Description";
import Rating from "./Rating";
import {useNavigate} from "react-router-dom";

const ItemElement = (props) => {
    const navigate = useNavigate()

    function aboutItem() {
        navigate(`/about-item/${props.item.slug}`)
    }
    return (
        <div className={styles.Item_element}>
            <ImageSlider photos={props.item.images}/>
            <Description item={props.item}/>
            <Rating/>
            <div className={styles.button}
                onClick={aboutItem}
            >
                Подробнее...
            </div>
        </div>
    );
};

export default ItemElement;

