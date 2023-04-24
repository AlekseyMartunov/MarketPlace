import React, {useEffect, useState} from 'react';
import { useNavigate } from "react-router-dom";
import Server from "../../API/Server";
import CatsList from "./CatsList";
import style from "./SelectCategory.module.css"

const SelectCategory = () => {
    const navigate = useNavigate()
    const [cats, setCats] = useState([])

    const index = 0

    useEffect(() => {
        getCats()
    }, [])

    async function getCats() {
        const response = await Server.getCats()
        setCats(response)
    }

    function goToNextPage(cat) {
        navigate(`/catalog/${cat.slug}`, {state: {cat: cat}})
    }

    return (
        <div className={style.mainList}>
            <p className={style.mainHeader}>Какая категория вам интересна ?</p>
            {cats.map((cat) => (
                cat.parent === null
                    ? (<div
                            key={cat.pk}
                            className={style.subCatContent}
                        >
                           <CatsList
                               navigate={goToNextPage}
                                currentCat={cat}
                                allcats={cats}
                                index={index + 1}
                            />
                        </div>
                    )
                    : null
            ))}
        </div>
    );
};

export default SelectCategory;