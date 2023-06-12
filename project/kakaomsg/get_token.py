
'''
1 인가코드 받기
kauth.kakao.com/oauth/authorize?client_id=${REST_API_KEY}&redirect_uri=${REDIRECT_URI}&response_type=code

- ${REST_API_KEY} : 내 어플리케이션 > REST API 키
- ${REDIRECT_URI} : https://localhost.com

# 인가코드 요청 경로
https://kauth.kakao.com/oauth/authorize?client_id=e5416bc8599f67b31d6efc5d23bf72a4&redirect_uri=https://localhost.com&response_type=code
'''


'''
2. 인증토큰 받기
'''
import requests

url = 'https://kauth.kakao.com/oauth/token'

data = {
    'grant_type'    : 'authorization_code',
    'client_id'     : 'd',    # REST API 키
    'redirect_uri'  : 'https://localhost.com',               #
    'code'          : 'q'      # 인가코드
}

response = requests.post(url, data=data)


# 요청 실패 시,
if response.status_code != 200:
    print('오류가 발생하였습니다', response.json())
# 요청 성공 시,    
else:
    token = response.json()
    print(token)