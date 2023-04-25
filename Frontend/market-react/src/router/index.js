import Login from "../pages/Login/Login";
import Catalog from "../pages/Catalog/Catalog";
import SelectCategory from "../pages/SelectCategory/SelectCategory";
import DetailItem from "../pages/DetailItem/DetailItem";


export const routes = [
    {link: "/catalog", name: "Каталог", component: <SelectCategory/>, exact: true},
    {link: "/catalog/:category", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/login", name: "Вход", component: <Login/>, exact: false},
    {link: "/about-item/:item", name: "О товаре", component: <DetailItem/>, exact: false}
]

export const navBarRoutes = [
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/login", name: "Вход", component: <Login/>, exact: false},
]
