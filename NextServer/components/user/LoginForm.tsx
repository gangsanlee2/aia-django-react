import 'uat/styles/Login.css'
import { useState } from 'react'
import { userLogin } from './index'

export default function LoginForm(){
    const [inputs, setInputs] = useState({})
  
    return(
    <>
        EMAIL: <br/>
        PASSWORD: <br/>
        <button> 로그인 </button>
    </>
)}