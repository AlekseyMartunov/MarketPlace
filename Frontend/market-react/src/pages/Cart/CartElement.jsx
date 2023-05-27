import React, {useEffect, useState} from 'react';
import styles from "./cart.module.css"

const CartElement = ({item, index, deleteItem, updateAmount}) => {
    const [amount, setAmount] = useState(item.amount)

    useEffect(()=>{
        updateAmount(index, amount)
    }, [amount])

    function removeItem() {
        deleteItem(index)
    }

    function increase() {
        setAmount(amount + 1)
    }

    function decrease() {
        if (amount > 1) {
            setAmount( amount - 1)
        }
    }

    return (
        <div className={styles.cart_element}>
            <span className={styles.text}>
                {index + 1}
            </span>

            <span className={styles.text}>
                {item.name}
            </span>

            <span className={styles.text}>
                <img
                    className={styles.img}
                    src={item.img}
                />
            </span>

            <span className={styles.text}>
                Кол-во: {amount}
            </span>
            <span>
                <p><button className={styles.button_amount} onClick={increase}>+</button></p>
                <p><button className={styles.button_amount} onClick={decrease}>-</button></p>
            </span>

            <span className={styles.text}>
                Цена: {item.price}
            </span>

            <span className={styles.text}>
                Суммарная стоимость: {item.price * amount}
            </span>

            <span>
                <button
                    onClick={removeItem}
                    className={styles.button}>
                    Удалить из Корзины
                </button>
            </span>
        </div>
    );
};

export default CartElement;


