# file_search(['C:', 'backup.log', 'ideas.txt'], 'C:/ideas.txt')
# file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
# file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')

def file_search( dir_list, file_path, current_path=None):
    current_path = '' if current_path is None else current_path
    current_path += dir_list[0] + '/'
    if len(dir_list) <= 1:
        return False
    for i in range(1, len(dir_list)):
        if isinstance(dir_list[i], list):
            res = file_search(dir_list[i], file_path, current_path)
            if res:
                return res
        elif isinstance(dir_list[i], str):
            if (current_path + dir_list[i]) == file_path:
                return True
    return False

# print file_search(['C:', 'backup.log', 'ideas.txt'], 'C:/ideas.txt')
# print file_search(['/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], '/home/user2/desktop/new folder/hereiam.py')
# print file_search(['/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', 'hereiam.py' ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], '/home/user2/desktop/new folder/hereiam.py')
