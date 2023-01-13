export default function FindPassword(){
    return (<>
    <h1>비밀번호 찾기</h1>
        <form action="/send-data-here">
        <label htmlFor="first">User Email:</label>
            <input type="text" id="user_email" name="user_email" required minLength={4} maxLength={20}/>
        <label htmlFor="first">User Name:</label>           
            <input type="text" id="user_name" name="user_name" required minLength={4} maxLength={20}/>
        <label htmlFor="last">Phone:</label>
            <input type="text" id="phone" name="phone" required minLength={4} maxLength={20}/>
        </form>
    </>)
}