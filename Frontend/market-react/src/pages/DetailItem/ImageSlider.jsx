import React, {useState} from 'react';
import styles from "./DetailItem.module.css"


const ImageSlider = ({images}) => {
    const [currentImg, setCurrentImg] = useState(0);
    const maxlength = images.length;

    function getIndex(pos) {
        return (maxlength + pos) % maxlength
    }

    return (
        <div className={styles.ImageSlider__container}>
            <div className={styles.ImageSlider__images_list}>
                <div>+</div>
                <div>
                    <img className={styles.ImageSlider__little_img} src={images[getIndex(1)]}/>
                </div>
                <div>
                    <img className={styles.ImageSlider__little_img} src={images[getIndex(2)]}/>
                </div>
                <div>
                    <img className={styles.ImageSlider__little_img} src={images[getIndex(3)]}/>
                </div>
                <div>
                    <img className={styles.ImageSlider__little_img} src={getIndex(4)}/>
                </div>
                <div>
                    <img className={styles.ImageSlider__little_img} src={getIndex(5)}/>
                </div>
                <div>-</div>
            </div>
            <div className={styles.ImageSlider__main_image}>
                <img className={styles.ImageSlider__big_img} src={images[1]}/>
            </div>
        </div>
    );
};

export default ImageSlider;