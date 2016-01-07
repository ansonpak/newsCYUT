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
    album = addAlbum('https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/487600_1190756514285689_3854036393850684069_n.jpg?oh=97d1cbc31b51fe16ee9a0ead1e327ea4&oe=570CE415', 'text')
    addPhoto(album, 'https://scontent-tpe1-1.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/487600_1190756514285689_3854036393850684069_n.jpg?oh=97d1cbc31b51fe16ee9a0ead1e327ea4&oe=570CE415', '1')
    

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
