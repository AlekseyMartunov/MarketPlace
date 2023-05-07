import classes from './Navbar.module.css'
import {AuthContext} from "../../context";
import {Link} from "react-router-dom";
import {navBarRoutesAuthorized, navBarRoutes} from "../../router";
import {useContext} from "react";
import UserName from "./UserName";


const Navbar = () => {
    const {isAuth, setIsAuth} = useContext(AuthContext)

    return (
        <div className={classes.navbar}>
            {
                isAuth ? (
                    navBarRoutesAuthorized.map((router, indx) =>
                            <div className={classes.element} key={indx}>
                                <Link className={classes.link} to={router.link}>
                                    {router.name}
                                </Link>
                            </div>
                        )
                ) : (
                    navBarRoutes.map((router, indx) =>
                        <div className={classes.element} key={indx}>
                            <Link className={classes.link} to={router.link}>
                                {router.name}
                            </Link>
                        </div>
                    )
                )
            }
            <UserName/>
        </div>
    );
};

export default Navbar;

