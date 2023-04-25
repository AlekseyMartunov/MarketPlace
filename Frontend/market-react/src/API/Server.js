import axios from "axios";


export default class Server {
    static async getItems(slug_cat, queryParams={}) {
        let url = 'http://localhost:8000/api/v1/search-items/' + slug_cat

        if (Object.keys(queryParams).length === 0) {
            const response = await axios.get(url)
            return response.data
        }

        url += '?'
        for (const [key, value] of Object.entries(queryParams)) {
            const keyValue = `${key}=${value}&`
            url += keyValue
        }
        const response = await axios.get(url)
        return response.data
    }

    static async getCats(slug="") {
        let url;
        if (slug !== "") {
            url = 'http://localhost:8000/api/v1/categories' + '/' + slug
        }
        else {
            url = 'http://localhost:8000/api/v1/categories'
        }
        const response = await axios.get(url)
        return response.data
    }

    static async getShops(category) {
        let url = 'http://localhost:8000/api/v1/shops/' + category
        const response = await axios.get(url)
        return response.data
    }
}