import axios from "axios";
const server = `http://localhost:8000`
export const fakeFaces = req => axios.get(`${server}/movie/movies/fake-faces`, req)
