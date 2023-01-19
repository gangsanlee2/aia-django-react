
export interface User{
    user_id? : string,
    user_email? : string,
    password? : string,
    cpassword?: string, 
    user_name? : string,
    phone? : string,
    birth? : string,
    address? : string,
    job? : string,
    user_interests? : string,
    token? : string,
    created_at? : string,
    updated_at? : string
}

export interface UserLoginInput{
    user_email: string,
    password: string
}

export interface UserUpdate{
    user_id?: string,
    phone?: string,
    job?: string,
    user_interests?: string,
    updated_at?: string
}
export interface LoginUser{ 
    user_name?:string, password:string, email:string, userid?:string,
    phone?:string, birth?:string, 
    token?: any
}

export interface UserInfo{
    user_name:string, password:string, email:string,
    phone:string, birth:string,
    token: any
}

export interface UserInfoState{
    data: UserInfo[],
    isloggined: boolean
}

export interface UserState{
    data: User[],
    status: 'idle' | 'loading' | 'failed',
    token?: null,
    isLoggined: boolean,
    error : null,
    loginedUser: null,
    check: boolean
}