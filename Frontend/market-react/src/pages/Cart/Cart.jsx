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
        if (response.length != 0) {
            setItems(response)
        }
    }

    async function removeItemList() {
        setItems([])
        const response = await Server.deleteCAche()
    }

    async function updateItemsList(indx) {
        let copy = [...items]
        copy.splice(indx, 1)
        const response = await Server.updateCache(copy)
        setItems(response)
    }

    async function updateAmountItems(indx, amount) {
        let copy = [...items]
        copy[indx].amount = amount
        setItems(copy)
        const response = await Server.updateCache(copy)
    }

    async function createOrder() {
        const response = await Server.createOrder()
        console.log(response)
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
                            updateAmount={updateAmountItems}
                        />
                    )
                }
            </div>
            <button
                className={styles.button_order}
                onClick={removeItemList}
            >
                Очистить корзину
            </button>
            <button
                className={styles.button_order}
                onClick={createOrder}
            >
                Сделать заказ
            </button>
        </div>
    );
};

export default Cart;