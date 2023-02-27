import React, {useState} from 'react';
import styles from "./Catalog.module.css";

const Images = ({photos}) => {
    const [currentImg, setCurrentImg] = useState(0);
    const maxlength = photos.length;

    function increase() {
        if (currentImg + 1 == maxlength) {
            setCurrentImg(0)
        }
        else {
            setCurrentImg(currentImg + 1)
        }
    }

    function decrease() {
        if (currentImg == 0) {
            setCurrentImg(maxlength -1)
        }
        else {
            setCurrentImg(currentImg - 1)
        }
    }

    return (
        <div>
            <button onClick={increase}>+</button>
            <button onClick={decrease}>-</button>
            <img className={styles.Images} src={photos[currentImg]}/>
            {currentImg}
        </div>
    );
};

export default Images;