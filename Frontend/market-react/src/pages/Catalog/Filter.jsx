import React, {useEffect, useState} from 'react';
import styles from "./Catalog.module.css";
import FilterByParams from "./FilterByParams";
import {useLocation, useSearchParams} from "react-router-dom";
import Ordering from "./Ordering";
import SelectShop from "./SelectShop";
import SelectedCat from "./SelectedCat";
import SelectCat from "./SelectCat";


const Filter = ({getItemsByURLParams, selectedCat}) => {
    const [searchParams, setSearchParams] = useSearchParams();
    // const [cat] = useState(state ?  (state.cat) : 1)


    function resetFilter() {
        setSearchParams({})
    }

    function search() {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        getItemsByURLParams(selectedCat.slug, queryParams)
    }

    return (
        <div className={styles.Filter__contend}>
            <SelectedCat cat={selectedCat}/>
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