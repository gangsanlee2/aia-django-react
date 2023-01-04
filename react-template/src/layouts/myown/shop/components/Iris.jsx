import { iris } from "../api";
import { useState } from "react";

const Iris = () => {
    const [inputs, setInputs] = useState({})
    const {SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const request = {SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm}
        alert(`꽃잎,받침 길이/너비 : ${JSON.stringify(request)}`)
        iris(request)
        .then((res)=>{
            console.log(`Response is ${res.data.result}`)
            localStorage.setItem('token', JSON.stringify(res.data.result))
            alert(`찾는 품종 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('꽃잎,받침 길이/너비를 다시 입력해주세요')
        })
    }
    
    return(
    <>
        꽃받침 길이: <input type="number" step="0.1" name="SepalLengthCm" placeholder='~.~소수점첫째자리(cm)' onChange={onChange} /><br/>
        꽃받침 너비: <input type="number" step="0.1" name="SepalWidthCm" placeholder='~.~소수점첫째자리(cm)' onChange={onChange} /><br/>
        꽃잎 길이: <input type="number" step="0.1" name="PetalLengthCm" placeholder='~.~소수점첫째자리(cm)' onChange={onChange} /><br/>
        꽃잎 너비: <input type="number" step="0.1" name="PetalWidthCm" placeholder='~.~소수점첫째자리(cm)' onChange={onChange} /><br/>
        <button onClick={onClick}> 입력 </button>
    </>)
}
export default Iris