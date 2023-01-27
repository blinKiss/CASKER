
import json
import requests
import save_token

# 저장된 토큰 정보를 읽어옴
tokens = save_token.load_tokens(save_token.KAKAO_TOKEN_FILE)

# json 문자열의 '(작은따옴표)를 "(큰따옴표)로 변환
json_str = tokens.replace("'", "\"")

# json 문자열을 딕셔너리로 변환
tokens = json.loads(json_str) 

# print(tokens)
print(tokens['access_token'])


# 텍스트 메시지 url
# 카카오톡 나에게 보내기 URL
url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

# header 정보
# Authorization : 인증정보를 담는 헤더
headers = {
    'Authorization' : 'Bearer ' + tokens['access_token']
}

temp = {
    'object_type' : 'feed',     # text, feed
    # 'text' : '안녕 동찬?',
    # URL은 Kakao Developer > 내 애플리케이션 > 앱 설정 > 플랫폼 > Web에 등록된 도메인만 사용가능
    "content" : {
        "title" : "송태섭",
        "description" : "가드",
        "image_url" : "https://w.namu.la/s/9ee1c8737f565c9612a1007d10322704abd329c34061eb55a048e99c49fdcabf34821d8ed0a317da09c02fc8170fa53d0dda8ef16d81ee8e1160f314d4a60505d2c3d828122119b4259f2e174bd072baeaa60061a2a8ae3b855b5586edd7ccd9",
        "image_width" : 640,
        "image_height" : 640,
        'link' : { 
            "web_url" : 'https://www.naver.com',         # PC 카톡의 url
            "mobile_web_url" : 'https://m.youtube.com'  # 모바일 url
            }
    }
}

data = {
    'template_object' : json.dumps( temp )
}


# 나에게 카카오 메시지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)