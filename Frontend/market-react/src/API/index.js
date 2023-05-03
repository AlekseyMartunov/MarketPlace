import axios from "axios";


export const BASE_URL = 'http://localhost:8000/api/v1/'

const api = axios.create({
    // withCredentials: true,
    baseURL : BASE_URL
})

api.interceptors.request.use((config) => {
    // config.headers.Authorization = ""
    return config
})

export default api