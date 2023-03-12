import React from 'react';
import styles from "./Catalog.module.css";

const CategoryList = ({cats}) => {
    return (
        <div>
        {cats.length > 0 ? (
                <div className={styles.CategoryList}>
                    {cats.join("  -->  ")}
                </div>
            ):(
                <div></div>
            )}
        </div>
    );
};

export default CategoryList;

