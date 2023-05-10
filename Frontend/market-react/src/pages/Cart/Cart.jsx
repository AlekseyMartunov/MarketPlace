import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemElement from "../Catalog/ItemElement";

const Cart = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        getCartItems()
    }, [])

    async function getCartItems() {
        const response = await Server.getCartItems()
        // setItems(response)
        console.log(response)
    }


    return (
        <div>
            {
                items.map((item) =>
                    <div>11</div>
            )}
        </div>
    );
};

export default Cart;