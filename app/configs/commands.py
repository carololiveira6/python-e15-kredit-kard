from flask import Flask
from random import randint

from flask.cli import AppGroup
from click import echo, argument

from app.models import UsersModel, CreditCardsModel

from faker import Faker

fake = Faker()


def cli_user(app: Flask):

    cli_user_group = AppGroup("user")
    session = app.db.session

    @cli_user_group.command("create")
    @argument("quantity")
    def create_user_cli(quantity: int) -> None:
        for _ in range(int(quantity)):
            user = fake.name()
            password_fake = fake.password(length=15)
            is_admin = False
            response = UsersModel(login=user, password=password_fake, is_admin=is_admin)

            session.add(response)
            session.commit()

    app.cli.add_command(cli_user_group)  


    cli_admin_group = AppGroup("admin")
    @cli_admin_group.command("create")
    def create_admin():

        user = fake.name()
        password_fake = fake.password(length=10)
        is_admin = True
        response = UsersModel(login=user, password=password_fake, is_admin=is_admin)

        echo("Admin criado")
        echo(f"Login:{user}") 
        echo(f"password:{password_fake}")

        session.add(response)
        session.commit()

    app.cli.add_command(cli_admin_group)


    cli_card_group = AppGroup("users_credit_cards")
    @cli_card_group.command("create")
    @argument("quantity")
    def users_credit_cards(quantity: int):

        for _ in range(int(quantity)):

            user = fake.name()
            password_fake = fake.password(length=15)
            is_admin = False
            
            user_card = UsersModel(login=user, password=password_fake, is_admin=is_admin)

            session.add(user_card)
            session.commit()

            for _ in range(randint(0, 2)):

                expire_date = fake.credit_card_expire()
                number = fake.credit_card_number()
                provider = fake.credit_card_provider()
                security_code = fake.credit_card_security_code()[:3]  
                user_id = user_card.id   
                
                card = CreditCardsModel(expire_date=expire_date, number=number, provider=provider, security_code=security_code, user_id=user_id)

                session.add(card)
                session.commit()

    app.cli.add_command(cli_card_group)


def init_app(app: Flask):
    cli_user(app)