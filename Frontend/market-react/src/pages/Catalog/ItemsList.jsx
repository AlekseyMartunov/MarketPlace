import React from 'react';
import ItemElement from "./ItemElement";
import styles from "./Catalog.module.css";


const ItemsList = ({items}) => {
    return (
        <div className={styles.ItemList}>
            {items.map(item =>
                <ItemElement item={item} key={item.pk}/>
            )}
        </div>
    );
};

export default ItemsList;

