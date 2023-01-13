export default function UserUpdate(){
    return (<>
        <h2>회원정보 수정</h2>
            <form action="/send-data-here" method="post">
                <label htmlFor="first">User Email:</label>
                <div id="user_email"></div>
                <label htmlFor="last">Password:</label>
                <input type="text" id="password" name="password" required minLength={4} maxLength={20}/>
                <label htmlFor="first">User Name:</label>           
                <div id="user_name"></div>
                <label htmlFor="last">Phone:</label>
                <input type="text" id="phone" name="phone" minLength={4} maxLength={20}/>
                <label htmlFor="first">Birth:</label>
                <div id="birth"></div>
                <label htmlFor="last">Address:</label>
                <input type="text" id="address" name="address" minLength={4} maxLength={20}/>
                <label htmlFor="first">Job:</label>
                <input type="text" id="job" name="job" minLength={4} maxLength={20}/>
                <label htmlFor="last">User Interests:</label>
                <input type="text" id="user_interests" name="user_interests" minLength={4} maxLength={20}/>
                <button type="submit">Submit</button>
            </form>
    </>)
}