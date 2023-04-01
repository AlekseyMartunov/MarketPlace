import React, {useEffect, useState} from 'react';
import {useSearchParams} from "react-router-dom";
import { useLocation } from 'react-router-dom';
import Server from "../../../API/Server";

const Filter = () => {
    const [searchParams, setSearchParams] = useSearchParams()
    const [fields, setFields] = useState({})
    const url = useLocation()

    useEffect(() => {
        setAllowedParams(url)
    }, [])

    async function setAllowedParams() {
        const slug = url.pathname.split('/')[2]
        const response = await Server.getCats(slug)
        setFields(response[0].allowed_params)
    }

    return (
        <div>
            {Object.keys(fields).map((keyName, i) =>
                <div>
                <div key={i}>{keyName}</div>
                <div key={i+1}>{fields[keyName]['min']}</div>
                </div>
            )}
        </div>
    );
};

export default Filter;