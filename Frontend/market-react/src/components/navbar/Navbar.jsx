import React from 'react';
import classes from './Navbar.module.css'
import {Link} from "react-router-dom";
import {routes} from "../../router";

const Navbar = () => {

    return (
        <div className={classes.navbar}>
            {routes.map((router) =>
                <div className={classes.element}>
                    <Link to={router.link} className={classes.link}>{router.name}</Link>
                </div>
            )}
        </div>
    );
};

export default Navbar;