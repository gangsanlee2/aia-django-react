import nlpService from "../api"
import { useState } from "react"

const SamsungReport = () => {
    
    const [input, setInput] = useState()

    const onClick = e => {
        e.preventDefault()
        nlpService.report().then(res => {
            const json = JSON.parse(res)
            setInput(json['result'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h2>삼성 보고서 분석</h2>
    <button onClick={onClick}>삼성 보고서 분석</button>
    <p>버튼을 클릭하시면, 삼성 보고서 단어 빈도 분석이 출력됩니다.</p>
    <table>
        <thead>
            <tr>
                <th>단어</th><th>빈도수</th>
            </tr>
        </thead>
        <tbody>
        {input && input.map(({word, freq})=>(
            <tr key={word}><td>{word}</td><td>{freq}</td></tr>
        ))}
        </tbody>
    </table>
    </>)
}
export default SamsungReport