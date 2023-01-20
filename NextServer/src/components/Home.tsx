import { useState, useEffect } from "react"
import Pagination from "./admin/Pagination"
import axios from "axios";


export default function Home(){
    const [currentPage, setCurrentPage] = useState(1);
    const lastPage = 3;
    
    const [list, setList] = useState([])
    const [rowCount, setRowCount] = useState(0)
    const [rowStart, setRowStrart] = useState(0)
    const [rowEnd, setRowEnd] = useState(0)
    const [pageStart, setPageStrat] = useState(0)
    const [pageEnd, setPageEnd] = useState(0)
    const [requestPage, setRequestPage] = useState(0)
    const [rows, setRows] = useState<number[]>([])
    const [pages, setPages] = useState<number[]>([])
    const [prevArrow, setPrevArrow] = useState(false)
    const [nextArrow, setNextArrow] = useState(false)

    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/5')
        .then(res => {
            setList(res.data.user_info.items)
            setRowCount(res.data.page_info.row_cnt)
            setRowStrart(Number(res.data.page_info.row_start))
            setRowEnd(Number(res.data.page_info.row_end))
            setPageStrat(Number(res.data.page_info.page_start))
            setPageEnd(Number(res.data.page_info.page_end))
            setRequestPage(Number(res.data.page_info.request_page))
            
            console.log(` ### 페이지 내용 표시 ### `)
            let rows: number[] = []
            let pages: number[] = []
            for (let i = rowStart; i <= rowEnd; i++){
                rows.push(i)
            }
            setRows(rows)

            console.log(` ### 블록 내용 표시 ### `)
            for (let i = pageStart; i <= pageEnd; i++){
                pages.push(i)
            }
            setPages(pages)
            
            setPrevArrow(res.data.page_info.prev_arrow)
            setPrevArrow(res.data.page_info.next_arrow)

            console.log(` 사용자가 요청한 페이지 번호 : ${requestPage}`)

        })
        .catch(err => {console.log(err)})
    }, [])

    return (<>
        <h2>User List</h2>
        <h6>total {rowCount}</h6>
        <h6></h6>
        <h6></h6>
        <h6></h6>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비번</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>
            {list && list.map(({user_id, user_email, password, user_name, phone, birth, address, job, user_interests})=>(
                <tr key={user_id}>
                    <td>{user_id}</td><td>{user_email}</td><td>{user_name}</td>
                    <td>{phone}</td><td>{birth}</td><td>{address}</td>
                    <td>{job}</td><td>{user_interests}</td>
                </tr>
            ))}
            </tbody>
        </table>
        <div>
            {prevArrow && <span>이전</span>}
            {pages && pages.map((value, index) => (<span style={{"border": "1px solid black"}}>{value+1}</span>))}
            {nextArrow && <span>이후</span>}
        </div>
        <div className="page-container">
        </div>
    </>)
}