import time

def start_bot(email: str, password: str, links: list):
    
    for link in links:
        print(f"Обрабатываем {link} для {email}")
        time.sleep(1)
    return {"status": "Бот завершил работу"}
