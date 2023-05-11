import React, {useState} from 'react';
import style from "./DetailItem.module.css"
import Server from "../../API/Server";

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


const AddInbacket = ({item}) => {
    const [amount, setAmount] = useState(1);
    const notify = () => toast.success('Товар в корзине', {
        position: "top-center",
        autoClose: 500,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "light",
    });

    async function AddInBasket() {
        const response = await Server.cartCache(
            {
                'name': item.name,
                'amount': amount,
                'price': item.price,
                'slug':item.slug,
                'img': item.images[0]
            }
        )
        if (response.statusText === "Created") {
            notify()
        }
    }

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
                <button onClick={AddInBasket}>
                    Добавить в корзину
                </button>
                <ToastContainer
                    position="top-center"
                    autoClose={500}
                    hideProgressBar
                    newestOnTop={false}
                    closeOnClick
                    rtl={false}
                    pauseOnFocusLoss
                    draggable
                    pauseOnHover
                    theme="light"
                />
            </div>
        </div>
    );
};

export default AddInbacket;