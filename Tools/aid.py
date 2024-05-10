import os
import time


def create_folder(folder_name: str) -> bool:
    base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    folder_path = os.path.join(base_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_name)
    return True


def info_file_save(info, dataset_path: str) -> bool:
    create_folder(folder_name=dataset_path)
    base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # stat_file = 'information-' + time.strftime('%m%d-%H%M%S', time.localtime()) + "-" + str(time.time()) + '.txt'
    stat_file = 'info(ans)-' + time.strftime('%m%d-%H%M%S', time.localtime()) + "-" + str(time.time()) + '.txt'
    result_stat_file = open(os.path.join(base_path, dataset_path, stat_file), 'w')
    result_stat_file.write(info.get_RICS_result())
    result_stat_file.close()
    print(info.output_info_file_name, "saved successfully!")
    return True
