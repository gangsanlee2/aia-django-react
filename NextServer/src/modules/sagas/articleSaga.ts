import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { writeRequest, writeSuccess, articleAction } from "../slices/articleSlice";
import { Article } from '@/modules/types';
import { article } from "../apis/articleAPI";

export function* watchWrite(){
    yield takeLatest(writeRequest, (action: {payload: Article}) => {
        
        try{
            const response: any = article.write(action.payload)
            put(writeSuccess(response.payload))
            window.location.href = '/article/write'
        }catch(error){
            put(articleAction.writeFailure(error))
        }
    })
}