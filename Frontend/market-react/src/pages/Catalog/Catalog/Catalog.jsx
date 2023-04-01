import React, {useEffect, useState} from 'react';
import Server from "../../../API/Server";
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

    return (
        <div className={styles.Catalog}>
            <div>
                <Filter/>
            </div>
            <div>
                <div>SOME TEXT</div>
                <ItemsList items={items}/>
            </div>
        </div>
    );
};

export default Catalog;