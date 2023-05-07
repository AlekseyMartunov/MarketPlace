import React from 'react';
import classes from './Navbar.module.css'
const UserName = () => {
    const name = localStorage.getItem("userName")
    return (
        <div className={classes.username_context}>
            {name ? (
                <div className={classes.username}>
                    {name}
                </div>
            ) : (
                null
            )}
        </div>
    );
};

export default UserName;