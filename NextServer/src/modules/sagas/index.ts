import { all, fork } from "redux-saga/effects"
import { watchWrite } from "./articleSaga"
import{ watchJoin, watchLogin, watchLogout } from "./userSaga"

export default function* rootSaga(){
    yield all([ fork(watchJoin), fork(watchLogin), fork(watchLogout), fork(watchWrite) ])
}