import React from 'react';
import styles from "./Catalog.module.css";

const Images = ({photos}) => {
    return (
        <div>
            <img className={styles.Images} src={photos}/>
        </div>
    );
};

export default Images;