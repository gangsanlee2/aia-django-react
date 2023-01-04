import dlearnService from "../api"
import { useState } from "react"

const AiTrader = () => {
    const [inputs, setInputs] = useState({})
    const [label, setLabel] = useState('')
    const [predict_dnn, setPredict_dnn] = useState('')
    const [predict_lstm, setPredict_lstm] = useState('')
    const [predict_dnn_ensemble, setPredict_dnn_ensemble] = useState('')
    const [predict_lstm_ensemble, setPredict_lstm_ensemble] = useState('')
    const {index} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        dlearnService.aitrader(index).then(res => {
            const json = JSON.parse(res)
            setLabel(json["label"])
            setPredict_dnn(json["result_dnn"])
            setPredict_lstm(json["result_lstm"])
            setPredict_dnn_ensemble(json["result_dnn_ensemble"])
            setPredict_lstm_ensemble(json["result_lstm_ensemble"])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(
    <>
    <form method="post">
        인덱스 입력: <input type="text" className="box" name="index" onChange={onChange} /><br/>
        <button type="submit" onClick={onClick}>입력</button>
    </form>
    <table>
        <thead>
            <tr>
            <th>인덱스 번호</th><th>실제 종가</th><th>예측 종가 DNN</th><th>예측 종가 LSTM</th><th>예측 종가 DNN Ensemble</th><th>예측 종가 LSTM Ensemble</th>
            </tr>
        </thead>
        <tbody>
        {label && 
            <tr ><td>{index}</td><td>{label}</td><td>{predict_dnn}</td><td>{predict_lstm}</td><td>{predict_dnn_ensemble}</td><td>{predict_lstm_ensemble}</td></tr>
        }  
        </tbody>
    </table>     
    </>
)
}
export default AiTrader