import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import CartElement from "./CartElement";
import styles from "./cart.module.css"


const Cart = () => {
    const [items, setItems] = useState([])

    useEffect(() => {
        getCartItems()
    }, [])

    async function getCartItems() {
        const response = await Server.getCartItems()
        console.log(response)
        if (response.length != 0) {
            setItems(response)

        }
    }

    async function updateItemsList(indx) {
        let copy = [...items]
        copy.splice(indx, 1)
        const response = await Server.updateCache(copy)
        setItems(response)
    }

    return (
        <div>
            <div>
                {
                    items.map((item, index) =>
                        <CartElement
                            item={item}
                            index={index}
                            key={index}
                            deleteItem={updateItemsList}
                        />
                    )
                }
            </div>
            <button className={styles.button_order}>Очистить корзину</button>
            <button className={styles.button_order}>Сделать заказ</button>
        </div>
    );
};

export default Cart;