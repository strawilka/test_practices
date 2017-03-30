# test finding path in tree
import tree

def test_find():
    # assert tree.file_search(['C:', 'backup.log', 'ideas.txt'], 'C:/ideas.txt') == True
    res = tree.file_search(['/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], '/home/user2/desktop/new folder/hereiam.py')
    assert res == True


def test_not_find():
    res = tree.file_search(['/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', 'hereiam.py' ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], '/home/user2/desktop/new folder/hereiam.py')
    assert res == False
