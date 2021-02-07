from test_serv import locators
from test_serv import some_func


def test_add_user_1():
    name = 'test_name 1'
    surname = 'test surname 2'
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    assert response_add_user, f'Response is: "{response_add_user}"'


def test_add_user_2():
    name = 'test_name 2'
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}')
    assert response_add_user == '2 required parameters are expected: name and surname', \
        f'Response is: "{response_add_user}"'


def test_add_user_3():
    surname = 'test_name 3'
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}surname={surname}')
    assert response_add_user == '2 required parameters are expected: name and surname', \
        f'Response is: "{response_add_user}"'


def test_add_user_4():
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}')
    assert response_add_user == '2 required parameters are expected: name and surname', \
        f'Response is: "{response_add_user}"'


def test_add_user_5():
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
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    assert response_add_user, f'Response is: "{response_add_user}"'


def test_add_user_6():
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
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    assert response_add_user, f'Response is: "{response_add_user}"'


def test_add_user_7():
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
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    assert response_add_user, f'Response is: "{response_add_user}"'


def test_add_user_8(locked_file):
    name = 'test name 8'
    surname = 'test surname 8'
    response_add_user = some_func.give_me_json(f'{locators.links.ADD_USER}name={name}&surname={surname}')
    assert response_add_user, f'Response is: "{response_add_user}"'


if __name__ == "__main__":
    pass