import { stroke } from "../api"

const Stroke = () => {
    const onClick = e => {
        e.preventDefault()
        stroke()
    }
    return(<>
    <button onClick={onClick}>stroke</button>
    </>)
}
export default Stroke