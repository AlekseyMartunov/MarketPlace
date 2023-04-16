import React, {useEffect, useState} from 'react';
import { useSearchParams } from "react-router-dom";
import styles from "./Catalog.module.css";

const FilterByParams = () => {
    const [searchParams, setSearchParams] = useSearchParams();

    function updateRating(value) {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        queryParams["rating"] = value
        setSearchParams(queryParams)
    }

    function updateMinPrice(value) {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        queryParams["min_price"] = value
        setSearchParams(queryParams)
    }

    function updateMaxPrice(value) {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        queryParams["max_price"] = value
        setSearchParams(queryParams)
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