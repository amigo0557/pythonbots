from aiogram.types import Message, CallbackQuery
from aiogram import executor

from config import dp
from keyboard import menuStart, menuShirinliklar, menuzakaz, menuZakazBerish, menuZakazBerish1, menuZakazBerish2, menuIchimliklar, menuGoshtmahsulotlari, menuSabzavotlar, menuSutvaTuxum
import logging
from PIL import Image


@dp.message_handler(commands='start')
async def start(message: Message):
    txt = f"Assalomu alaykum {message.from_user.full_name}"
    await message.answer_photo(open("main.jpg", "rb"), reply_markup=menuStart)
    await message.answer(txt, reply_markup=menuStart)
    await message.answer("Foodbotga Xush kelibsiz🤩")


@dp.message_handler(text='Shirinliklar')
async def phones(message: Message):
    await message.answer("O`zingizga kerakli qatorni tanlang👇🏻", reply_markup=menuShirinliklar)


@dp.message_handler(text='Shokolad')
async def samsung1(message: Message):
    text1 = f" Alpen Gold\n" \
            f"Narxi 8,499 so`m\n"
    text2 = f"MaxFun\n" \
            f"Narxi 13,490 so`m\n"
    text3 = f"Milka bubbles\n" \
            f"Narxi 11,999 so`m\n"
    text4 = f"Nestle\n" \
            f"Narxi  7,999 so`m\n"
    text5 = f"Millennium\n" \
            f"Narxi 15,999 so`m\n"

    await message.answer_photo(open("small_1587034777913Alpen5.jpg","rb"), text1, reply_markup=menuzakaz)
    await message.answer_photo(open("small_image_630e15aeb0b65.png","rb"), text2, reply_markup=menuzakaz)
    await message.answer_photo(open("small_1587037690440Milka2.jpg", "rb"), text3, reply_markup=menuzakaz)
    await message.answer_photo(open("small_1601058316056080203-00116.jpg","rb"), text4, reply_markup=menuzakaz)
    await message.answer_photo(open("millenium.jpg", "rb"), text5, reply_markup=menuzakaz)


@dp.message_handler(text='Konfet')
async def apple(message: Message):
    Pobeda = f"Pobeda\n" \
             f"Narxi 119,500 so`m/kg\n"
    PobedaMishka = f"Pobeda Mishka" \
                   f"Narxi 89,900 so`m/kg"
    Mishka = f"Mishka\n" \
             f"Narxi 109,350 so`m/kg\n"
    Serdechka = f"Serdechka\n" \
                f"Narxi 89,950 so`m/kg\n"
    Sonata = f"Sonata\n" \
             f"Narxi 99,450 so`m/kg\n"

    await message.answer_photo(open("medium_1578545843037080211-00154.jpg","rb"), Pobeda, reply_markup=menuzakaz)
    await message.answer_photo(open("mishka.jpg","rb"), PobedaMishka, reply_markup=menuzakaz)
    await message.answer_photo(open("po mishka.jpg","rb"), Mishka, reply_markup=menuzakaz)
    await message.answer_photo(open("serdecka.jpg","rb"), Serdechka, reply_markup=menuzakaz)
    await message.answer_photo(open("sonata.jpg","rb"), Sonata, reply_markup=menuzakaz)


@dp.message_handler(text='Pechenye')
async def redmi(message: Message):
    Korovka = f"Korovka" \
              f"Narxi 21,990 so`m"
    Alenka = f"Alenka\n" \
             f"Narxi 9,990 so`m\n"
    Grona = f"Grona\n" \
            f"Narxi 12,990 so`m\n"
    Yubileynoe = f"Yubileynoe\n" \
                 f"Narxi 6,990 so`m\n"
    Rondo = f"Rondo\n" \
            f"Narxi 2,990 so`m\n"

    await message.answer_photo(open("korvoka.jpg", "rb"), Korovka, reply_markup=menuzakaz)
    await message.answer_photo(open("alenka.jpg", "rb"), Alenka, reply_markup=menuzakaz)
    await message.answer_photo(open("grona.png", "rb"), Grona, reply_markup=menuzakaz)
    await message.answer_photo(open("yubileynoe.jpg", "rb"), Yubileynoe, reply_markup=menuzakaz)
    await message.answer_photo(open("ron.jpg", "rb"), Rondo, reply_markup=menuzakaz)


@dp.message_handler(commands='help')
async def help(message: Message):
    await message.answer("Savollar uchun https://t.me/carlosdeamigo")


# @dp.message_handler(text='Ichimliklar')
# async def note(message: Message):
#     await message.answer("Ichimliklar", reply_markup=menuIchimliklar)


@dp.message_handler(text='Ichimliklar')
async def hp(message: Message):
    Pepsi = f"Pepsi\n" \
               f"Narxi 11000 so`m 1,5L\n"\
               f"Narxi 6000 so`m 0,5L\n"
    CocaCola = f"CocaCola\n" \
               f"Narxi: 10000 so`m 1,5L\n" \
               f"Narxi: 5500 so`m 0,5L\n"
    Fanta = f"Fanta\n" \
            f"Narxi 9000 so`m 1L\n"
    ASU = f"ASU\n" \
          f"Narxi 5000 so`m 1L\n"
    Chortoq = f"Chortoq\n" \
              f"Narxi 9000 so`m\n"
    RedBull = f"Monster\n" \
              f"Narxi 12000 so`m\n"
    Flesh = f"Flesh\n" \
            f"Narxi 9000 so`m\n"
    Bliss = f"Bliss\n" \
            f"Narxi 8500 so`m\n"
    Viko = f"Viko\n" \
           f"Narxi 11500 so`m\n"
    await message.answer_photo(open("pepsi.jpg","rb"), Pepsi, reply_markup=menuzakaz)
    await message.answer_photo(open("kula.jpg","rb"), CocaCola, reply_markup=menuzakaz)
    await message.answer_photo(open("fanta.jpg","rb"), Fanta, reply_markup=menuzakaz)
    await message.answer_photo(open("asu.jpg","rb"), ASU, reply_markup = menuzakaz)
    await message.answer_photo(open("chortoq.jpg","rb"), Chortoq, reply_markup = menuzakaz)
    await message.answer_photo(open("redbull.jpg","rb"), RedBull, reply_markup = menuzakaz)
    await message.answer_photo(open("flesh.jpg","rb"), Flesh, reply_markup = menuzakaz)
    await message.answer_photo(open("bliss.jpg","rb"), Bliss, reply_markup = menuzakaz)
    await message.answer_photo(open("viko.jpg","rb"), Viko, reply_markup = menuzakaz)


# @dp.message_handler(text='Go`sht mahsulotlari')
# async def note(message: Message):
#     await message.answer("Go`sht  mahsulotlari", reply_markup=menuGoshtmahsulotlari)


@dp.message_handler(text='Gosht mahsulotlari')
async def mak(message: Message):
        Goshtboyin = f"Go`sht bo`yin\n" \
                     f"Narxi 77,790 so`m/kg\n"
        Farshmol = f"Farsh mol\n" \
                   f"Narxi 77,000 so`m/kg\n"
        Farshqoy = f"Farsh qo`y\n" \
                   f"Narxi 76,560 so`m/kg\n"
        Tovuqbroyler = f"Tovuq broyler\n" \
                       f"Narxi 34,560 so`m/kg\n"
        Halolkolbasa = f"Sagban kolbasa\n" \
                       f"Narxi 78,560 so`m/kg\n"
        Qazi = f"Qazi\n" \
               f"Narxi 78,560 so`m/kg\n"
        await message.answer_photo(open("gosht mol.jpg", "rb"), Goshtboyin, reply_markup=menuzakaz)
        await message.answer_photo(open("farshmol.jpg", "rb"), Farshmol, reply_markup=menuzakaz)
        await message.answer_photo(open("farsh.jpg", "rb"), Farshqoy, reply_markup=menuzakaz)
        await message.answer_photo(open("tovuq.jpg", "rb"), Tovuqbroyler, reply_markup=menuzakaz)
        await message.answer_photo(open("sagban.jpg", "rb"), Halolkolbasa, reply_markup=menuzakaz)
        await message.answer_photo(open("qazi.jpg", "rb"), Qazi, reply_markup=menuzakaz)


# @dp.message_handler(text='Mevalar')
# async def note(message: Message):
#     await message.answer("Mevalar", reply_markup=menuGoshtmahsulotlari)


@dp.message_handler(text='Mevalar')
async def asus(message: Message):
    Olma = f"Olma\n" \
           f"Narxi 11,990 so`m/kg\n"
    Nok = f"Nok\n" \
          f"Narxi 25,990 so`m/kg\n"
    Uzum = f"Uzum\n" \
           f"Narxi 39,990 so`m/kg\n"
    Behi = f"Behi\n" \
           f"Narxi 19,900 so`m/kg\n"
    Kivi = f"Kivi\n" \
           f"Narxi 19,990 so`m/kg\n"
    Apelsin = f"Apelsin\n" \
              f"Narxi 33,990 so`m/kg\n"

    await message.answer_photo(open("olma.jpg", "rb"), Olma, reply_markup=menuzakaz)
    await message.answer_photo(open("nok.jpg", "rb"), Nok, reply_markup=menuzakaz)
    await message.answer_photo(open("uzum.jpg", "rb"), Uzum, reply_markup=menuzakaz)
    await message.answer_photo(open("behi.jpg", "rb"), Behi, reply_markup=menuzakaz)
    await message.answer_photo(open("kivi.jpg", "rb"), Kivi, reply_markup=menuzakaz)
    await message.answer_photo(open("apelsin.jpg", "rb"), Apelsin, reply_markup=menuzakaz)


# @dp.message_handler(text='Sabzavotlar')
# async def note(message: Message):
#     await message.answer("Sabzavotlar", reply_markup=menuSabzavotlar)


@dp.message_handler(text='Sabzavotlar')
async def tex(message: Message):
    Sabzi = f"Sabzi\n" \
            f"Narxi 5,490 so`m/kg\n"
    Piyoz = f"Piyoz\n" \
            f"Narxi 3,990 so`m/kg\n"
    Kartoshka = f"Kartoshka\n" \
                f"Narxi 5,890 so`m/kg\n"
    Pomidor = f"Pomidor\n" \
              f"Narxi 26,100 so`m/kg\n"
    Bodring = f"Bodring\n" \
              f"Narxi 16,990 so`m/kg\n"
    Karam = f"Karam\n" \
            f"Narxi: 2,100 so`m/kg\n"

    await message.answer_photo(open("sabzi.jpg", "rb"), Sabzi, reply_markup=menuzakaz)
    await message.answer_photo(open("piyoz.jpg", "rb"), Piyoz, reply_markup=menuzakaz)
    await message.answer_photo(open("kartoshka.jpg", "rb"), Kartoshka, reply_markup=menuzakaz)
    await message.answer_photo(open("pomidor.jpg", "rb"), Pomidor, reply_markup=menuzakaz)
    await message.answer_photo(open("bodring.jpg", "rb"), Bodring, reply_markup=menuzakaz)
    await message.answer_photo(open("karam.jpg", "rb"), Karam, reply_markup=menuzakaz)


# @dp.message_handler(text='Sut va tuxum')
# async def note(message: Message):
#     await message.answer("Sut va tuxum", reply_markup=menuSutvaTuxum)


@dp.message_handler(text='Sut va tuxum')
async def tex(message: Message):
    Sut = f"Sut\n" \
          f"Narxi 10,990 so`m 1L\n"
    Tuxum = f"Tuxum\n" \
            f"Narxi 48,990 so`m 30ta\n"
    Saryog = f"Saryog President\n" \
             f"Narxi: 37,560 so`m\n"
    Qatiq = f"Qatiq\n" \
            f"Narxi 14,490 so`m\n"
    Yogurt = f"Yogurt\n" \
             f"Narxi 7,990 so`m\n"
    Smetana = f"Smetana\n" \
              f"Narxi 18,590 so`m\n"
    Bedanatuxumi = f"Bedana tuxumi\n" \
                   f"Narxi 8,400 so`m 12ta\n"

    await message.answer_photo(open("sut.jpg", "rb"), Sut, reply_markup=menuzakaz)
    await message.answer_photo(open("tuxum.jpg", "rb"), Tuxum, reply_markup=menuzakaz)
    await message.answer_photo(open("kefir.jpg", "rb"), Qatiq, reply_markup=menuzakaz)
    await message.answer_photo(open("saryog.jpg", "rb"), Saryog, reply_markup=menuzakaz)
    await message.answer_photo(open("yogurt.jpg", "rb"), Yogurt, reply_markup=menuzakaz)
    await message.answer_photo(open("smetana.jpg", "rb"), Smetana, reply_markup=menuzakaz)
    await message.answer_photo(open("bedanatuxum.jpg", "rb"), Bedanatuxumi, reply_markup=menuzakaz)


@dp.message_handler(text="Orqaga👈")
async def orqa(message: Message):
    await message.answer("Orqaga", reply_markup=menuStart)


@dp.callback_query_handler(text="Zakaz")
async def zakaz(call: CallbackQuery):
    await call.message.answer("Contact va Locationni yuboring", reply_markup=menuZakazBerish2)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="Location")
async def zakaz1(call: CallbackQuery):
    await call.message.answer("zakaz uchun joyingizni jo'nating", menuZakazBerish1)


@dp.callback_query_handler(text="Contact")
async def zakaz1(call: CallbackQuery):
    txt = "Zakazingiz qabul qilindi"
    await call.message.answer("zakaz uchun kontaktingizni jo'nating", txt, menuZakazBerish)
    try:
       await call.message.answer("Zakazingiz qabul qilindi")
    except IOError:
        return



@dp.callback_query_handler(text="Orqaga👈")
async def orqaga(call: CallbackQuery):
    await call.message.answer("orqaga", reply_markup=menuShirinliklar)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="Bosh Menu🏠")
async def menus(call: CallbackQuery):
    await call.message.answer("Bosh Menu🏠", reply_markup=menuStart)


@dp.message_handler(text="Bosh Menu🏠")
async def menu(message: Message):
    await message.answer("Bosh Menu🏠", reply_markup=menuStart)


if __name__ == '__main__':
    executor.start_polling(dp)
