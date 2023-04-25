import React from 'react';
import style from "./Catalog.module.css"
import { useNavigate } from "react-router-dom";

const SelectCat = () => {
    const navigate = useNavigate()

    function goToPreviousPage() {
        navigate("/catalog")
    }
    return (
        <div className={style.SelectCat}
             onClick={goToPreviousPage}
        >
            Выбрать другую категорию
        </div>
    );
};

export default SelectCat;