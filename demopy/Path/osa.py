# coding:utf8
import datetime, time

import os, os.path
import threading


test_path = r"d:\MyStore\000 - inbox - 信息中转站\123"
# 列出一个目录里面所有的文件，不知道是否包含目录=> 是包含目录的；
# ???得到一个文件的类型的函数有没有？
files = os.listdir(test_path)
assert type(files) == list

for file in files:
    print(file)

file1 = files[2]
print(file1)

# 改变文件的名字
old_file_path = os.path.join(test_path, file1)
print(old_file_path)
new_file1_name = "SPG_2022-03-29_23-20-15.png"
new_file1_path = os.path.join(test_path, file1)
result = os.rename(old_file_path, new_file1_path)
print(result)



def print_dir_files(dir):
    """
    打印一个文件下面的所有文件的名字；不包括其路径；
    文件有属性：
        文件的名字：即文件名
        文件的路径:文件从哪里来的
        文件的完整路径
        文件的
    """

    _files = os.listdir(dir)
    for _file in _files:
        print(_file)


print_dir_files(test_path)


def get_time_string(use_time, formation = "%Y-%m-%d %H:%M:%S"):
    """
    将一个原始时间，以格式formation转化；
    如何use_time为假，则打印出现在的时间；
    两个功能：转换use_time或者转换现在时间；
    """
    if use_time:
        timetuple = time.localtime(use_time)
        time_string = time.strftime(formation, timetuple)
        pass
    else:
        # use_time 为 False
        now = datetime.datetime.now()
        time_string = now.strftime(formation)
        pass
    return time_string



def get_file_info(location):
    """
    location : 是一个文件名，而不是目录
    作用： 返回一个字典，这个字典是关于一个文件的信息，包含创建信息，修改信息
    父目录，文件名，文件的类型；
    """
    formation = os.path.getsize(location)
    create_time = os.path.getctime(location)
    modify_time = os.path.getmtime(location)
    create_time = get_time_string(create_time)
    modify_time = get_time_string(modify_time)
    parent_dir = os.path.dirname(location)
    file_name = os.path.split(location)[-1]
    file_type = os.path.splitext(location)[1].strip('.')
    result = {}
    var_list = [create_time, modify_time, parent_dir, file_name,
                file_type]
    # 打印出本局部空间里面的变量的名字以及变量的值的字典
    for k, v in locals().items():
        if v in var_list:
            result[k] = v
    return result


print(get_file_info(old_file_path))


def list_file(location: str):
    """
    location: 为一个目录
    作用：返回一个列表，列表里存放着目录下所有文件的错别字；
    并非是完整的路径，且列表排除了目录；
    """
    # 移除路径后面的双反斜杠
    location = location.strip('\\')
    file_list = os.listdir(location)
    for name in file_list[:]:
        fullname = os.path.join(location, name)
        # 如果是隐藏文件，则移除列表
        if name.startswith('.'):
            file_list.remove(name)
        # 如果是目录，则移除； isdir需要完整的路径
        if os.path.isdir(fullname):
            file_list.remove(name)
    return file_list


def count_size(location):
    """
    location: 为一个目录
    得到文件的大小信息
    """
    assert (os.path.isdir(location))
    filelist = list_file(location)
    totalsize = 0
    for name in filelist:
        filelocation = os.path.join(location, name)
        totalsize += os.path.getsize(filelocation)
    return totalsize


print("test_path目录下文件的大小的总和是：{}".format(count_size(test_path)))


# 计算一个函数的运行时间，可以作用装饰器
def clock(function):
    """
    作用：计算一个函数的运行时间，参数为一个函数的名字
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        use_time = (end_time - start_time) * 1000
        print("->elapsed time: %.2f ms" % use_time)
        return result
    return wrapper


@clock
def test_clock():
    time.sleep(3)


print(test_clock())


# 开一个新的线程并通过队列将函数的返回值同步；
def thread(resultQueue=None):
    """

    """
    def wrapper(function):
        def proWarp(*args, **kwargs):
            def process(*args, **kwargs):
                ret = function(*args, **kwargs)
                print('ret is {}'.format(ret))
                if resultQueue:
                    resultQueue.put(ret)
                return resultQueue
            thread = threading.Thread(target=process,
                                      args=args, kwargs=kwargs)
            thread.setDaemon(True)
            thread.start()
            return process
    return wrapper


# 测试上面的装饰器
@thread
def test_thread(a):
    """

    """
    print("in test_thread function~ args is :{}".format(a))
    time.sleep(a)


print("线程开启！！！测试中！！！")
test_thread(1)  # todo 有问题，好像线程函数没有运行，因为看不到print；
test_thread(2)
test_thread(3)

# assert 1 # ok
# assert (2) # ok
# assert (2, ) # ok
# assert (0)  # except
assert all([1, 1 ,2])  # ok
assert all([1, 1 ,0])  # except
assert list()  # except
