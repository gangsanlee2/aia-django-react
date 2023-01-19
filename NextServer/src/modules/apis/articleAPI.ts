import axios, { AxiosResponse } from 'axios'
import {context} from '@/components/admin/enums'
import { currentTime } from '@/components/admin/utils'
import { Article, User } from '@/modules/types'
import { author, client } from "@/modules/controllers"

export const article = {
    async write(payload: Article){
            try{
                const response : AxiosResponse<any, Article[]> =
                await axios.post(`http://localhost:8000/articles/write`, payload, {headers: {
                    "Content-Type" : "application/json",
                    Authorization: "JWT fefege...",
                }})
                if(response.data === "success"){
                    alert(' 결과: API 내부 write 성공  '+ JSON.stringify(response.data))
                }else{
                    alert(` 결과: ${response.data.msg}  `)
                }
                
                return response
            }catch(err){
                console.log(` ${currentTime} : userSaga 내부에서 write 실패 `)
            }
        }    
}