export default function GoogleLogin(){
    return (<>
        <h1>구글 로그인</h1>
        <form action="/send-data-here" method="post">
            <label htmlFor="first">User Email:</label>
            <input type="text" id="user_email" name="user_email" required minLength={4} maxLength={20} />
            <label htmlFor="last">Password:</label>
            <input type="text" id="password" name="password" required minLength={4} maxLength={20} />

            <button type="submit">Submit</button>
        </form>
    </>)
}