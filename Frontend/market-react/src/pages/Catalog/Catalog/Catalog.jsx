import React, {useEffect, useState} from 'react';
import Server from "../../../API/Server";
import ItemsList from "./ItemsList";
import styles from "./Catalog.module.css";



const Catalog = () => {
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
                Тут будет фильтр
            </div>
            <div>
                {/*<CategoryList />*/}
                <ItemsList items={items}/>
            </div>
        </div>
    );
};

export default Catalog;