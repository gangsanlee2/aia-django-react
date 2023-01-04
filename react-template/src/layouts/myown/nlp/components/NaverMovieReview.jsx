import nlpService from "../api"
import { useState } from "react"

const NaverMovieReview = () => {
    const [inputs, setInputs] = useState({})
    const [positive, setPositive] = useState('')
    const {inhalt} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        nlpService.review(inhalt).then(res => {
            const json = JSON.parse(res)
            setPositive(json["result"])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(
    <>
    <form method="post">
        REVIEW: <input type="text" className="box" name="inhalt" onChange={onChange} /><br/>
        <button type="submit" onClick={onClick}>리뷰 긍정도 확인</button>
    </form>
    <table>
        <thead>
            <tr>
            <th>리뷰</th><th>긍정도</th>
            </tr>
        </thead>
        <tbody>
        {positive && 
            <tr ><td>{inhalt}</td><td>{positive}</td></tr>
        }    
        </tbody>
    </table>     
    </>
)
}
export default NaverMovieReview