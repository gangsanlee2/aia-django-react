#-*- encoding: utf-8 -*-

from PyKakao import KoGPT

from app.services.chatbot.secrets import KAKAO_KOGPT_API

api = KoGPT(service_key = KAKAO_KOGPT_API)

class KakaoKoGpt3:
    def __init__(self):
        pass

    def exec(self, request):
        # 필수 파라미터
        prompt = f"""정보:거주지 서울, 나이 30대, 성별 남자, 자녀 두 명, 전공 인공지능, 말투 친절함
        정보를 바탕으로 질문에 답하세요.
        Q:{request}
        A:"""
        max_tokens = 32

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.3, top_p=0.85)['generations'][0]['text'].split('Q')[0]
        return result

if __name__ == '__main__':
    KakaoKoGpt3().exec('안녕 반가워 너는 어디 사니?')