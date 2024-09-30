import click
from pathlib import Path
import json

HOME = Path.home()
PWD = Path('.')

# configs dir
BASE_DIR = HOME / '.bipdev'

# configs file
CONF_FILE = BASE_DIR / 'configs.json'

# patch dir
PATCH_DIR = BASE_DIR / 'patch'

BASE_CONFIGS = { 'BIPHOME': '' }


@click.group()
def cli():
    pass


@cli.command()
def init():
    if not BASE_DIR.exists():
        BASE_DIR.mkdir()
    if not PATCH_DIR.exists():
        PATCH_DIR.mkdir()
    if not CONF_FILE.exists():
        pwd = Path('.').resolve()
        BASE_CONFIGS['BIPHOME'] = str(pwd)
        print(BASE_CONFIGS)
        CONF_FILE.write_text(json.dumps(BASE_CONFIGS))


@cli.command()
def configs():
    for k, v in load_configs().items():
        print(f'{k}: {v}')


# util
def load_configs():
    return json.loads(CONF_FILE.read_text('utf-8'))


if __name__ == '__main__':
    cli()
