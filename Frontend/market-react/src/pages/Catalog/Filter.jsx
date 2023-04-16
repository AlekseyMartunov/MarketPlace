import React, {useState} from 'react';
import styles from "./Catalog.module.css";
import FilterByParams from "./FilterByParams";
import {useSearchParams} from "react-router-dom";


const Filter = ({getItemsByURLParams}) => {
    const [searchParams, setSearchParams] = useSearchParams();

    function resetFilter() {
        setSearchParams({})
    }

    function search() {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        getItemsByURLParams(queryParams)
    }

    return (
        <div className={styles.Filter__contend}>
            <FilterByParams/>
            <div>сортировка</div>
            <div>выбор магазина</div>
            <div>выбор категории</div>
            <div className={styles.Filter__button_space}>
               <button
                   className={styles.Filter__button_search}
                   onClick={search}
               >
                   Поиск
               </button>
                <button
                    className={styles.Filter__button_reset}
                    onClick={resetFilter}
                >
                    Сбросить Фильтр
                </button>
            </div>
        </div>
    );
};

export default Filter;