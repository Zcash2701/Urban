from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline() != '':
            all_data.append(file.readline())


if __name__ == '__main__':
    data_list = [f'file {number}.txt' for number in range(1, 5)]
    time_start = time.time()
    list(map(read_info, data_list))
    time_end = time.time()
    print(f'1 Затрачено времени  {time_end - time_start}')

    with Pool(processes=4) as pool:
        data_list = (f'./file {number}.txt' for number in range(1, 5))
        time_start = time.time()
        result = pool.map(read_info, data_list)
        time_end = time.time()
        print(f'2 Затрачено времени  {time_end - time_start}')


