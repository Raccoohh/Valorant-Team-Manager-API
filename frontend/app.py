import streamlit as st
import requests
import pandas as pd
import os

# Якщо змінна BACKEND_URL задана (в Docker) — беремо її, інакше — локальний шлях
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
API_URL = BACKEND_URL

# Налаштування сторінки (широкий формат, темна тема підтягується автоматично)
st.set_page_config(
    page_title="no talent | Valorant Analytics",
    page_icon="🎯",
    layout="wide"
)

# === САЙДБАР (Бокове меню) ===
with st.sidebar:
    st.title("🎯 no talent HQ")
    st.markdown("Панель управління складом та ШІ-аналітика матчів.")
    st.divider()
    st.info("💡 **Порада:** Спочатку знайди гравця, скопіюй його ID матчу з історії, а потім запускай AI Coach.")

st.title("Valorant Team Manager Dashboard")
st.divider()

# Створюємо дві колонки для зручної розмітки
col1, col2 = st.columns([1, 1])

# === БЛОК 1: ДОДАВАННЯ ГРАВЦЯ ===
with col1:
    st.subheader("📝 Реєстрація нового гравця")
    
    with st.form("add_player_form", clear_on_submit=True):
        nickname = st.text_input("Нікнейм (Nickname)", placeholder="Young")
        riot_id = st.text_input("Riot ID", placeholder="Name#Tag")
        role = st.selectbox("Ігрова роль", ["Duelist", "Initiator", "Controller", "Sentinel"])
        discord_tag = st.text_input("Discord Tag", placeholder="raccoohh#1234")
        
        submitted = st.form_submit_button("➕ Додати гравця")
        
        if submitted:
            if not riot_id or "#" not in riot_id:
                st.error("Помилка: Riot ID має бути у форматі Name#Tag")
            else:
                # Збираємо payload (зверни увагу, що role та discord ми додаємо на майбутнє, 
                # якщо твій бекенд PlayerCreate їх ще не приймає, вони просто проігноруються)
                payload = {
                    "nickname": nickname,
                    "riot_id": riot_id,
                    "game_role": role,  # 👈 ЗМІНЕНО: role -> game_role
                    "discord_tag": discord_tag
                }
                
                try:
                    response = requests.post(f"{API_URL}/players/", json=payload)
                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"✅ Гравця успішно додано!")
                        st.json({"DB ID": data.get("id"), "PUUID": data.get("puuid")})
                    else:
                        st.error(f"Помилка сервера: {response.text}")
                except Exception as e:
                    st.error(f"Не вдалося з'єднатися з API: {e}")

# === БЛОК 2: ІСТОРІЯ МАТЧІВ ===
with col2:
    st.subheader("📜 Історія матчів гравця")
    
    # Використовуємо 2 як дефолтний ID (наш протестований гравець)
    player_id_input = st.number_input("Введіть внутрішній ID гравця (з БД)", min_value=1, value=2, step=1)
    
    if st.button("🔄 Отримати матчі"):
        with st.spinner("Завантаження матчів з HenrikDev API..."):
            try:
                response = requests.get(f"{API_URL}/players/{player_id_input}/matches")
                if response.status_code == 200:
                    data = response.json()
                    matches = data.get("matches", [])
                    
                    if matches:
                        st.success(f"Знайдено матчів для {data['player']['nickname']}: {len(matches)}")
                        
                        # Перетворюємо словник у таблицю
                        df = pd.DataFrame(matches)
                        
                        # 👈 ЗМІНЕНО: Виводимо всі дані "як є", щоб уникнути KeyError
                        st.dataframe(df, use_container_width=True, hide_index=True)
                    else:
                        st.warning("Матчів не знайдено.")
                else:
                    st.error(f"Помилка {response.status_code}: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"Не вдалося з'єднатися з API: {e}")

st.divider()

# === БЛОК 3: AI COACH АНАЛІТИКА ===
st.subheader("🧠 ШІ-Тренер: Глибокий аналіз матчу")

analyze_col1, analyze_col2 = st.columns([1, 2])

with analyze_col1:
    coach_player_id = st.number_input("ID гравця для аналізу", min_value=1, value=2, step=1, key="coach_pid")
    coach_match_id = st.text_input("Match ID (скопіюйте з таблиці вище)", placeholder="Наприклад: 43293168-da39-...")
    analyze_btn = st.button("🚀 Запустити AI Аналіз", type="primary")

with analyze_col2:
    if analyze_btn:
        if not coach_match_id:
            st.warning("Будь ласка, вставте Match ID.")
        else:
            with st.spinner("Тренер переглядає VOD та аналізує статистику Llama 3.1..."):
                try:
                    response = requests.get(f"{API_URL}/players/{coach_player_id}/matches/{coach_match_id}/analyze")
                    
                    if response.status_code == 200:
                        data = response.json()
                        stats = data.get("stats", {})
                        coach_feedback = data.get("coach_analysis", "Відповідь не отримана.")
                        
                        # Виводимо базову статистику за допомогою красивих метрик Streamlit
                        st.markdown("### 📊 Статистика")
                        m1, m2, m3, m4, m5 = st.columns(5)
                        m1.metric(label="Агент", value=stats.get("agent", "N/A"))
                        m2.metric(label="Карта", value=stats.get("map", "N/A"))
                        m3.metric(label="Kills", value=stats.get("kills", 0))
                        m4.metric(label="Deaths", value=stats.get("deaths", 0))
                        m5.metric(label="Assists", value=stats.get("assists", 0))
                        
                        # Виводимо статус гри (Перемога/Поразка)
                        is_win = stats.get("won")
                        if is_win:
                            st.success("🏆 Перемога")
                        else:
                            st.error("💀 Поразка")
                            
                        # Виводимо коментар ШІ у виділеному стилізованому блоці
                        st.markdown("### 🎙️ Вердикт Тренера")
                        st.info(coach_feedback, icon="🤖")
                        
                    else:
                        st.error(f"Помилка {response.status_code}: {response.json().get('detail')}")
                except Exception as e:
                    st.error(f"Не вдалося з'єднатися з API: {e}")