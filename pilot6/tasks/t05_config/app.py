import json
from pathlib import Path

def load_config(config_path):
    config_path = Path(config_path)
    config = json.loads(config_path.read_text(encoding='utf-8'))
    template = Path(config['template_file'])
    config['template_text'] = template.read_text(encoding='utf-8')
    return config
