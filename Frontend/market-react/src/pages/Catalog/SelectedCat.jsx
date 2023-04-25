import React, {useEffect} from 'react';
import {useLocation} from "react-router-dom";
import style from "./Catalog.module.css"


const SelectedCat = () => {
    const { state } = useLocation();

    return (
        <div className={style.Selected__cat}>
            <p>выбранная категория:</p>
            {state.cat.name}
        </div>
    );
};

export default SelectedCat;