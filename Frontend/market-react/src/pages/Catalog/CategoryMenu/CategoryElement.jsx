import React, {useState} from 'react';
import Server from "../../../API/Server";
import styles from "./CategoryMenu.module.css"
import {useNavigate} from 'react-router-dom';

const CategoryElement = ({cat}) => {
    const [cats,  setCats] = useState([])
    const [head, setHead] = useState(cat.name)
    const navigate = useNavigate();


    async function getCats(cat) {
        const response = await Server.getCats(cat.slug)
        setCats(response)
        setHead(cat.name)
        if (response.length === 0) {
            navigate(`/catalog/${cat.slug}`);
        }

    }

    return (
        <div className={styles.element}>
            <div
                onClick={() => getCats(cat)}
                className={styles.head}
            >{head}</div>
            <div>
                {cats.map(cat =>
                <div
                    onClick={() => getCats(cat)}
                    className={styles.link}
                    key={cat.pk}
                >{cat.name}</div>)}
            </div>
        </div>
    );
};

export default CategoryElement;