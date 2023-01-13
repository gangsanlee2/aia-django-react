import { NextPage } from "next"
import Login from "@/components/user/Login";
import GoogleLogin from "@/components/user/GoogleLogin";


const LoginPage: NextPage = function(){

    return (
        <>
           <Login/>
           <GoogleLogin/>
        </>
            
        
 );
}
export default LoginPage