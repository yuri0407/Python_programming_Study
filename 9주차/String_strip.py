ss = '     파  이  썬     '
print(ss.strip())      #'파  이  썬'
print(ss.rstrip())     #'     파  이  썬'
print(ss.lstrip())     #'파  이  썬     '

ss = '-----파  이  썬-----'
print(ss.strip('-'))

ss = '<<<파 << 이 >> 썬>>>'
print(ss.strip('<>'))