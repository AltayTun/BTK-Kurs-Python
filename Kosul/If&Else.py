kulad="sadikturan"
sifre="1234"

# dogrulama=kulad=="sadikturan" and sifre=="1234"

# if dogrulama:
#     {
# print(f'Hoşgeldiniz {kulad}')
#     }
#     print("Kullanıcı adı veya şifreniz hatalı lütfen tekrar deneyiniz")

if kulad=="sadikturan" :
    if sifre=="1234":
        print(f'Hoşgeldiniz {kulad}')
    else:print("Şifrenizi eksik ya da hatalı tuşladınız lütfen tekrar deneyin")
else:
    print("Kullanıcı Adınızı eksik ya da yanlış tuşladınız")