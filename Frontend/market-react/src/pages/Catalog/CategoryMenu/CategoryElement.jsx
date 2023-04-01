import React, {useState} from 'react';
import styles from "./CategoryMenu.module.css"
import {useNavigate} from 'react-router-dom';

const CategoryElement = ({cat}) => {

    const navigate = useNavigate();


    async function getCats(cat) {
        navigate(`/catalog/${cat.slug}`)
    }

    return (
        <div className={styles.element}
        onClick={() => getCats(cat)}>
            {cat.name}
        </div>
    );
};

export default CategoryElement;