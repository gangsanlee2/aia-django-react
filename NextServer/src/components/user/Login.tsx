export default function Login(){    
    return(
    <>
        <h1>로그인</h1>
        <form action="/send-data-here" method="post">

            <label htmlFor="user_email">User Email:</label>
            <input type="text" id="user_email" name="user_email" required minLength={4} maxLength={20} />

            <label htmlFor="password">Password:</label>
            <input type="text" id="password" name="password" required minLength={4} maxLength={20}/>
            
            <button type="submit">Submit</button>
        </form>
    </>
)}