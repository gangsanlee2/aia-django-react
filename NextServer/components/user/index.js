import axios from "axios";
const server = `http://localhost:8000`
export const userLogin = req => axios.post(`${server}/security/users/login`, req)

const uatService = {
    signup
}
function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
    }
async function signup(){
    fetch(`${server}/blog/b_users/signup`)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
} 
export default uatService