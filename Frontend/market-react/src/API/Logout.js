import Server from "./Server";


async function logout() {
    try {
        const token_refresh = localStorage.getItem('token_refresh')
        let token = {}
        token['refresh'] = token_refresh
        const responce = await Server.logout(token)
        console.log(responce)

        localStorage.removeItem('token_refresh')
        localStorage.removeItem('token_access')
        localStorage.removeItem('userName')

        setUserName("")
    } catch (e) {
            console.log(e.response)
        }

}

export default logout;