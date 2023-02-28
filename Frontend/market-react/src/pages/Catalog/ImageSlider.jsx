import React, {useState} from 'react';
import styles from "./Catalog.module.css";
import {TfiAngleDoubleLeft, TfiAngleDoubleRight} from 'react-icons/tfi';

const ImageSlider = ({photos}) => {
    const [currentImg, setCurrentImg] = useState(0);
    const maxlength = photos.length;

    function increase() {
        if (currentImg + 1 === maxlength) {
            setCurrentImg(0)
        }
        else {
            setCurrentImg(currentImg + 1)
        }
    }

    function decrease() {
        if (currentImg === 0) {
            setCurrentImg(maxlength -1)
        }
        else {
            setCurrentImg(currentImg - 1)
        }
    }

    function setIndex(indx) {
        setCurrentImg(indx)
    }

    return (
        <div>
            <div className={styles.ImageSlider__imageContainer}>
                <TfiAngleDoubleLeft
                    className={styles.ImageSlider__icon}
                    onClick={decrease}
                />
                <img className={styles.ImageSlider} src={photos[currentImg]}/>
                <TfiAngleDoubleRight
                    className={styles.ImageSlider__icon}
                    onClick={increase}
                />
            </div>
            <div className={styles.ImageSlider__dotsContainer}>
                {photos.map((img, index) => (
                    <div
                        className={index === currentImg ?
                            styles.ImageSlider__dots + " " + styles.ImageSlider__dots__selected
                            : styles.ImageSlider__dots}
                        key={index}
                        onClick={() => setCurrentImg(index)}
                    >•</div>
                ))}
            </div>
        </div>
    );
};

export default ImageSlider;