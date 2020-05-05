
a=input('이름을 입력하세요:')
b=input('전화번호를 입력하세요:')

print('제 이름은', a ,'입니다.')
print('제 전화번호는',b,'입니다')

c = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'

c = c.replace("My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.",
"My naMe is Son Chang Ha, my pin is 000125-3!!!!!!.")
print(c)
c = c.replace("My naMe is Son Chang Ha, my pin is 000125-3!!!!!!.",
"My name is Son Chang Ha, My pin is 000125-3!!!!!!.")
print(c)
c=c.replace("!", "")
print(c)


