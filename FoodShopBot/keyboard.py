from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shirinliklar"),
            KeyboardButton(text="Ichimliklar"),
            KeyboardButton(text="Gosht mahsulotlari")],
        [
            KeyboardButton(text="Mevalar"),
            KeyboardButton(text="Sabzavotlar"),
            KeyboardButton(text="Sut va tuxum"),
        ],
    ],
    resize_keyboard=True
)
menuShirinliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="Konfet"),
             KeyboardButton(text="Shokolad"),
             KeyboardButton(text="Pechenye"),
             KeyboardButton(text="Orqaga👈")
        ],
    ],
    resize_keyboard=True
)
menuIchimliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="CocaCola"),
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="ASU"),
            KeyboardButton(text="Chortoq"),
            KeyboardButton(text="Monster"),
            KeyboardButton(text="Godzilla"),
            KeyboardButton(text="Bliss"),
            KeyboardButton(text="Viko"),
            KeyboardButton(text="Orqaga👈")
                ],
            ],
    resize_keyboard=True
)
menuGoshtmahsulotlari = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="Gosht bo`yin"),
             KeyboardButton(text="Farsh mol"),
             KeyboardButton(text="Farsh qo`y"),
             KeyboardButton(text="Tovuq broyler"),
             KeyboardButton(text="Sagban kolbasa"),
             KeyboardButton(text="Qazi"),
             KeyboardButton(text="Orqaga👈")
        ],
    ],
    resize_keyboard=True
)
menuMevalar = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="Olma"),
             KeyboardButton(text="Xurmo"),
             KeyboardButton(text="Uzum"),
             KeyboardButton(text="Behi"),
             KeyboardButton(text="Mango"),
             KeyboardButton(text="Apelsin"),
             KeyboardButton(text="Orqaga👈")
        ],
    ],
    resize_keyboard=True
)
menuSabzavotlar = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="Sabzi"),
             KeyboardButton(text="Piyoz"),
             KeyboardButton(text="Kartoshka"),
             KeyboardButton(text="Pomidor"),
             KeyboardButton(text="Bodring"),
             KeyboardButton(text="Karam"),
             KeyboardButton(text="Orqaga👈")
        ],
    ],
    resize_keyboard=True
)
menuSutvaTuxum = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="Sut"),
             KeyboardButton(text="Tuxum"),
             KeyboardButton(text="Qatiq"),
             KeyboardButton(text="Yogurt"),
             KeyboardButton(text="Smetana"),
             KeyboardButton(text="Bedana tuxumi"),
             KeyboardButton(text="Orqaga👈")
        ],
    ],
    resize_keyboard=True
)
menuZakazBerish2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
            KeyboardButton(text="Location", request_location=True),
            KeyboardButton(text="Bosh Menu🏠")
        ],
    ],
    resize_keyboard=True
)
menuZakazBerish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
        ],
    ],
    resize_keyboard=True
)
menuZakazBerish1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location", request_location=True)
        ],
    ],
    resize_keyboard=True
)
menuzakaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zakaz", callback_data="Zakaz"),
            InlineKeyboardButton(text="Orqaga👈", callback_data="Orqaga👈"),
            InlineKeyboardButton(text="Bosh Menu🏠", callback_data="Bosh Menu🏠")
        ]
    ]
)
