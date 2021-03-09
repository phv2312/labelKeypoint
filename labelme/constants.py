

class_position = { # x,y coordinates
    'rarm': (.37, .45),
    'body': (.47, .45),
    'larm': (.57, .45),
    'relbow': (.32, .55),
    'lelbow': (.62, .55),
    'rleg': (.42, .6),
    'lleg': (.52, .6),
    'rwrist': (.27, .65),
    'lwrist': (.67, .65),
    'rknee': (.42, .7),
    'lknee': (.52, .7),
    'rankle': (.42, .8),
    'lankle': (.52, .8),

    # head
    'chin': (.47, .35),
    'mouth': (.47, .27),
    'nose': (.47, .19),
    'reye': (.39, .15),
    'leye': (.55, .15)
}

class_names = list(class_position.keys())
class_pairs = [
    ('reye', 'nose'), ('leye', 'nose'), ('nose', 'mouth'), ('mouth', 'chin'),
    ('chin', 'body'),
    ('body', 'larm'), ('body', 'rarm'), ('larm', 'lelbow'), ('rarm', 'relbow'), ('lelbow', 'lwrist'), ('relbow', 'rwrist'),
    ('body', 'lleg'), ('body', 'rleg'), ('lleg', 'lknee'), ('rleg', 'rknee'), ('lknee', 'lankle'), ('rknee', 'rankle')
]