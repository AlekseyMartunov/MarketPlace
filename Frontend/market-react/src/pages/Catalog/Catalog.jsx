import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemsList from "./ItemsList";

const Catalog = () => {
    const [items, setItems] = useState([])

    useEffect(() => {
        getItems()
    }, [])

    async function getItems() {
        const responce = await Server.getItems()
        setItems(responce)
        console.log(responce)
    }

    return (
        <div>
            <ItemsList items={items}/>
        </div>
    );
};

export default Catalog;