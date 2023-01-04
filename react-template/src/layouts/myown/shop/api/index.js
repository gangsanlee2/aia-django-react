import axios from "axios";
const server = `http://localhost:8000`
export const iris = req => axios.post(`${server}/basic/dlearn/iris`, req)
