import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsCYUT.settings')
import django
django.setup()
from news.models import Latestnews
from photo.models import Album, Photo

def populate():
    latestnews = addLatestnews('【8/16 新生暨家長歡迎會】', '來見見自己的同學及班導師吧！除了參觀宿舍及圖書館還抽筆記型電腦就等你來呦資管系學會歡迎您照片中身穿紅色衣服的都是系學會的學長姐們，當天如有任何問題或需要幫忙的不要害羞歡迎來找我們哦！', '2015-8-14')
    latestnews = addLatestnews('【驚豔資管 ● 迎新茶會】', '謝謝有你真好！', '2015-09-09')
    latestnews = addLatestnews('【104上學期 系升旗時間】', '★ 就在本週四 上午7:45 ★各班位置如圖，1年級位置在面向司令台「右側」我們不見不散 😁※ 各班代務必提醒班上同學※ 若與勞作教育衝突，請與各小組長聯絡 🌟※ 此為重大集會，未到者將扣操行成績', '2015-09-19')
    latestnews = addLatestnews('【一資獨秀 迎新晚會】', '感謝最熱情的學弟妹們共同響應全國制服日一起來參加迎新晚會 !!不知道各位學弟妹有沒有平安到家呢也祝你們有個美好的一晚🌟 22th資管系學會感謝你 🌟', '2015-09-30')
    latestnews = addLatestnews('【拾隨資味驚艷卡通大進擊】', '希望這兩天能夠帶給你大學生涯中一段美好的回憶 ☺照片已經上傳完成記得到新生交流版回味一下呦 ！2015.10.09 資管系迎新露營 -＃‎宣導‬：網路購物要小心，詐騙案層出不窮，低於市價、拒絕面交、無法驗貨、強烈要求盡快匯款，可能就是詐騙，冷靜、查證、撥打165、110 保障財產安全，辛苦錢別輕易被騙走了!', '2015-10-15')
    latestnews = addLatestnews('【露營晚會 Pro Dance】', '久等了！👑 快閃11人 👑現在 精彩重現！YouTube：https://youtu.be/p7Xog39ufrk (HQ)', '2015-10-21')
    latestnews = addLatestnews('【露營晚會 香舞演出】', '🌟 叭噗叭噗香舞團 🌟現在 精彩重現！YouTube：https://youtu.be/m0yGnoWLpr8 (HQ)', '2015-10-21')
    latestnews = addLatestnews('【露營晚會 火棍演出】', '🔥 機甲神棍 🔥現在 精彩重現！YouTube：https://youtu.be/BbFO0jkPDXY (HQ)', '2015-10-21')
    latestnews = addLatestnews('【Coco 與你有約】', '塗城、二宿附近這兩間都有優惠呦！詳情不囉嗦直接上圖霧峰店：台中市霧峰區中正路910號大里店：台中市大里區塗城路494號', '2015-11-09')
    latestnews = addLatestnews('【週二朝陽資管系服日】', '眾所期待 !!朝陽資管系服日來啦拿出你的系服每週二穿上它讓朝陽充滿 IM神秘活動敬請期待 !', '2015-11-16')
    latestnews = addLatestnews('【朝陽食物暨社會與文化銀行】', '💡 這是一個跨傳播系、資管系、社工系三個領域的學程，同學在大學修讀期間可以擁有不同的專業技能、認識不同專業領域的同學，會讓你在畢業後更吃香！欲了解詳情的二年級同學們歡迎你在 11/30 (一) 12:00~13:30 參與課程說明會當天備有午餐如有問題可私訊資管系會長許嘉元⬇ 歡迎您報名參加 ⬇報名網址：http://ppt.cc/Lw9G5', '2015-11-20')
    latestnews = addLatestnews('【‪#‎週二資管系服日‬ - 1. 王少澧】', '帥氣 Love 資管會長來啦！週二系服日 👍每週都有每週都穿 下週封面人物是誰呢 ?還是先揭曉一下神秘活動沒有往下滑你就不知道啦 ~【這12家餐廳 週二秀出系服立馬優惠】活動時間：本學期每週二 (阿德師除外)⚠ 身穿系服才有優惠呦 ⚠《第一餐廳》熊大心：牛肉粥 折5元 阿德師：焗烤飯 折5元 (12/15前的每週二)享半天：飲品 折5元《第二餐廳》菲珈露：海苔飯卷 折5元 (50元以上)天慈素食：餐點 折5元 (50元以上)茶香園： 飲品9折食神：餐點 折5元金讚：免費多加一樣菜(油豆腐)《第三餐廳》黃師傅：炒飯燴飯 折 5 元 (1點後供應)古早味：香草豬排 三份折5元左撇子：豆芽菜 折5元香園燒臘：蔬食餐點 折5元活動未詳事宜請依現場公告! 準備好系服享受折扣吧 😃', '2015-11-22')
    latestnews = addLatestnews('【系際盃合唱團 即時】', '恭喜資管系榮獲【三大獎】創意組 季軍創意組 最佳伴奏獎創意組 最佳指揮獎https://youtu.be/mTEqS0AE8I8（側面拍攝）https://youtu.be/DeoRpfodZqA（正面拍攝）照片再等我們一下！太開心啦！', '2015-12-01')
    latestnews = addLatestnews('【‪#‎週二資管系服日‬ - 2. 曾信豪】', '本週邀請在迎新晚會脫穎而出的資管系草他是 1A 曾信豪 👍週二系服日每週都有每週都穿 穿系服用餐【立馬享優惠】快用新台幣下架它們 !🔔 資管系服日 特約商家 🔔《第一餐廳》熊大心：牛肉粥 折5元 阿德師：焗烤飯 折5元 (12/15前的每週二)享半天：飲品 折5元《第二餐廳》菲珈露：海苔飯卷 折5元 (50元以上)天慈素食：餐點 折5元 (50元以上)茶香園： 飲品9折食神：餐點 折5金讚：免費多加一樣菜(油豆腐)《第三餐廳》黃師傅：炒飯燴飯 折 5 元 (1點後供應)古早味：香草豬排 三份折5元左撇子：豆芽菜 折5元香園燒臘：蔬食餐點 折5元活動未詳事宜請依現場公告! 準備好系服享受折扣吧 😃', '2015-12-07')
    album = addAlbum('https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/487600_1190756514285689_3854036393850684069_n.jpg?oh=97d1cbc31b51fe16ee9a0ead1e327ea4&oe=570CE415', '聖誕活動')
    addPhoto(album, 'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/487600_1190756514285689_3854036393850684069_n.jpg?oh=97d1cbc31b51fe16ee9a0ead1e327ea4&oe=570CE415', '今年聖誕，資管系學會前進朝陽幼稚園，與小朋友們一起完成屬於自己的聖誕襪，也很榮幸能與小朋友們一起度過一段歡樂時光，祝福他們也祝福大家：聖誕快樂 Merry Chrismas !')
    addPhoto(album, 'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/1460947_1190756520952355_8841875966028184751_n.jpg?oh=432979c197c56eda31cdfb02c3dce173&oe=570E3C89', '今年聖誕，資管系學會前進朝陽幼稚園，與小朋友們一起完成屬於自己的聖誕襪，也很榮幸能與小朋友們一起度過一段歡樂時光，祝福他們也祝福大家：聖誕快樂 Merry Chrismas !')
    album = addAlbum('https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/12308386_1180744885286852_7460973740773158190_n.jpg?oh=fc53eaf2172f7550297bf2c8b17c2e18&oe=5715AA5A', '資管系體育週')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xft1/v/t1.0-9/1915219_1190543367640337_3065591711135270816_n.jpg?oh=bb0233e05428ba65a7b957cf2aa175a8&oe=57119E5F', '恭喜【叫我喇叭會長】獲得籃球冠軍！感謝各工作人員及參與這場活動的朋友們，資管體育週在今天將告一段落，明年體育週我們再相會！即將畢業的學長姐，下學期的資訊週我們一樣歡迎你稱霸資訊學院！籃球其他得獎消息：恭喜【統一AV又露乳】獲得亞軍！恭喜【鳳山LaBron劉彥廷】獲得季軍！')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xlp1/v/t1.0-9/10550835_1190544224306918_3501377806548707255_n.jpg?oh=1a34a4405f79fd1d4878cf23b6c6845b&oe=5744EB09', '恭喜【大牙齒】獲得排球冠軍！感謝各工作人員及參與這場活動的朋友們，資管體育週在今天將告一段落，明年體育週我們再相會！即將畢業的學長姐，下學期的資訊週我們一樣歡迎你稱霸資訊學院！排球其他得獎消息：恭喜【歐蜜抖虎】獲得亞軍！恭喜【地瓜是會呱呱叫的球】獲得季軍！')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/12308386_1180744885286852_7460973740773158190_n.jpg?oh=fc53eaf2172f7550297bf2c8b17c2e18&oe=5715AA5A', '【資管體育週 報名開催】🎉一年一度的體育週開跑啦！延續去年榮耀的你誓言討回冠軍的你剛來朝陽資管的你12/21 (一) - 12/25打出你的籃球信仰成為資管排球之神 【 男籃 / 女籃 / 男女混排 】① 找班代② 領取報名表③ 繳至資管系學會信箱③ 注意報名至 12/14 17:00③ 信箱在系辦④ 留言區有圖解⑤ 記得來抽籤 12/15 中午我們等你來 battle !!')
    album = addAlbum('https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xpf1/v/t1.0-9/12313669_1174326582595349_8427914277186526831_n.jpg?oh=a098fa78219263c8fb129fed2e8847a5&oe=56FC2F09', '系合唱比賽')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xpf1/v/t1.0-9/12313669_1174326582595349_8427914277186526831_n.jpg?oh=a098fa78219263c8fb129fed2e8847a5&oe=56FC2F09', '經過一個多月的努力系合唱比賽已經進入倒數階段囉相信學長姐準備的澎大海以及主任老師系辦學姐的加持鼓勵之下能讓你們利咽開音迎接週二挑戰12/1 (二) 設計禮堂 17:34 資管開唱 (15點入場)🔥 朝陽資管恩哈哈系合唱 Fighting!')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xlp1/v/t1.0-9/12311037_1175764832451524_4139229812972645322_n.jpg?oh=9aef05ee011b0101c95fde76a60312fd&oe=571556BF', '#回憶是今年合唱的主軸四首歌分別代表著四段回憶 -回憶以前在追老婆的時候 ....與老婆的熱戀期，從結婚到生下小孩的種種回憶 ...12/1 (二) 設計禮堂 17:34 資管登場.#週二資管系服日 http://ppt.cc/LBQAk剛好也是合唱團比賽日歡迎穿著系服共襄盛舉多間學餐享有優惠唷！#系徽系旗投票 11/30~12/03資訊大樓五樓 你的一票決定資管系學會投票再抽多樣好禮記得要來呦 😘')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/12301459_1176226932405314_4104889849670824544_n.jpg?oh=1c958c248bbdb28eb6ed87f0c380bf7e&oe=570F0167', '人家說，比賽之前是辛苦的。但，比賽之後是值得的。努力練習一個月就為了明天相信你們會成功，衝吧！資管系！12/1 (二) 設計禮堂 17:34 資管登場 ！(三點入場)🌟 歡迎穿著系服 用行動支持資管系 🌟#週二資管系服日 http://ppt.cc/LBQAk朝陽學餐12家優惠實施中朝陽資管加油 ！！')
    addPhoto(album,'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/12295243_1177917612236246_8055201388919968162_n.jpg?oh=676c3b391d22d6348a0ad3da47ca0e7c&oe=57158E5F', '12/1 歷史性的一刻總副召學弟妹學長姐全資管系一起締造合唱團的榮耀得來真的不易資管是今年唯一榮獲三大獎的系所最佳指揮與伴奏更打破資管系 22 年以來的紀錄所以沒看過的一定要看看過的值得你再次回味🎥 https://youtu.be/DeoRpfodZqA 🎥#創意組季軍#最佳伴奏 李昱蓁#最佳指揮 李家宇無論你有沒有參加資管合唱團明年校慶啦啦隊比賽邀你一起為資管系締造神話一起創造下一個更美好的回憶 !')
    
def addLatestnews(title,content,uploadDate):
    latestnews = Latestnews.objects.get_or_create(title=title,content=content,uploadDate=uploadDate)[0]
    return latestnews

def addAlbum(url, title):
    album = Album.objects.get_or_create(photourl=url, albumtitle=title)[0]
    return album

def addPhoto(album, url, index):
    photo = Photo.objects.get_or_create(album=album, url=url, index=index)[0]
    photo.save()

if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 
