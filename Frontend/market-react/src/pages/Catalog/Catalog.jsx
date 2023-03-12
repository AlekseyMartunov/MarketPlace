import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import ItemsList from "./ItemsList";
import СategoriesMenu from "./СategoriesMenu";
import styles from "./Catalog.module.css";
import CategoryList from "./CategoryList";


const Catalog = () => {
    const [items, setItems] = useState([])
    const [cats, setCats] = useState([])
    const [catsList, setCatsList] = useState([])

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
        setCats(response)
    }

    function setSubCatsList(catsList) {
        setCats(catsList)
    }

    function addIntoCatsList(cat) {
        setCatsList([...catsList, cat])
    }

    return (
        <div className={styles.Catalog}>
            <СategoriesMenu
                cats={cats}
                setSubCatsList={setSubCatsList}
                addIntoCatsList={addIntoCatsList}
            />
            <div>
                <CategoryList cats={catsList}/>
                <ItemsList items={items}/>
            </div>
        </div>
    );
};

export default Catalog;