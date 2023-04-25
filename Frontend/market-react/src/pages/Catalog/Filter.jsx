import React, {useState} from 'react';
import styles from "./Catalog.module.css";
import FilterByParams from "./FilterByParams";
import {useLocation, useSearchParams} from "react-router-dom";
import Ordering from "./Ordering";
import SelectShop from "./SelectShop";
import SelectedCat from "./SelectedCat";
import SelectCat from "./SelectCat";


const Filter = ({getItemsByURLParams}) => {
    const [searchParams, setSearchParams] = useSearchParams();
    const { state } = useLocation();


    function resetFilter() {
        setSearchParams({})
    }

    function search() {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        getItemsByURLParams(state.cat.slug, queryParams)
    }

    return (
        <div className={styles.Filter__contend}>
            <SelectedCat/>
            <SelectCat/>
            <FilterByParams/>
            <Ordering/>
            <SelectShop/>
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