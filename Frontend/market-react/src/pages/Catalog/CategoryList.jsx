import React from 'react';
import styles from "./Catalog.module.css";

const CategoryList = ({cats, clearList}) => {
    return (
        <div>
        {cats.length > 0 ? (
                <div className={styles.CategoryList}>
                    <div>{cats.join(" \\ ")}</div>
                </div>
            ):(
            <div className={styles.CategoryList}>
                Выберите категори....
            </div>
            )}
        </div>
    );
};

export default CategoryList;

