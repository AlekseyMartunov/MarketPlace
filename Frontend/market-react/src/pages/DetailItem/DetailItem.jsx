import React, {useEffect, useState} from 'react';
import {useLocation} from "react-router-dom";
import Server from "../../API/Server";
import styles from "./DetailItem.module.css"
import DetailInfo from "./DetailInfo";
import ImageSlider from "./ImageSlider";


const DetailItem = () => {
    const location = useLocation()
    const [item, setItem] = useState({})

    useEffect(() => {
        getItem()
    }, [])

    async function getItem() {
        const slug = location.pathname.split('/')[2]
        const response = await Server.getDetailItem(slug)
        setItem(response)
        console.log(response)
    }

    return (
        <div>
            <h1 className={styles.header}>{item.name}</h1>
            <div className={styles.container}>
                <div className={styles.content}>
                    <ImageSlider images={item.images}/>
                </div>
                <div className={styles.content_info}>
                    <DetailInfo item={item}/>
                </div>
            </div>
            <div>
                {item.description}
            </div>
            <div>смотреть отзывы</div>
        </div>
    );
};

export default DetailItem;