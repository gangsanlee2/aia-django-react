export default function UserRemove(){
    return (<>
        <h1>회원 탈퇴</h1>
        <form action="/send-data-here">
        <label htmlFor="first">비밀번호 확인:</label>
        <input type="text" id="password" name="password" required minLength={4} maxLength={20}/>
        <button type="submit">Submit</button>
        </form>
    </>)
}