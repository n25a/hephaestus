import os


def make_folders(project_name: str):
    """
    Make folders for project

    :param: project_name: project name in string type
    """

    if not os.path.exists(project_name):
        raise Exception('Project folder is exist. Please try again with another name.')
    os.makedirs(project_name)
