import api from "./index";



export default class Server {
    static async getItems(slug_cat, queryParams={}) {
        let url = 'search-items/' + slug_cat

        if (Object.keys(queryParams).length === 0) {
            const response = await api.get(url)
            return response.data
        }

        url += '?'
        for (const [key, value] of Object.entries(queryParams)) {
            const keyValue = `${key}=${value}&`
            url += keyValue
        }
        const response = await api.get(url)
        return response.data
    }

    static async getCats(slug="") {
        let url;
        if (slug !== "") {
            url = 'categories/' + slug
        }
        else {
            url = 'categories'
        }
        const response = await api.get(url)
        return response.data
    }

    static async getShops(category) {
        let url = 'shops/' + category
        const response = await api.get(url)
        return response.data
    }

    static async getDetailItem(slug) {
        const url = 'items/' + slug
        const response = await api.get(url)
        return response.data
    }

    static async authorization(data) {
        const url = 'token/'
        const response = await api.post(url, data)
        return response
    }

    static async logout(token) {
        const url = 'logout/'
        return await api.post(url, token)
    }

    static async cartCacheCreate(data) {
        const url = 'cart/'
        const response = await api.post(url, data)
        return response
    }

    static async getCartItems() {
        const url = 'cart/'
        const response = await api.get(url)
        return response.data
    }

    static async updateCache(data){
        const url = 'cart/'
        const response = await api.put(url, data)
        return response.data
    }

    static async deleteCAche(){
        const url = 'cart/'
        const response = await api.delete(url)
        return response
    }

    static async createOrder(data){
        const url = 'create-order/'
        const response = await api.post(url)
        return response
    }


}