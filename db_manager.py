import sys
from app.models import db
_help = 'help      帮助\n' \
        'init      初始化数据库\n' \
        'migrate   同步数据库\n' \
        ''

if len(sys.argv) > 1:
    t = sys.argv[1]
    if t == 'init':
        db.create_all()
    if t == 'help':
        print(_help)
    if t == 'migrate':
        print('--------------')


else:
    print(_help)

