import React from 'react';
import ItemElement from "./ItemElement";

const ItemsList = ({items}) => {
    return (
        <div>
            {items.map(item =>
                <ItemElement item={item} key={item.pk}/>
            )}
        </div>
    );
};

export default ItemsList;