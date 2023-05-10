import Catalog from "../pages/Catalog/Catalog";
import SelectCategory from "../pages/SelectCategory/SelectCategory";
import DetailItem from "../pages/DetailItem/DetailItem";
import Registration from "../pages/Login/Registration";
import Authorization from "../pages/Login/Authorization";
import Logout from "../pages/Login/Logout";
import Cart from "../pages/Cart/Cart"
import ErrorPage from "../pages/404/ErrorPage"


export const routes = [
    {link: "/*", name: "Ошибка", component: <ErrorPage/>, exact: true},
    {link: "/catalog", name: "Каталог", component: <SelectCategory/>, exact: true},
    {link: "/catalog/:category", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/registration", name: "Регистрация", component: <Registration/>, exact: false},
    {link: "/authorization", name: "Вход", component: <Authorization/>, exact: false},
    {link: "/about-item/:item", name: "О товаре", component: <DetailItem/>, exact: false},
    {link: "/cart", name: "Корзина", component: <Cart/>, exact: false}
]

export const routesAuthorized = [
    {link: "/*", name: "Ошибка", component: <ErrorPage/>, exact: true},
    {link: "/catalog", name: "Каталог", component: <SelectCategory/>, exact: true},
    {link: "/catalog/:category", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/about-item/:item", name: "О товаре", component: <DetailItem/>, exact: false},
    {link: "/logout", name: "Выход", component: <Logout/>, exact: false},
    {link: "/cart", name: "Корзина", component: <Cart/>, exact: false}
]

export const navBarRoutes = [
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/cart", name: "Корзина", component: <Cart/>, exact: false},
    {link: "/registration", name: "Вход/Регистрация", component: <Registration/>, exact: false},
]

export const navBarRoutesAuthorized = [
    {link: "/catalog", name: "Каталог", component: <Catalog/>, exact: true},
    {link: "/cart", name: "Корзина", component: <Cart/>, exact: false},
    {link: "/logout", name: "Выход", component: <Logout/>, exact: false},
]
