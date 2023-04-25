import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemsList from "./ItemsList";
import styles from "./Catalog.module.css";
import Filter from "./Filter";


const Catalog = (props) => {
    const [items, setItems] = useState([])

    useEffect(() => {
        getItems()
    }, [])

    async function getItems() {
        const response = await Server.getItems()
        setItems(response)
    }

    async function getItemsByURLParams(slug_cat, queryParams) {
        const response = await Server.getItems(slug_cat, queryParams)
        setItems(response)
    }

    return (
        <div className={styles.Catalog}>
            <Filter getItemsByURLParams={getItemsByURLParams}/>
            <ItemsList items={items}/>
        </div>
    );
};

export default Catalog;