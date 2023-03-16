import Login from "../pages/Login/Login";
import CategoryMenu from "../pages/Catalog/CategoryMenu/CategoryMenu";
import Catalog from "../pages/Catalog/Catalog/Catalog";

export const routes = [
    {link: "/catalog", name: "Каталог", component: <CategoryMenu/>, exact: true},
    {link: "/catalog/:slug", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/login", name: "Вход", component: <Login/>, exact: true},

]

export const NavbarRoutes = [
    {link: "/catalog", name: "Каталог", component: <CategoryMenu/>, exact: true},
    {link: "/login", name: "Вход", component: <Login/>, exact: true},

]