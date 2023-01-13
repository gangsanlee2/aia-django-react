export default function UserDetail(){
    return (<>
        <h2>회원정보</h2>
        <div>
            <label htmlFor="first">User Email:</label>
            <div id="user_email"></div>
            <label htmlFor="last">Password:</label>
            <div id="password"></div>
            <label htmlFor="first">User Name:</label>    
            <div id="user_name"></div>
            <label htmlFor="last">Phone:</label>
            <div id="phone"></div>
            <label htmlFor="first">Birth:</label>
            <div id="birth"></div>
            <label htmlFor="last">Address:</label>
            <div id="address"></div>
            <label htmlFor="first">Job:</label>
            <div id="job"></div>
            <label htmlFor="last">User Interests:</label>
            <div id="user_interests"></div>

            <button type="submit">회원정보 수정</button>
        </div>
    </>)
}