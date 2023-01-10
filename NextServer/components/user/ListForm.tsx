import 'uat/styles/UserList.css'
export default function ListForm({list:[]}){
    return(<>
    <br/><br/>검색: <input type="text"/><button>입력</button><br/><br/><br/>
    <table className='user-list'>
        <thead>
            <tr>
                <th>ID</th><th>이메일</th><th>비밀번호</th><th>이름</th><th>전화번호</th><th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    </>)
}
