import { useState } from "react"

const Counter = () => {
  const [count, setCount] = useState(0)
  return (<>
    <h3>카운터</h3>
    <div>클릭한 횟수 : {count}</div><br></br>
    <button onClick={() => {setCount(count + 1)}}>
      더하기
    </button><br></br><br></br>
    <button onClick={() => {setCount(count - 1)}}>
      빼기
    </button>
  </>)
}

export default Counter