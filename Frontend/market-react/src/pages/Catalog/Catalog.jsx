import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemsList from "./ItemsList";
import styles from "./Catalog.module.css";
import Filter from "./Filter";
import {useLocation} from "react-router-dom";


const Catalog = (props) => {
    const [items, setItems] = useState([])
    const { state } = useLocation();


    useEffect(() => {
        getItems()
        console.log(state.cat)
    }, [])

    async function getItems() {
        const response = await Server.getItems()
        setItems(response)
    }

    async function getItemsByURLParams(queryParams) {
        const response = await Server.getItems(queryParams)
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