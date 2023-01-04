import nlpService from "../api"
import { useState } from "react"

const KoreanClassify = () => {
    const [inputs, setInputs] = useState({})
    const [language, setLanguage] = useState('')
    const {text} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        nlpService.korean_classify(text).then(res => {
            const json = JSON.parse(res)
            setLanguage(json["result"])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(
    <>
    <form method="post">
        TEXT: <input type="text" className="box" name="text" onChange={onChange} /><br/>
        <button type="submit" onClick={onClick}>enter</button>
    </form>
    <table>
        <thead>
            <tr>
            <th>입력</th><th>언어</th>
            </tr>
        </thead>
        <tbody>
        {language && 
            <tr ><td>{text}</td><td>{language}</td></tr>
        }    
        </tbody>
    </table>     
    </>
)
}
export default KoreanClassify