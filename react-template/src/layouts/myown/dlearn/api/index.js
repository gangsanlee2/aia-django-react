/*
import axios from "axios";
const server = `http://localhost:8000`
export const getFashion = id => axios.get(`${server}/dlearn/fashion?id=${id}`)
export const postFashion = req => axios.post(`${server}/dlearn/fashion`, req)
*/

const server = `http://localhost:8000`
const dlearnService = {
    getFashion, postFashion, getNumber, postNumber, aitrader
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
async function postFashion(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}/basic/dlearn/fashion`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}
async function getFashion(id){
    fetch(`${server}/basic/dlearn/fashion?id=${id}`)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
} 

async function postNumber(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}/basic/mnist-number/number`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}
async function getNumber(id){
    fetch(`${server}/basic/mnist-number/number?id=${id}`)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
} 

async function aitrader(index){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(index)
    }
    const res = await fetch(`${server}/basic/dlearn/aitrader`, requestOption)
    .then(handleResponse)
    .then(data => (JSON.stringify(data)))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}

export default dlearnService