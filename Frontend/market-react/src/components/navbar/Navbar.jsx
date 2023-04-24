import React from 'react';
import classes from './Navbar.module.css'
import {Link} from "react-router-dom";
import {navBarRoutes} from "../../router";

const Navbar = () => {

    return (
        <div className={classes.navbar}>
            {navBarRoutes.map((router, indx) =>
                <div className={classes.element} key={indx}>
                    <Link className={classes.link} to={router.link}>
                        {router.name}
                    </Link>
                </div>
            )}
        </div>
    );
};

export default Navbar;