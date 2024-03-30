from collections import Counter

msg = "Je m'appelle Jessica. Je suis une fille, je suis française et j'ai treize ans. Je vais à l'école à Nice, mais j'habite à Cagnes-Sur-Mer. J'ai deux frères. Le premier s'appelle Thomas, il a quatorze ans. Le second s'appelle Yann et il a neuf ans. Mon papa est italien et il est fleuriste. Ma mère est allemande et est avocate. Mes frères et moi parlons français, italien et allemand à la maison. Nous avons une grande maison avec un chien, un poisson et deux chats.Aujourd'hui, on est samedi, nous rendons visite à notre grand-mère. Elle a 84 ans et elle habite à Antibes. J'adore ma grand-mère, elle est très gentille. Elle fait des bons gâteaux.Lundi, je retourne à l'école. Je suis contente, je vais voir Amélie. C'est ma meilleure amie. J'aime beaucoup l'école. Mes matières préférées sont le français et le sport. J'aime beaucoup lire et je nage très bien."

key = 1

msg = msg.replace("."," ")
msg = msg.replace(","," ")
msg = msg.replace("'"," ")
msg = msg.replace("-"," ")
msg = msg.upper()


msg_crypted = ""


for letter in msg :
    print()
    l = ord(letter)  + key
    newLetter = chr(l )
    msg_crypted =msg_crypted+ newLetter

print(msg_crypted)

# je suppose eli hedha en français

# letter e la plus occurente

# rechercher dans le message 

crypted_msg = "KF N BQQFMMF KFTTJDB  KF TVJT VOF GJMMF  KF TVJT GSBOÈBJTF FU K BJ USFJ[F BOT  KF WBJT Á M ÊDPMF Á OJDF  NBJT K IBCJUF Á DBHOFT TVS NFS  K BJ EFVY GSÉSFT  MF QSFNJFS T BQQFMMF UIPNBT  JM B RVBUPS[F BOT  MF TFDPOE T BQQFMMF ZBOO FU JM B OFVG BOT  NPO QBQB FTU JUBMJFO FU JM FTU GMFVSJTUF  NB NÉSF FTU BMMFNBOEF FU FTU BWPDBUF  NFT GSÉSFT FU NPJ QBSMPOT GSBOÈBJT  JUBMJFO FU BMMFNBOE Á MB NBJTPO  OPVT BWPOT VOF HSBOEF NBJTPO BWFD VO DIJFO  VO QPJTTPO FU EFVY DIBUT BVKPVSE IVJ  PO FTU TBNFEJ  OPVT SFOEPOT WJTJUF Á OPUSF HSBOE NÉSF  FMMF B 95 BOT FU FMMF IBCJUF Á BOUJCFT  K BEPSF NB HSBOE NÉSF  FMMF FTU USÉT HFOUJMMF  FMMF GBJU EFT CPOT HÃUFBVY MVOEJ  KF SFUPVSOF Á M ÊDPMF  KF TVJT DPOUFOUF  KF WBJT WPJS BNÊMJF  D FTU NB NFJMMFVSF BNJF  K BJNF CFBVDPVQ M ÊDPMF  NFT NBUJÉSFT QSÊGÊSÊFT TPOU MF GSBOÈBJT FU MF TQPSU  K BJNF CFBVDPVQ MJSF FU KF OBHF USÉT CJFO "


count = Counter(crypted_msg)

print(count)
"""max = count.values()[0]
for el in count.keys():
    if(max<count[el]):
        max = count[el]
        print(el)

print(max)"""


decrypted = ""
for letter in crypted_msg :
    l = ord(letter)  - 1
    newLetter = chr(l)
    decrypter =decrypted+ newLetter

print(decrypter)