import Catalog from "../pages/Catalog/Catalog";
import SelectCategory from "../pages/SelectCategory/SelectCategory";
import DetailItem from "../pages/DetailItem/DetailItem";
import Registration from "../pages/Login/Registration";
import Authorization from "../pages/Login/Authorization";


export const routes = [
    {link: "/catalog", name: "Каталог", component: <SelectCategory/>, exact: true},
    {link: "/catalog/:category", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/registration", name: "Регистрация", component: <Registration/>, exact: false},
    {link: "/authorization", name: "Вход", component: <Authorization/>, exact: false},
    {link: "/about-item/:item", name: "О товаре", component: <DetailItem/>, exact: false}
]

export const navBarRoutes = [
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/registration", name: "Вход/Регистрация", component: <Registration/>, exact: false},
]

export const navBarRoutesAuthorized = [
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/registration", name: "Вход/Регистрация", component: <Registration/>, exact: false},
]
