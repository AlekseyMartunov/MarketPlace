import React, {useEffect, useState} from 'react';
import styles from "./Catalog.module.css";
import {useSearchParams} from "react-router-dom";



const Ordering = () => {
    const [searchParams, setSearchParams] = useSearchParams();

    // useEffect(() => {
    //
    // }, [])

    function updateOrderingParams(value) {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        queryParams["order"] = value
        setSearchParams(queryParams)
    }

    return (
        <div className={styles.Ordering__content}>
            <p className={styles.Ordering__header}>Сортировка:</p>
            <div className={styles.Ordering__content_box}>
                <input type="radio" id="Ordering"
                       name="ord" value="price"
                       onChange={(e) =>updateOrderingParams(e.target.value)}
                       checked={searchParams.get("order") === "price"}
                />
                <label htmlFor="contactChoice1">По возрастанию цены</label>
            </div>
            <div className={styles.Ordering__content_box}>
                <input type="radio" id="Ordering"
                       name="ord" value="-price"
                       onChange={(e) =>updateOrderingParams(e.target.value)}
                       checked={searchParams.get("order") === "-price"}
                />
                <label htmlFor="contactChoice1">По убыванию цены</label>
            </div>
            <div className={styles.Ordering__content_box}>
                <input type="radio" id="Ordering"
                       name="ord" value="rating"
                       onChange={(e) =>updateOrderingParams(e.target.value)}
                       checked={searchParams.get("order") === "rating"}
                />
                <label htmlFor="contactChoice1">По возрастанию рейтинга</label>
            </div>
            <div className={styles.Ordering__content_box}>
                <input type="radio" id="Ordering"
                       name="ord" value="-rating"
                       onChange={(e) =>updateOrderingParams(e.target.value)}
                       checked={searchParams.get("order") === "-rating"}
                />
                <label htmlFor="contactChoice1">По убыванию рейтинга</label>
            </div>

        </div>
    );
};

export default Ordering;