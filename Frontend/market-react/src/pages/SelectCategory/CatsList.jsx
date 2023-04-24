import React, {useEffect, useState} from 'react';
import style from "./SelectCategory.module.css";

const CatsList = ({currentCat, allcats, index, navigate}) => {
    const [cats, setCats] = useState([])
    const [open, setOpen] = useState(false)
    const [nextPage, setNextPage] = useState(false)


    function getSubCats() {
        let catsArr = []
        for (const el of Object.entries(allcats)) {
            if (el[1].parent === currentCat.pk) {
                catsArr.push(el[1])
            }
        }
        if (catsArr.length === 0){
            navigate(currentCat.slug)
        } else {
            setCats(catsArr)
            setOpen(!open)
        }
    }

    return (
        <div>
            <div className={style.header}
                 onClick={getSubCats}>
                {currentCat.name}
            </div>
            {cats.map((subCat) => (
                subCat.parent === currentCat.pk && open
                    ? (<div
                        key={subCat.pk}
                        className={style.subCatContent}
                    >

                        <CatsList
                            navigate={navigate}
                            currentCat={subCat}
                            allcats={allcats}
                            index={index + 1}
                        />
                    </div>)
                    : null
            ))}
        </div>
    );
};

export default CatsList;