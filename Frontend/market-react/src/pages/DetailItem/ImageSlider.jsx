import React, {useState} from 'react';
import styles from "./DetailItem.module.css"


const ImageSlider = ({images}) => {
    const [selected, setSelected] = useState(0);
    const [bigImg, setBigImg] = useState("")

    function updateImages(img, id){
        setBigImg(img)
        setSelected(id)
    }

    return (
        <div className={styles.ImageSlider_container}>
            <div className={styles.ImageSlider_images_list}>
                {images.map((img, id)=>
                    <div>
                        <img
                            key={id}
                            onClick={() => updateImages(img, id)}
                            src={img}
                            className={id === selected ? (
                                styles.ImageSlider_little_img_selected + " " + styles.ImageSlider_little_img
                            ): (
                                styles.ImageSlider_little_img
                            )}
                        />
                    </div>
                )}
            </div>
            <div className={styles.ImageSlider_main_image}>
                <img className={styles.ImageSlider_big_img} src={bigImg ? (bigImg) : (images[0])}/>
            </div>
        </div>
    );
};

export default ImageSlider;