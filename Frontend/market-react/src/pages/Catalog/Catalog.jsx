import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemsList from "./ItemsList";
import CategoruMenu from "./CategoruMenu";
import styles from "./Catalog.module.css";


const Catalog = () => {
    const [items, setItems] = useState([])

    useEffect(() => {
        getItems()
        getCats()
    }, [])

    async function getItems() {
        const response = await Server.getItems()
        setItems(response)
    }

    async function getCats() {
        const response = await Server.getCats()
        setItems(response)
        console.log(response)
    }

    return (
        <div className={styles.Catalog}>
            <CategoruMenu/>
            <ItemsList items={items}/>
        </div>
    );
};

export default Catalog;