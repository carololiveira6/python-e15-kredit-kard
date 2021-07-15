from flask import Flask
from flask.cli import AppGroup
from click import echo, argument
from sqlalchemy.sql.functions import user

from app.models import UsersModel, CreditCardsModel

def cli_user(app: Flask):
    cli_user_group = AppGroup("user")
    session = app.db.session


    @cli_user_group.command("create")
    @argument("login")
    @argument("is_admin")
    @argument("password")
    def create(login, password):
        password_to_hash = password

        user = UsersModel(login=login, password=password, is_admin=False)

        user.password = password_to_hash

        session.add(user)
        session.commit()
        echo(
            f"User created, Login: {user.login}, Password Hash: {user.password_hash}, Is Admin: {user.is_admin}"
            )

    @cli_user_group.command("print")
    def to_print():
        users = UsersModel.query.all()
        [
            echo(
                f"Login: {user.login}, Password Hash: {user.password_hash}, Is Admin: {user.is_admin}"
                ) for user in users
        ]


    app.cli.add_command(cli_user_group) 

def cli_cards(app: Flask):
    cli_cards_group = AppGroup("users_credit_cards")
    session = app.db.session

    @cli_cards_group.command("create")
    @argument("expire_date")
    @argument("provider")
    @argument("security_code")
    @argument("user_id")
    def create(expire_date, provider, security_code, user_id):

        card = CreditCardsModel(expire_date=expire_date, provider=provider, security_code=security_code, user_id=user_id)

        session.add(card)
        session.commit()
        echo(
            f"Users Credit Cards, Expire Date: {card.expire_date}, Provider: {card.provider}, Security Code: {card.security_code}, User: {card.user_id}"
            )

    @cli_cards_group.command("print")
    def to_print():
        cards = CreditCardsModel.query.all()
        [
            echo(
                f"Users Credit Cards, Expire Date: {card.expire_date}, Provider: {card.provider}, Security Code: {card.security_code}, User: {card.user_id}"
                ) for card in cards
        ]


    app.cli.add_command(cli_cards_group)

def init_app(app: Flask):
    cli_user(app)
    cli_cards(app)