import React, {useState} from 'react';
import styles from "./Catalog.module.css";
import FilterByParams from "./FilterByParams";

const Filter = () => {
    return (
        <div className={styles.Filter__contend}>
            <FilterByParams/>
            <div>сортировка</div>
            <div>выбор магазина</div>
            <div>выбор категории</div>
        </div>
    );
};

export default Filter;