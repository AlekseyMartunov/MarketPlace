import Catalog from "../pages/Catalog/Catalog";
import Login from "../pages/Login/Login";

export const routes = [
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/login", name: "Вход", component: <Login/>, exact: true},
]