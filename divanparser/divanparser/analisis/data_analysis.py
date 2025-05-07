import csv
import os
import matplotlib.pyplot as plt


def analyze_data():
    prices = []
    file_path = os.path.join(os.getcwd(), 'divan_prices.csv')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['price'] and row['price'].isdigit():
                    prices.append(int(row['price']))
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    if not prices:
        print("Нет данных для анализа")
        return

    average_price = sum(prices) / len(prices)
    print(f"Средняя цена на диваны: {average_price:.2f} ₽")

    plt.figure(figsize=(12, 6))
    plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
    plt.title('Распределение цен на диваны')
    plt.xlabel('Цена (рубли)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()