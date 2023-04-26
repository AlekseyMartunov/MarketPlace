import React, {useState} from 'react';
import style from "./DetailItem.module.css"

const AddInbacket = ({item}) => {
    const [amount, setAmount] = useState(1);

    function increase() {
        if (item.amount > amount){
            setAmount(amount + 1)
        }
    }

    function decrease() {
        if (amount >= 2) {
            setAmount(amount - 1)
        }
    }

    function setValue(e) {
        const value = parseInt(e.target.value, 10)
        if (Number.isInteger(value) && 1 <= value && value <= item.amount) {
            setAmount(value)
        }
    }

    return (
        <div>
            <div className={style.info_conteiner}>
                <div>КОЛИЧЕСТВО:</div>
                <button
                    onClick={decrease}
                    className={style.AddInbacket_button}
                >-</button>
                <input
                    className={style.AddInbacket_input}
                    value={amount}
                    onChange={(e) => setValue(e)}
                    name="amount"
                />
                <button
                    onClick={increase}
                    className={style.AddInbacket_button}
                >+</button>
                <p>CТОИМОСТЬ: {item.price * amount}</p>
            </div>
            <div className={style.AddInbacket_send}>
                <button>
                    Добавить в корзину
                </button>
            </div>
        </div>
    );
};

export default AddInbacket;