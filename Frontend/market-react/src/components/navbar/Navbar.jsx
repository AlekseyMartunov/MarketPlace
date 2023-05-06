import React, {useContext} from 'react';
import classes from './Navbar.module.css'
import {Link} from "react-router-dom";
import {AuthContext} from "../../context";
import logout from "../../API/Logout";


const Navbar = () => {
    const {name, shop} = useContext(AuthContext);
    const [username, setUserName] = name;
    const [isShopOwner, setIhopOwner] = shop;

    return (
        <div className={classes.navbar}>
            <div className={classes.element}>
                <Link className={classes.link} to={'/catalog'}>
                    Каталог
                </Link>
            </div>
            {
                username ? (
                    <div
                        onClick={logout}
                    >Logout</div>
                ) : (
                    <div className={classes.element}>
                        <Link className={classes.link} to={'/registration'}>
                            Вход/Регистрация
                        </Link>
                    </div>
                )
            }

        </div>
    );
};

export default Navbar;

