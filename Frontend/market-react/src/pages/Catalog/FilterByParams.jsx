import React, {useState} from 'react';
import styles from "./Catalog.module.css";

const FilterByParams = () => {
    const [rating, setRating] = useState(0)
    const [minPrice, setMinPrice] = useState(0)
    const [maxPrice, setMaxPrice] = useState(9999999999)

    function updateRating(event) {
        setRating(event.target.value)
    }

    function updateMinPrice(event) {
        setMinPrice(event.target.value)
    }

    function updateMaxPrice(event) {
        setMaxPrice(event.target.value)
    }

    return (
        <div>
            <div className={styles.Filter__inputHeader}>Цена</div>
            <div className={styles.Filter__inputBox}>
                <input
                    onChange={updateMinPrice}
                    type="text"
                    placeholder="цена от"
                />
                <input
                    onChange={updateMaxPrice}
                    type="text"
                    placeholder="цена до"
                />
            </div>
            <div className={styles.Filter__inputHeader}>Минимальный рейтинг</div>
            <div className={styles.Filter__inputBox}>
                <input
                    onChange={updateRating}
                    type="range"
                    min="0"
                    max="5"
                    step="0.1"/>
            </div>
            <div className={styles.Filter__rating}>
                {rating}
            </div>
        </div>
    );
};

export default FilterByParams;