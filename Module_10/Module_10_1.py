import time
import threading
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(1, word_count + 1):
            text_str = f'Какое-то слово № {i}\n'
            file.write(text_str)
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")



first_start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
first_end_time = time.time()
print(f'Работа потоков {first_end_time - first_start_time}')

second_start_time = time.time()
#args_1 = {'word_count': 10, 'file_name':'example5.txt'}
first_thread = threading.Thread(target=write_words, kwargs=({'word_count': 10, 'file_name': 'example5.txt'}))
second_thread = threading.Thread(target=write_words, kwargs=({'word_count': 30, 'file_name': 'example6.txt'}))
third_thread = threading.Thread(target=write_words, kwargs=({'word_count': 200, 'file_name': 'example7.txt'}))
fourth_thread = threading.Thread(target=write_words, kwargs=({'word_count': 100, 'file_name': 'example8.txt'}))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

second_stop_time = time.time()

print(f'Работа потоков {second_stop_time - second_start_time}')
