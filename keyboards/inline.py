from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

courses = {
  "course_english": "🇬🇧 Английский язык",
  "course_it": "💻 Программирование",
  "course_art": "🎨 Графический дизайн",
  "course_smm": "📊 Маркетинг и SMM",
  "course_ORT": "📚 Подготовка к ОРТ",
  "course_math": "🧮 Математика",
  "course_voice": "🎤 Ораторское мастерство"
}

inline_list = []

for i in courses:
  btn = [
    InlineKeyboardButton(
      text=courses[i],
      callback_data=i
    )
  ]
  inline_list.append(btn)


courses_keyboard = InlineKeyboardMarkup(
  inline_keyboard=inline_list
)

def register_keyboard(course):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📝 Записаться на курс", 
                    callback_data=f"register_{course}"
                )
            ]
        ]
    )

hello_btn = InlineKeyboardMarkup(
  inline_keyboard = [
      [InlineKeyboardButton(text="Привет", callback_data="hello_")]
  ]
)

