import axios from "axios";



export default class Server {
    static async getItems() {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/items')
        return response.data
    }
}