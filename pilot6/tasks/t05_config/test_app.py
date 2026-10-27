import json
from pathlib import Path
import pytest
from app import load_config

@pytest.fixture
def configured_app(tmp_path, monkeypatch):
    project=tmp_path/'project'
    project.mkdir()
    (project/'templates').mkdir()
    (project/'templates'/'welcome.txt').write_text('Welcome!',encoding='utf-8')
    config_path=project/'config.json'
    config_path.write_text(json.dumps({'template_file':'templates/welcome.txt','name':'demo'}),encoding='utf-8')
    elsewhere=tmp_path/'elsewhere'
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)
    return load_config(config_path)

def test_template_loaded(configured_app):
    assert configured_app['template_text'] == 'Welcome!'

def test_fields_preserved(configured_app):
    assert configured_app['name'] == 'demo'
    assert configured_app['template_file'] == 'templates/welcome.txt'

def test_absolute_template(tmp_path):
    template=tmp_path/'welcome.txt'
    template.write_text('Hi',encoding='utf-8')
    config=tmp_path/'config.json'
    config.write_text(json.dumps({'template_file':str(template)}),encoding='utf-8')
    before=Path.cwd()
    assert load_config(config)['template_text'] == 'Hi'
    assert Path.cwd() == before

def test_relative_config_path(tmp_path,monkeypatch):
    (tmp_path/'sub').mkdir()
    (tmp_path/'sub'/'message.txt').write_text('Hello',encoding='utf-8')
    (tmp_path/'sub'/'config.json').write_text(json.dumps({'template_file':'message.txt'}),encoding='utf-8')
    monkeypatch.chdir(tmp_path)
    assert load_config('sub/config.json')['template_text'] == 'Hello'
    assert Path.cwd() == tmp_path
