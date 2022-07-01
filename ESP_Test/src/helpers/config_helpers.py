import os


def get_base_url():
    env = os.environ.get('ENV', 'qa')

    if env.lower() == 'qa':
        return 'https://qaesp.azurewebsites.net/applications'
    elif env.lower() == 'prod':
        return 'https://qaesp.azurewebsites.net/applications'
    else:
        raise Exception(f"Unknown environment: {env}")
