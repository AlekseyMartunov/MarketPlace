import React, {useState} from 'react';
import styles from "./Catalog.module.css";
import Server from "../../API/Server";
import Filter from "./Filter";



const CategoriesMenu = ({cats, setSubCatsList, addIntoCatsList, clearCatList}) => {
    const [header, setHeader] = useState("")
    const [allowedParams, setAllowedParams] = useState([])

    async function getSubCats(cat) {
        const response = await Server.getCats(cat.slug)
        setSubCatsList(response)
        addIntoCatsList(cat.name)
        setHeader(cat.name)
        setAllowedParams(cat.allowed_params)
        console.log(cat.allowed_params)
    }

    function clearHeader() {
        setHeader("")
        clearCatList()
    }

    return (
        <div>
        <div className={styles.CategoruMenu}>
            <div className={styles.CategoryHeader}>{header}</div>
            {cats.map(cat =>
                <div
                    key={cat.pk}
                    className={styles.CategoryElement}
                    onClick={() => getSubCats(cat)}
                >
                    {cat.name}
                </div>
            )}
            <div
                className={styles.CategoryBack}
                onClick={() => clearHeader()}
            >
                Назад
            </div>
        </div>
            <Filter params={allowedParams}/>
        </div>
    );
};

export default CategoriesMenu;