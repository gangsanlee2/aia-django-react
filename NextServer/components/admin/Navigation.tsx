import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';


const Navigation = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 500 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        {/* <Link to="/home" style={{width:70, margin:10}}>홈</Link>
        <Link to="/counter" style={{width:70, margin:10}}>카운터</Link>
        <Link to="/todos" style={{width:70, margin:10}}>할일</Link>
        <Link to="/signup" style={{width:70, margin:10}}>회원가입</Link>
        <Link to="/login" style={{width:70, margin:10}}>로그인</Link>
        <Link to="/stroke" style={{width:70, margin:10}}>뇌졸중</Link>
        <Link to="/iris" style={{width:70, margin:10}}>아이리스</Link>
        <Link to="/fashion" style={{width:70, margin:10}}>패션</Link>
        <Link to="/number" style={{width:70, margin:10}}>손글씨</Link>
        <Link to="/naver-movie" style={{width:70, margin:10}}>네이버 영화</Link>
        <Link to="/samsung-report" style={{width:70, margin:10}}>삼성 보고서</Link>
        <Link to="/naver-movie-review" style={{width:70, margin:10}}>네이버 영화 리뷰</Link>
        <Link to="/user-list" style={{width:70, margin:10}}>사용자목록</Link>
        <Link to="/korean-classify" style={{width:70, margin:10}}>언어분류기</Link>
        <Link to="/aitrader" style={{width:70, margin:10}}>주가예측</Link> */}
      </BottomNavigation>
    </Box>
  );
}

export default Navigation