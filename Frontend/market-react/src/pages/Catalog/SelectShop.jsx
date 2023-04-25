import React, {useEffect, useState} from 'react';
import Server from "../../API/Server";
import styles from "./Catalog.module.css";
import {useLocation, useSearchParams} from "react-router-dom";


const SelectShop = ({currCategory}) => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [shops, setShops] = useState([]);
    const [shop, setShop] = useState("Выберите Магазин")
    const { state } = useLocation();

    useEffect(() => {
        getShops()
    }, [])

    async function getShops() {
        const response = await Server.getShops(state.cat.slug)
        setShops(response)
    }

    function selectShop(el) {
        updateShopParams(el.slug)
    }

    function updateShopParams(value) {
        const queryParams = {}
        for (const entry of searchParams.entries()) {
            queryParams[entry[0]] = entry[1]
        }
        queryParams["shop"] = value
        setSearchParams(queryParams)
    }

    function getCurrentShopName() {
        const shop_slug = searchParams.get("shop")
        var i ;
        for(i=0; i < shops.length; i++){
            if (shops[i].slug === shop_slug){
                return shops[i].name
            }
        }
        return "Магазин не выбран..."
    }

    return (
        <div>
            <div className={styles.Filter__Header}>
                Магазин:
            </div>
            <div className={styles.Shop__dropdown}>
                <div className={styles.Shop__current_shop}>
                    {getCurrentShopName()}
                </div>
                <div className={styles.Shop__dropdown_content}>
                    {shops.map(el =>
                        <li key={el.pk}
                            onClick={() => selectShop(el)}
                        >
                            {el.name}
                        </li>
                    )}
                </div>
            </div>
        </div>
    );
};

export default SelectShop;