from dataclasses import dataclass
from pathlib import Path

from environs import Env


@dataclass
class Api:
    webhook_host: str
    webhook_path: str
    webapp_host: str
    webapp_port: int


@dataclass
class Db:
    host: str
    port_target: int
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list
    use_redis: bool
    skip_updates: bool
    anti_flood_rate_limit: float
    root_path: Path


@dataclass
class Config:
    tg_bot: TgBot
    db: Db
    api: Api


def load_config():
    print(Path.cwd())

    env = Env()
    env.read_env(".env")

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
            skip_updates=env.bool("SKIP_UPDATES"),
            anti_flood_rate_limit=env.float("ANTI_FLOOD_RATE_LIMIT"),
            root_path=Path.cwd(),
        ),
        db=Db(
            host=env.str("DB_HOST"),
            port_target=env.int("DB_PORT_TARGET"),
            password=env.str("DB_PASSWORD"),
            user=env.str("DB_USER"),
            database=env.str("DB_NAME"),

        ),
        api=Api(
            webhook_host=env.str("WEBHOOK_HOST"),
            webhook_path=f'/bot-api',
            webapp_host=env.str("WEBAPP_HOST"),
            webapp_port=env.int("WEBAPP_PORT"),
        )
    )
