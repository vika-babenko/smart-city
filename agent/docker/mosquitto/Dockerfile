# Базовий образ – офіційний eclipse-mosquitto
FROM eclipse-mosquitto:latest

# (Опційно) Копіюємо власний mosquitto.conf (щоб дозволити зовнішні підключення)
COPY config/mosquitto.conf /mosquitto/config/mosquitto.conf

# Відкриваємо порти
EXPOSE 1883
EXPOSE 9001

# Запускаємо mosquitto
# (Зазвичай ENTRYPOINT/CMD у базовому образі вже прописані,
# тож можна нічого не вказувати, якщо eclipse-mosquitto робить усе автоматично)
