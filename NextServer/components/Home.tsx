import Navigation from './admin/Navigation'
import Footer from './admin/Footer'
export default function Home(){
    return (<>
    <table style={{ width: "1200px", height: "550px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr>
                <td style={{ width: "100%", border: "1px solid black"}}><Navigation/></td>
            </tr>
        </thead>
        <tbody>
            <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
                <td style={{ width: "100%", border: "1px solid black"}}>
                {/* <Routes>
                    <Route path="/counter" element={<Counter/>}></Route>
                    <Route path="/todos/" element={<Schedule/>}></Route>
                    <Route path="/signup" element={<SignUp/>}></Route>
                    <Route path="/login" element={<Login/>}></Route>
                    <Route path="/stroke" element={<Stroke/>}></Route>
                    <Route path="/iris" element={<IrisForm/>}></Route>
                    <Route path="/fashion" element={<FashionForm/>}></Route>
                    <Route path="/number" element={<Number/>}></Route>
                    <Route path="/naver-movie" element={<NaverMovie/>}></Route>
                    <Route path="/samsung-report" element={<SamsungReport/>}></Route>
                    <Route path="/naver-movie-review" element={<NaverMovieReview/>}></Route>
                    <Route path="/user-list" element={<UserList/>}></Route>
                    <Route path="/korean-classify" element={<KoreanClassify/>}></Route>
                    <Route path="/aitrader" element={<AiTrader/>}></Route>
                </Routes> */}
                </td>
            </tr>
            <tr>
                <td>
                </td>
            </tr>
            <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
                <td style={{ width: "100%", border: "1px solid black"}}><Footer/></td>
            </tr>
        </tbody>
    </table>
  </>)
}
