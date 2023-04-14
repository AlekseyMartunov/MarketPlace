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

    async function getURL(url) {
        const response = await Server.getItems(url)
        setItems(response)
    }

    return (
        <div className={styles.Catalog}>
            <Filter getURL={getURL}/>
            <ItemsList items={items}/>
        </div>
    );
};

export default Catalog;