import axios from "axios";


export default class Server {
    static async getItems(url="") {
        if (url === "") {
            let url = 'http://127.0.0.1:8000/api/v1/search-items'
            const response = await axios.get(url)
            return response.data
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
}