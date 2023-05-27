import axios from "axios";


export const BASE_URL = 'http://localhost:8000/api/v1/'

const api = axios.create({
    withCredentials: true,
    baseURL : BASE_URL
})

api.interceptors.request.use((config) => {
    const token= localStorage.getItem('token_access')
    if (token !== null) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

api.interceptors.response.use((config) => {
    return config
}, async (error) => {
    const originalRequest = error.config;
     if (error.response.status === 401) {
         try {
             const token_refresh = localStorage.getItem("token_refresh")
             const response = await axios.post(BASE_URL + 'token/refresh/',
                 {'refresh': token_refresh})
             localStorage.setItem('token_access', response.data['access'])
             return  api.request(originalRequest)
         } catch (e) {
             console.log("Не авторизован")
         }

     }
})

export default api