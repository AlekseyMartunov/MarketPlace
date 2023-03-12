import axios from "axios";


export default class Server {
    s
    static async getItems() {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/items')
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
        console.log(url)
        return response.data
    }
}