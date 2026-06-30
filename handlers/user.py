from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.reply import main_menu
from keyboards.inline import courses_keyboard, register_keyboard, hello_btn
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import admin_id
router = Router()

class Registration(StatesGroup):
    name = State()
    age = State()
    course = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в Intellect Academy!",
        reply_markup=main_menu
    )
    
@router.message(F.text.lower() == "📞 контакты")
async def reply_contacts(message: Message):
    await message.reply("""
        👨🏼 Менеджер: +996767676767\n                
📍Адрес: ул Ж Бакиева 16 Кайнар БЦ 2 этаж                
                        """)
    


@router.message(F.text.lower() == "📚 курсы")
async def reply_courses(message:Message):
    await message.answer("Наши курсы:", reply_markup=courses_keyboard)

@router.message(F.data.startswith("hello_"))
async def reply_hello(callback: CallbackQuery):
    await callback.message.reply(text="И тебе привет")

courses_info = {
"course_english": {
    "id": 1,
    "name": "🇬🇧 Английский язык",
    "description": "Изучение грамматики, разговорной речи, чтения и письма.",
    "price": 5000,
    "duration": 3
},
"course_it": {
    "id": 2,
    "name": "💻 Программирование",
    "description": "Изучение языков программирования и создание проектов.",
    "price": 7000,
    "duration": 6
},
"course_art": {
    "id": 3,
    "name": "🎨 Графический дизайн",
    "description": "Освоение инструментов дизайна и создание визуального контента.",
    "price": 6000,
    "duration": 4
},
"course_smm": {
    "id": 4,
    "name": "📊 Маркетинг и SMM",
    "description": "Продвижение брендов в социальных сетях и настройка рекламы.",
    "price": 5500,
    "duration": 3
},
"course_ORT": {
    "id": 5,
    "name": "📚 Подготовка к ОРТ",
    "description": "Подготовка к тестированию с практикой и разбором заданий.",
    "price": 4500,
    "duration": 5
},
"course_math": {
    "id": 6,
    "name": "🧮 Математика",
    "description": "Изучение школьной и углублённой математики.",
    "price": 4000,
    "duration": 4
},
"course_voice": {
    "id": 7,
    "name": "🎤 Ораторское мастерство",
    "description": "Развитие навыков публичных выступлений и уверенной речи.",
    "price": 5000,
    "duration": 2
    }
}

@router.callback_query(F.data.startswith("course_"))
async def course_handler(callback: CallbackQuery):
    course_key = callback.data
    
    if course_key in courses_info:
        info = courses_info[course_key]
        
        text = (
            f"Название: {info['name']}\n"
            f"Длительность: {info['duration']} мес.\n"
            f"Стоимость: {info['price']} сом\n\n"
            f"Описание: {info['description']}"
        )
        
        await callback.message.reply(
            text=text, 
            reply_markup=register_keyboard(course_key)
        )

    await callback.answer()



@router.callback_query(F.data.startswith("register_"))
async def register(callback: CallbackQuery, state: FSMContext):

    # print(callback.data)
    await state.set_state(Registration.name)
    await callback.message.reply("Введите ваше ФИО")


@router.message(Registration.name)
async def register_two(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Registration.age)
    await message.answer("Введите ваш возраст")

@router.message(Registration.age)
async def register_second(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Registration.course)
    await message.answer("Введите курс на который хотите записаться")

@router.message(Registration.course)
async def register_third(message: Message, state: FSMContext):
    await state.update_data(course = message.text)
    data = await state.get_data()
    text = f"Спасибо, вы успешно зарегистрированы\nФИО: {data['name']}\nВозраст: {data['age']}\nКурс: {data['course']}"
    await message.bot.send_message(chat_id=int(admin_id), text=text)
    await message.answer(text)




    await state.clear()
