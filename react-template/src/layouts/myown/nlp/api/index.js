const server = `http://localhost:8000`
const nlpService = {
    report, review, handleResponse, korean_classify
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
async function report(){
    const res = await fetch(`${server}/basic/nlp/samsung-report`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    
    return Promise.resolve(res);
} 
async function review(inhalt){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(inhalt)
    }
    const res = await fetch(`${server}/basic/nlp/naver-movie-review`, requestOption)
    .then(handleResponse)
    .then(data => (JSON.stringify(data)))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}

async function korean_classify(text){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(text)
    }
    const res = await fetch(`${server}/basic/nlp/korean-classify`, requestOption)
    .then(handleResponse)
    .then(data => (JSON.stringify(data)))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}
export default nlpService
