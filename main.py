meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK": "Klavyeden uzakta",
            "GG": "Güzel oyun",
            "WP": "İyi Oynuyorsun",
            "F2P": "parasız oynayan",
            "NT": "Eline sağlık",
            "FPS": "saniyedeki kare sayısı",
            "GLHF": "İyi Şanslar iyi şanslar"
            }
for i in range(5):            
    kelime = input("Kelime girin")

    if kelime in meme_dict.keys():
        print(meme_dict[kelime])
    
    else:
        print("Kelime yok listede...")
