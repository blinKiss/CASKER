import datetime
# [모듈].[객체].함수()
nowtime = datetime.datetime.now()
print('현재 날짜와 시간 : {}'.format(nowtime))

oneul = datetime.date.today()
print('오늘은? : {}'.format(oneul.year),(oneul.month),(oneul.day), sep='-')
print(type(oneul))

# 월을 01 형식으로 나오게 하려면?
today = datetime.date.today().strftime('%Y-%m-%d')
print('현재 날짜 :', today)
print(type(today))
# print(datetime.datetime.today().strftime('%Y-%m-%d'))


lastDay = datetime.date(2023, 6, 29)
print('종강일 : {}'.format(lastDay))

end = lastDay - oneul
print('언제끝나? :', end)

# 임포트때문인지 문자열->데이트 변경이 안돼서 계산이 안됨
# lastDayTwo = datetime.date(2023, 6, 29).strftime('%Y-%m-%d')
# print(type(lastDayTwo))
# todayTwo = datetime.date.strptime(today, '%Y-%m-%d')
# print(type(todayTwo))

# endErr = lastDay - todayTwo
# print('이건 왜 안돼? :' + endErr)



t1 = datetime.time(11 ,15 ,0)
print('현재시간 : {}'.format(t1))

t2 = datetime.time(15, 30 ,0)
print('수업종료 : {}'.format(t2))

dtToday = datetime.datetime.now()
print('{}년'.format(dtToday.year))
print('{}월'.format(dtToday.month))
print('%02d월' % dtToday.month) # 01월로 표시
print('{}일'.format(dtToday.day))
print('{}시'.format(dtToday.hour))
print('{}분'.format(dtToday.minute))
print('{}초'.format(dtToday.second))

endDay = datetime.datetime(2023, 6, 29)

remain = endDay - dtToday
print('며칠 남았나? : {}'.format(remain))
