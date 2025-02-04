from multiprocessing import Process

import ray

from merge_k_sort_stemmed import merge_all_inverted_lists, merge_all_inverted_lists_from32

if __name__ == '__main__':
    # p1 = Process(target=merge_all_inverted_lists, args=(1, 12, 100))
    # p1.start()
    #
    # p2 = Process(target=merge_all_inverted_lists, args=(13, 25, 101))
    # p2.start()
    #
    # p3 = Process(target=merge_all_inverted_lists, args=(26, 35, 102))
    # p3.start()
    #
    # p4 = Process(target=merge_all_inverted_lists, args=(36, 47, 103))
    # p4.start()
    #
    # p5 = Process(target=merge_all_inverted_lists, args=(48, 59, 104))
    # p5.start()
    #
    # p6 = Process(target=merge_all_inverted_lists, args=(60, 75, 105))
    # p6.start()
    ray.init(memory=6000*1024*1024)
    a=merge_all_inverted_lists.remote(1,12,100)
    b=merge_all_inverted_lists.remote(13, 25, 101)
    c=merge_all_inverted_lists.remote(26, 35, 102)
    d=merge_all_inverted_lists.remote(36, 47, 103)
    e=merge_all_inverted_lists.remote(48, 59, 104)
    f=merge_all_inverted_lists.remote(60, 75, 105)
    h = ray.get(f)

    # print("prefinal")
    #
    # i=merge_all_inverted_lists_from32.remote(100,102,106)
    # k=merge_all_inverted_lists_from32.remote(103,105,107)
    # ray.get(k)
    print("final")
    l=merge_all_inverted_lists_from32.remote(100, 105, 108)
    ray.get(l)


    # p3 = Process(target=create_index_batch, args=(21, 30))
    # p3.start()
    #
    # p4 = Process(target=create_index_batch, args=(31, 40))
    # p4.start()
    #
    # p5 = Process(target=create_index_batch, args=(41, 50))
    # p5.start()
    #
    # p6 = Process(target=create_index_batch, args=(51, 60))
    # p6.start()
    #
    # p7 = Process(target=create_index_batch, args=(61, 70))
    # p7.start()
    #
    # p8 = Process(target=create_index_batch, args=(71, 75))
    # p8.start()

    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()


