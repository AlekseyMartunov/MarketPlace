import React, {useState} from 'react';
import styles from "./Catalog.module.css";
import Server from "../../API/Server";



const CategoriesMenu = ({cats, setSubCatsList, addIntoCatsList}) => {
    const [header, setHeader] = useState("")

    async function getSubCats(cat) {
        const response = await Server.getCats(cat.slug)
        setSubCatsList(response)
        addIntoCatsList(cat.name)
        setHeader(cat.name)
    }

    return (
        <div className={styles.CategoruMenu}>
            <div className={styles.CategoryHeader}>{header}</div>
            {cats.map(cat =>
                <div
                    className={styles.CategoryElement}
                    onClick={() => getSubCats(cat)}
                >
                    {cat.name}
                </div>
            )}
        </div>
    );
};

export default CategoriesMenu;