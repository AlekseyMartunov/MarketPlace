import React from 'react';
import Server from "../API/Server";

const Catalog = () => {
    async function getItems() {
       const responce = await Server.getItems()
        console.log(responce)
    }

    return (
        <div>
            <button onClick={getItems}>GET DATA</button>
        </div>
    );
};

export default Catalog;