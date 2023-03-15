import React from 'react';
import MinMaxNumber from "../../components/MinMaxNumber/MinMaxNumber";


const Filter = ({params}) => {

    function getFilter(value) {
        let filterMap = new Map([
            ["number", <MinMaxNumber name={"test"}/>],
        ]);
        return filterMap.get(value)
    }
    return (
        <div>
            {params ?
                (<div>
                    {Object.entries(params).map(([k,v]) =>
                    <div key={k}>{getFilter(v)}</div>)}
                </div>):
                (<div></div>)
            }
        </div>
    );
};

export default Filter;

