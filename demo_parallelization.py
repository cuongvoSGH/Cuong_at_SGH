from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Pool
from pathlib import Path

from knotprot_download import get_proteins, download_link, setup_download_dir, time_it, create_thumbnail


def run_seq(my_dir):
    i = 0
    prot_list = get_proteins()
    for p in prot_list:
        i += 1
        download_link(my_dir, p)
    print(f'structures downloaded: {i}')


def run_multiprocesssing(my_dir):
    prot_list = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(12) as pool:
        pool.map(download, prot_list)

def thumbnails_seq():
    for image_path in Path('images').iterdir():
        print(image_path)
        create_thumbnail((256, 256), image_path)


def thumbnails_parallel():
    image_list = Path('images').iterdir()
    create_thumb = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(create_thumb, image_list)

if __name__ == '__main__':
    setup_download_dir()
    #time_it(run_seq, 'images')
    time_it(run_multiprocesssing, 'images')
    #time_it(thumbnails_seq)
    time_it(thumbnails_parallel)