from test_serv import locators
from test_serv import some_func
import csv


def test_add_user_positive(get_last_user):
    name = 'test name 1'
    surname = 'test surname 2'
    response_successfully_added = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')

    response = get_last_user
    assert response_successfully_added[1] == 200 and response[0] == name and response[1] == surname, \
        f'Response is: "{response_successfully_added}"'


def test_add_user_missing_surname():
    name = 'test_name 2'
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}')
    assert response_add_user[0] == '2 required parameters are expected: name and surname', \
        f'Response is: "{response_add_user}"'


def test_add_user_missing_name():
    surname = 'test_name 3'
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}surname={surname}')
    assert response_add_user[0] == '2 required parameters are expected: name and surname', \
        f'Response is: "{response_add_user}"'


def test_add_user_missing_name_surname():
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}')
    assert response_add_user[0] == '2 required parameters are expected: name and surname', \
        f'Response is: "{response_add_user}"'


def test_add_user_long_name(get_last_user):
    name = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam auctor nulla sed sem bibendum
    dictum. Sed viverra ante nulla, quis tincidunt urna sagittis ut. Cras mollis vel est et ultrices. 
    Praesent id nisl a erat dapibus interdum. Curabitur tempor est ac lorem finibus, eget vulputate augue 
    mollis. Donec ante quam, ornare ut mattis placerat, venenatis ac odio. Aenean posuere tellus vitae leo 
    malesuada molestie. Proin feugiat nunc sit amet mollis auctor. Donec tempor faucibus mattis. Morbi 
    mollis dui tempus, facilisis nisl et, ullamcorper ex. Vivamus a lectus et turpis faucibus volutpat. 
    Aliquam gravida dui nec accumsan rhoncus. Fusce interdum congue diam eget congue. In hac habitasse 
    platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam risus mauris, 
    aliquam a risus quis, laoreet tincidunt quam. Quisque a faucibus nunc. Sed lobortis malesuada tellus. 
    Nullam facilisis lectus vitae nisi consectetur, vitae efficitur dui gravida. Maecenas interdum mi non 
    sapien lobortis pharetra. Etiam pulvinar arcu enim, sed interdum diam suscipit vitae. Maecenas laoreet
    id mi non sodales. Quisque iaculis nibh eget fringilla pharetra. Sed semper auctor dui vel consequat. 
    In euismod libero nec nisl dignissim, at feugiat elit vestibulum. Morbi luctus placerat turpis at 
    viverra. Aenean tempor nunc eget mi convallis, eget ultrices erat cursus. Quisque id turpis tortor. 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi efficitur eros id ipsum semper sagittis.
    Pellentesque id placerat mi. Vestibulum eget vehicula tellus. Curabitur eu scelerisque libero, et 
    finibus arcu. Nullam consectetur leo vitae tortor interdum, ac porttitor urna semper. Nunc vel semper 
    lacus. In a. '''
    surname = 'test surname'
    response_successfully_added = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    response = get_last_user
    assert response_successfully_added[1] == 200 and response[0] == name and response[1] == surname, \
        f'Response is: "{response_successfully_added}"'


def test_add_user_6(get_last_user):
    name = 'test name'
    surname = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam auctor nulla sed sem bibendum
    dictum. Sed viverra ante nulla, quis tincidunt urna sagittis ut. Cras mollis vel est et ultrices. 
    Praesent id nisl a erat dapibus interdum. Curabitur tempor est ac lorem finibus, eget vulputate augue 
    mollis. Donec ante quam, ornare ut mattis placerat, venenatis ac odio. Aenean posuere tellus vitae leo 
    malesuada molestie. Proin feugiat nunc sit amet mollis auctor. Donec tempor faucibus mattis. Morbi 
    mollis dui tempus, facilisis nisl et, ullamcorper ex. Vivamus a lectus et turpis faucibus volutpat. 
    Aliquam gravida dui nec accumsan rhoncus. Fusce interdum congue diam eget congue. In hac habitasse 
    platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam risus mauris, 
    aliquam a risus quis, laoreet tincidunt quam. Quisque a faucibus nunc. Sed lobortis malesuada tellus. 
    Nullam facilisis lectus vitae nisi consectetur, vitae efficitur dui gravida. Maecenas interdum mi non 
    sapien lobortis pharetra. Etiam pulvinar arcu enim, sed interdum diam suscipit vitae. Maecenas laoreet
    id mi non sodales. Quisque iaculis nibh eget fringilla pharetra. Sed semper auctor dui vel consequat. 
    In euismod libero nec nisl dignissim, at feugiat elit vestibulum. Morbi luctus placerat turpis at 
    viverra. Aenean tempor nunc eget mi convallis, eget ultrices erat cursus. Quisque id turpis tortor. 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi efficitur eros id ipsum semper sagittis.
    Pellentesque id placerat mi. Vestibulum eget vehicula tellus. Curabitur eu scelerisque libero, et 
    finibus arcu. Nullam consectetur leo vitae tortor interdum, ac porttitor urna semper. Nunc vel semper 
    lacus. In a. '''
    response_successfully_added = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    response = get_last_user
    assert response_successfully_added[1] == 200 and response[0] == name and response[1] == surname, \
        f'Response is: "{response_successfully_added}"'


def test_add_user_7(get_last_user):
    name = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam auctor nulla sed sem bibendum
    dictum. Sed viverra ante nulla, quis tincidunt urna sagittis ut. Cras mollis vel est et ultrices. 
    Praesent id nisl a erat dapibus interdum. Curabitur tempor est ac lorem finibus, eget vulputate augue 
    mollis. Donec ante quam, ornare ut mattis placerat, venenatis ac odio. Aenean posuere tellus vitae leo 
    malesuada molestie. Proin feugiat nunc sit amet mollis auctor. Donec tempor faucibus mattis. Morbi 
    mollis dui tempus, facilisis nisl et, ullamcorper ex. Vivamus a lectus et turpis faucibus volutpat. 
    Aliquam gravida dui nec accumsan rhoncus. Fusce interdum congue diam eget congue. In hac habitasse 
    platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam risus mauris, 
    aliquam a risus quis, laoreet tincidunt quam. Quisque a faucibus nunc. Sed lobortis malesuada tellus. 
    Nullam facilisis lectus vitae nisi consectetur, vitae efficitur dui gravida. Maecenas interdum mi non 
    sapien lobortis pharetra. Etiam pulvinar arcu enim, sed interdum diam suscipit vitae. Maecenas laoreet
    id mi non sodales. Quisque iaculis nibh eget fringilla pharetra. Sed semper auctor dui vel consequat. 
    In euismod libero nec nisl dignissim, at feugiat elit vestibulum. Morbi luctus placerat turpis at 
    viverra. Aenean tempor nunc eget mi convallis, eget ultrices erat cursus. Quisque id turpis tortor. 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi efficitur eros id ipsum semper sagittis.
    Pellentesque id placerat mi. Vestibulum eget vehicula tellus. Curabitur eu scelerisque libero, et 
    finibus arcu. Nullam consectetur leo vitae tortor interdum, ac porttitor urna semper. Nunc vel semper 
    lacus. In a. '''
    surname = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam auctor nulla sed sem bibendum
    dictum. Sed viverra ante nulla, quis tincidunt urna sagittis ut. Cras mollis vel est et ultrices. 
    Praesent id nisl a erat dapibus interdum. Curabitur tempor est ac lorem finibus, eget vulputate augue 
    mollis. Donec ante quam, ornare ut mattis placerat, venenatis ac odio. Aenean posuere tellus vitae leo 
    malesuada molestie. Proin feugiat nunc sit amet mollis auctor. Donec tempor faucibus mattis. Morbi 
    mollis dui tempus, facilisis nisl et, ullamcorper ex. Vivamus a lectus et turpis faucibus volutpat. 
    Aliquam gravida dui nec accumsan rhoncus. Fusce interdum congue diam eget congue. In hac habitasse 
    platea dictumst. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam risus mauris, 
    aliquam a risus quis, laoreet tincidunt quam. Quisque a faucibus nunc. Sed lobortis malesuada tellus. 
    Nullam facilisis lectus vitae nisi consectetur, vitae efficitur dui gravida. Maecenas interdum mi non 
    sapien lobortis pharetra. Etiam pulvinar arcu enim, sed interdum diam suscipit vitae. Maecenas laoreet
    id mi non sodales. Quisque iaculis nibh eget fringilla pharetra. Sed semper auctor dui vel consequat. 
    In euismod libero nec nisl dignissim, at feugiat elit vestibulum. Morbi luctus placerat turpis at 
    viverra. Aenean tempor nunc eget mi convallis, eget ultrices erat cursus. Quisque id turpis tortor. 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi efficitur eros id ipsum semper sagittis.
    Pellentesque id placerat mi. Vestibulum eget vehicula tellus. Curabitur eu scelerisque libero, et 
    finibus arcu. Nullam consectetur leo vitae tortor interdum, ac porttitor urna semper. Nunc vel semper 
    lacus. In a. '''
    response_successfully_added = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    response = get_last_user
    assert response_successfully_added[1] == 200 and response[0] == name and response[1] == surname, \
        f'Response is: "{response_successfully_added}"'


def test_add_user_8(locked_file, get_last_user):
    name = 'test name 8'
    surname = 'test surname 8'
    response_successfully_added = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    response = get_last_user
    assert response_successfully_added[1] == 200 and response[0] == name and response[1] == surname, \
        f'Response is: "{response_successfully_added}"'


if __name__ == "__main__":
    pass