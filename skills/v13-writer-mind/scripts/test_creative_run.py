import json, subprocess, sys, tempfile
from pathlib import Path

SRC = Path(__file__).parent / 'creative_run.py'

def run(*a, ok=True):
    x = subprocess.run([sys.executable, str(SRC), *map(str, a)], capture_output=True, text=True)
    if ok:
        assert x.returncode == 0, (x.stdout, x.stderr)
    else:
        assert x.returncode != 0, (x.stdout, x.stderr)
    return x.stdout + x.stderr

def test_roundtrip():
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        root = t / 'r'
        lock = t / 'l.md'
        lock.write_text('1639, same facts, no canon.', encoding='utf8')
        a = t / 'a.md'
        a.write_text('一' * 610 + '\n他拒绝了。\n', encoding='utf8')
        b = t / 'b.md'
        b.write_text('二' * 610 + '\n她先把信递了出去。\n', encoding='utf8')
        review = t / 'r.json'
        review.write_text(json.dumps({'observations':[{
            'line': 2, 'quote': '他拒绝了', 'reader_cost': '无因果', 'repair': '给动作以具体理由'
        }]}, ensure_ascii=False), encoding='utf8')
        run('init', '--root', root, '--case', 'test', '--lock', lock)
        run('draft', '--root', root, '--case', 'test', '--file', a, '--hypothesis', 'first')
        run('draft', '--root', root, '--case', 'test', '--file', b, '--hypothesis', 'second', ok=False)
        run('review', '--root', root, '--case', 'test', '--version', 'V001', '--file', review)
        run('draft', '--root', root, '--case', 'test', '--file', b, '--hypothesis', 'second')
        status = run('status', '--root', root, '--case', 'test')
        assert 'drafts 2 reviews 1 CANON_UNTOUCHED' in status
        manifest = json.loads((root/'test'/'run.json').read_text('utf8'))
        assert manifest['drafts'][1]['parent'] == 'V001'
        (root/'test'/'drafts'/'V001.md').write_text('tampered', encoding='utf8')
        run('status', '--root', root, '--case', 'test', ok=False)

if __name__ == '__main__':
    test_roundtrip()
    print('PASS: draft, review gate, revision, parent link, tamper detection')
