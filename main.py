from clone_data import clone
from social import get_information


def main():
    clone()
    data = get_information()
    for legislator_id, legislator in data.iteritems():
        print legislator


if __name__ == '__main__':
    main()
