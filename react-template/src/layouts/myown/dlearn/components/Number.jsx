import { useState } from "react";
import dlearnService from "../api"

const Number = () => {
    const [inputs, setInputs] = useState({})
    const {id} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})   //리스트로 감쌌다는 것은 변수라는 의미이다. ex) a = {'b':5,'c':10}   =>  a[b] = 5
    }
    const onGetClick = e => {
        e.preventDefault()
        dlearnService.getNumber(id)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    const onPostClick = e => {
        e.preventDefault()
       dlearnService.postNumber(id)
       let arr = document.getElementsByClassName('box')
       for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    
    return(<>
    <form method="get">
        <h1>손글씨 GET방식</h1>
        <p>알고 싶은 손글씨의 번호를 입력해주세요.</p>
        <input type="text" className="box" placeholder="테스트할 손글씨 번호" name="id" onChange={onChange}/>
        <button onClick={onGetClick}>손글씨의 카테고리 찾기</button>
    </form>
    <form method="post">
        <h1>손글씨 POST방식</h1>
        <p>알고 싶은 손글씨의 번호를 입력해주세요.</p>
        <input type="text" className="box" placeholder="테스트할 손글씨 번호" name="id" onChange={onChange}/>
        <button onClick={onPostClick}>손글씨의 카테고리 찾기</button>
    </form>
    </>)
}
export default Number