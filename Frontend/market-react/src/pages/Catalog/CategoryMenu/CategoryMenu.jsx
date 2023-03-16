import React, {useEffect, useState} from 'react';
import styles from './CategoryMenu.module.css'
import Server from "../../../API/Server";
import CategoryElement from "./CategoryElement";

const CategoryMenu = () => {
    const [cats,  setCats] = useState([])

    useEffect(() => {
        getCats()
    }, [])

    async function getCats() {
        const response = await Server.getCats()
        setCats(response)
    }

    return (
        <div className={styles.container}>
            {cats.map(cat =>
               <CategoryElement cat={cat} key={cat.pk}/>
            )}
        </div>
    );
};

export default CategoryMenu;