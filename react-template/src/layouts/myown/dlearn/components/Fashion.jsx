import { useState } from "react";
import dlearnService from "../api"

const Fashion = () => {
    const [inputs, setInputs] = useState({})
    const {id} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})   //리스트로 감쌌다는 것은 변수라는 의미이다. ex) a = {'b':5,'c':10}   =>  a[b] = 5
    }
    const onGetClick = e => {
        e.preventDefault()
        /*        
        alert(`선택한 번호 : ${JSON.stringify(id)}`)
        getFashion(id)
        .then((res)=>{
            alert(`찾는 옷의 종류 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('번호를 다시 입력해주세요')
        })
        */
        dlearnService.getFashion(id)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    const onPostClick = e => {
        e.preventDefault()
        /*
        const request = {id}
        alert(`선택한 번호 : ${JSON.stringify(request)}`)
        postFashion(request)
        .then((res)=>{
            console.log(`Response is ${res.data.result}`)
            localStorage.setItem('token', JSON.stringify(res.data.result))
            alert(`찾는 옷의 종류 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('번호를 다시 입력해주세요')
        })
        */
       dlearnService.postFashion(id)
       let arr = document.getElementsByClassName('box')
       for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    
    return(<>
    <form method="get">
        <h1>FASHION GET방식</h1>
        <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
        <input type="text" className="box" placeholder="테스트할 옷 번호" name="id" onChange={onChange}/>
        <button onClick={onGetClick}>옷의 카테고리 찾기</button>
    </form>
    <form method="post">
        <h1>FASHION POST방식</h1>
        <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
        <input type="text" className="box" placeholder="테스트할 옷 번호" name="id" onChange={onChange}/>
        <button onClick={onPostClick}>옷의 카테고리 찾기</button>
    </form>
    </>)
}
export default Fashion