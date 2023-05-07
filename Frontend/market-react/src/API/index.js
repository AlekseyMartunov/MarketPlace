import axios from "axios";


export const BASE_URL = 'http://localhost:8000/api/v1/'

const api = axios.create({
    // withCredentials: true,
    baseURL : BASE_URL
})

api.interceptors.request.use((config) => {
    const token= localStorage.getItem('token_access')
    if (token !== null) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

export default api