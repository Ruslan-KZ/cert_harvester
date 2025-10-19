# cert_harvester
cert_harvester is an automation bot that enrolls in online courses, completes quizzes, and collects verified certificates — no manual input required.


напиши пример кода для трехслойной архитектуры приложения
на фастапи чтобы был слой представления как router.py где будут веб методы обрабатываться
слой бизнес логики и слой доступа к данным

я юзаю pydantic, sqlalchemy

для селениума моего парсера тоже нужен вид архитектуры приложения
чтобы так же была бизнес логика и слой доступа к данным



PS D:\Рабочий стол\all\cert_harvester> Get-ChildItem -Recurse -Name | Where-Object {$_ -notmatch 'venv'}
alembic
app
core
database
model
parser
static_files
templates
__pycache__
.env
.gitignore
alembic.ini
LICENSE
main.py
README.md
requirements.txt
run.py
alembic\versions
alembic\__pycache__
alembic\env.py
alembic\README
alembic\script.py.mako
alembic\versions\__pycache__
alembic\versions\d0095a71bd91_add_new_models.py
alembic\versions\__pycache__\d0095a71bd91_add_new_models.cpython-313.pyc
alembic\__pycache__\env.cpython-313.pyc
app\api
app\__pycache__
app\router.py
app\api\frontend
app\api\user
app\api\frontend\commands
app\api\frontend\schemas
app\api\frontend\__pycache__
app\api\frontend\front_api.py
app\api\frontend\commands\__pycache__
app\api\frontend\commands\front_crud.py
app\api\frontend\commands\__pycache__\bot.cpython-313.pyc
app\api\frontend\commands\__pycache__\bot_crud.cpython-313.pyc
app\api\frontend\schemas\__pycache__
app\api\frontend\schemas\create.py
app\api\frontend\schemas\response.py
app\api\frontend\schemas\__pycache__\course.cpython-313.pyc
app\api\frontend\schemas\__pycache__\create.cpython-313.pyc
app\api\frontend\schemas\__pycache__\response.cpython-313.pyc
app\api\frontend\__pycache__\frontend.cpython-313.pyc
app\api\frontend\__pycache__\front_api.cpython-313.pyc
app\api\user\commands
app\api\user\schemas
app\api\user\__pycache__
app\api\user\user_api.py
app\api\user\commands\__pycache__
app\api\user\commands\user_crud.py
app\api\user\commands\__pycache__\user_crud.cpython-313.pyc
app\api\user\schemas\__pycache__
app\api\user\schemas\create.py
app\api\user\schemas\respons.py
app\api\user\schemas\__pycache__\create.cpython-313.pyc
app\api\user\schemas\__pycache__\respons.cpython-313.pyc
app\api\user\__pycache__\user_api.cpython-313.pyc
app\__pycache__\auth.cpython-313.pyc
app\__pycache__\router.cpython-313.pyc
core\__pycache__
core\config.py
core\config_path.py
core\__pycache__\config.cpython-313.pyc
core\__pycache__\config_path.cpython-313.pyc
database\__pycache__
database\db.py
database\__pycache__\db.cpython-313.pyc
model\__pycache__
model\models.py
model\__pycache__\models.cpython-313.pyc
parser\parser_app.py
static_files\css
static_files\css\style.css
templates\index.html
__pycache__\main.cpython-313.pyc
__pycache__\run.cpython-313.pyc
PS D:\Рабочий стол\all\cert_harvester>