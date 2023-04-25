import React, {useEffect} from 'react';
import style from "./Catalog.module.css"


const SelectedCat = ({cat}) => {

    return (
        <div className={style.Selected__cat}>
            <p>выбранная категория:</p>
            {cat.name}
        </div>

    );
};

export default SelectedCat;