import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import CartElement from "./CartElement";


const Cart = () => {
    const [items, setItems] = useState([])

    useEffect(() => {
        getCartItems()
    }, [])

    async function getCartItems() {
        const response = await Server.getCartItems()
        setItems(response.data)
        console.log(response.data)
    }

    function deleteItem(indx) {
        let copy = [...items]
        copy.splice(indx, 1)
        setItems(copy)
    }

    return (
        <div>
            {
                items.map((item, index) =>
                    <CartElement
                        item={item}
                        index={index}
                        key={index}
                        deleteItem={deleteItem}
                    />
                )
            }
        </div>
    );
};

export default Cart;