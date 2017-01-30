import yaml
from clone_data import DATA_DIR


CURRENT_LEGISLATORS = 'legislators-current.yaml'
LEGISLATORS_SOCIAL = 'legislators-social-media.yaml'


def _get_path_to_file(filename):
    if not DATA_DIR.endswith('/'):
        path = DATA_DIR + '/'
    else:
        path = DATA_DIR
    return '%s%s' % (path, filename)


def get_information():
    officials = {}
    with file(_get_path_to_file(CURRENT_LEGISLATORS), 'r') as f:
        for official in yaml.load(f.read()):
            current_term = official.get('terms', [])[-1]
            officials[official.get('id', {}).get('govtrack')] = {
                'name': official.get('name', {}).get('official_full'),
                'party': current_term.get('party'),
                'job': current_term.get('type')
            }

    with file(_get_path_to_file(LEGISLATORS_SOCIAL), 'r') as f:
        for official in yaml.load(f.read()):
            govtrack_id = official.get('id', {}).get('govtrack')
            if govtrack_id in officials:
                officials[govtrack_id]['twitter'] = \
                    official.get('social', {}).get('twitter')

    return officials

