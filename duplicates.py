from PIL import Image


def image_comparator(path_1, path_2):
    """ Compares two images. Two images are identical if they have same size and they are binary identical.
    :param path_1: Path to first image.
    :param path_2: Path to second image.
    :return: 1 if images are identical 0 otherwise.
    """
    first_image = Image.open(path_1)
    second_image = Image.open(path_2)
    if first_image.size == second_image.size:
        return 1 if list(first_image.getdata()) == list(second_image.getdata()) else 0
    else:
        return 0
