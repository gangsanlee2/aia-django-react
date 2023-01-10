import { useEffect, useState } from "react"
import axios from "axios"
import ListForm from './ListForm'
export default function UserList(){
    const [list, setList] = useState([])
    useEffect(()=>{
        fetchList()
    }, [])
    const fetchList = () => {
        axios
        .get('http://127.0.0.1:8000/security/users/user-list')
        .then(res => {setList(res.data)})
        .catch(err => {console.log(err)})
    }
    return<>
        <ListForm list={list}/>
    </>
}
