import React, {useEffect, useState} from 'react';
import { useSearchParams } from "react-router-dom";
import styles from "./Catalog.module.css";

const FilterByParams = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [params, setParams] = useState({})

    useEffect(() => {
        updateAllFields()
    }, [])

    function updateAllFields() {
        if (searchParams.get("rating")) updateRating(searchParams.get("rating"))
        if (searchParams.get("min_price")) updateMinPrice(searchParams.get("min_price"))
        if (searchParams.get("max_price")) updateMaxPrice(searchParams.get("max_price"))
    }

    function updateRating(value) {
        params.rating = value
        setSearchParams(params)
    }

    function updateMinPrice(value) {
        params.min_price = value
        setSearchParams(params)
    }

    function updateMaxPrice(value) {
        params.max_price = value
        setSearchParams(params)
    }

    return (
        <div>
            <div className={styles.Filter__inputHeader}>Цена</div>
            <div className={styles.Filter__inputBox}>
                <input
                    onChange={(e) => updateMinPrice(e.target.value)}
                    type="text"
                    placeholder="цена от"
                    value={searchParams.get("min_price") || ""}
                />
                <input
                    onChange={(e) => updateMaxPrice(e.target.value)}
                    type="text"
                    placeholder="цена до"
                    value={searchParams.get("max_price") || ""}
                />
            </div>
            <div className={styles.Filter__inputHeader}>Минимальный рейтинг</div>
            <div className={styles.Filter__inputBox}>
                <input
                    onChange={(e) => updateRating(e.target.value)}
                    type="range"
                    min="0"
                    max="5"
                    step="0.1"
                    value={searchParams.get("rating") || 0}/>
            </div>
            <div className={styles.Filter__rating}>
                {searchParams.get("rating") || 0}
            </div>
        </div>
    );
};

export default FilterByParams;