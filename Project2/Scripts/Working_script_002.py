import pandas as pd
from transliterate import translit  # make sure you have `pip install transliterate`

# -----------------------
# 1️⃣ Load your CSV
# Keep empty cells as empty strings, not NaN
# -----------------------
df = pd.read_csv("tajik_ethnicity_in_Russia.csv", encoding="utf-8-sig", keep_default_na=False)

# -----------------------
# 2️⃣ Translation dictionaries
# -----------------------
# Regions
region_dict = {
    "Москва": "Moscow",
    "Санкт-Петербург": "Saint Petersburg",
    "Республика Башкортостан": "Republic of Bashkortostan",
    "Республика Татарстан": "Republic of Tatarstan",
    "Республика Марий Эл": "Republic of Mari El",
    "Республика Мордовия": "Republic of Mordovia",
    "Удмуртская Республика": "Udmurt Republic",
    "Чувашская Республика": "Chuvash Republic",
    "Республика Алтай": "Altai Republic",
    "Республика Тыва": "Tuva Republic",
    "Республика Хакасия": "Khakassia Republic",
    "Республика Карелия": "Republic of Karelia",
    "Республика Коми": "Komi Republic",
    "Республика Адыгея": "Republic of Adygea",
    "Республика Калмыкия": "Republic of Kalmykia",
    "Республика Крым": "Republic of Crimea",
    "Республика Дагестан": "Republic of Dagestan",
    "Республика Ингушетия": "Republic of Ingushetia",
    "Кабардино-Балкарская Республика": "Kabardino-Balkar Republic",
    "Карачаево-Черкесская Республика": "Karachay-Cherkess Republic",
    "Республика Северная Осетия - Алания": "Republic of North Ossetia–Alania",
    "Чеченская Республика": "Chechen Republic",
    "Марий Эл": "Mari El Republic",
    "Таджикистан": "Tajikistan"
}

# Purposes
purpose_dict = {
    "работу": "Work",
    "учебу": "Study",
    "частную поездку": "Private Visit",
    "служебную или деловую поездку": "Business Trip",
    "туризм, отдых": "Tourism/Leisure",
    "транзитное перемещение": "Transit",
    "другую цель": "Other Purpose"
}

# Column headers
col_header_dict = {
    "Регион": "Region",
    "Всего": "Total",
    "Указавшие цель приезда": "Purpose_Declared_Total",
    "работу": "Work",
    "учебу": "Study",
    "частную поездку": "Private Visit",
    "служебную или деловую поездку": "Business Trip",
    "туризм, отдых": "Tourism/Leisure",
    "транзитное перемещение": "Transit",
    "другую цель": "Other Purpose",
    "Не указавшие цель приезда": "Purpose_Not_Declared_Total"
}

# -----------------------
# 3️⃣ Function to translate or transliterate
# -----------------------
def translate_or_latin(value, mapping_dict):
    value = str(value).strip()
    if value == "":
        return ""  # Keep empty cells
    if value in mapping_dict:
        return mapping_dict[value]
    elif any('А' <= c <= 'я' for c in value):
        return translit(value, 'ru', reversed=True)  # Transliterate remaining Cyrillic
    else:
        return value  # Already English / number

# -----------------------
# 4️⃣ Rename columns
# -----------------------
df.rename(columns=col_header_dict, inplace=True)

# -----------------------
# 5️⃣ Add a separate column for English/Latin Region
# -----------------------
df['Region_EN'] = df['Region'].apply(lambda x: translate_or_latin(x, region_dict))

# -----------------------
# 6️⃣ Apply translation/transliteration to purpose columns
# -----------------------
for col in ["Work","Study","Private Visit","Business Trip","Tourism/Leisure","Transit","Other Purpose"]:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: translate_or_latin(x, purpose_dict))

# Total / Not Declared columns (transliterate if anything remains)
for col in ["Purpose_Declared_Total","Purpose_Not_Declared_Total","Total"]:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: translate_or_latin(x, {}))

# -----------------------
# 7️⃣ Save final CSV
# -----------------------
df.to_csv("tajik_ethnicity_in_Russia_EN_Latin_v2.csv", index=False, encoding="utf-8-sig")

print("DONE ✅ Full table translated with separate English Region column, empty cells preserved")
