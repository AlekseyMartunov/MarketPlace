import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemsList from "./ItemsList";
import styles from "./Catalog.module.css";
import Filter from "./Filter";
import {useLocation} from "react-router-dom";


const Catalog = (props) => {
    const [items, setItems] = useState([])
    const location = useLocation()
    // не знаю почему, но это работает
    const [cat] = useState(location.state ?  (location.state.cat) : 1)

    useEffect(() => {
        getItems()
    }, [])

    async function getItems() {
        const response = await Server.getItems(cat.slug)
        setItems(response)
    }

    async function getItemsByURLParams(slug_cat, queryParams) {
        const response = await Server.getItems(slug_cat, queryParams)
        setItems(response)
    }

    return (
        <div className={styles.Catalog}>
            <Filter getItemsByURLParams={getItemsByURLParams} selectedCat={cat}/>
            <ItemsList items={items}/>
        </div>
    );
};

export default Catalog;