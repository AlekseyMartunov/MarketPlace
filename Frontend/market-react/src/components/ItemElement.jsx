import React from 'react';

const ItemElement = (props) => {
    return (
        <div className="ItemElement__contend">
            <p>{props.item.name}</p>
            <p>{props.item.amout}</p>
            <p>{props.item.shop}</p>
            <img src='http://127.0.0.1:8000/media/photos/2023/02/24/some_image.jpg'/>
            <p>{props.item.images[0]['photos']}</p>

        </div>
    );
};

export default ItemElement;

// "images": [{
//     "photos": "/media/photos/2023/02/24/some_image.jpg"
// }]