import datetime

import pytest
import pytz

from chess.models import ChessPlayer, ChessMatch, User


@pytest.fixture
def chess_match(db, chess_player, other_chess_player):
    return ChessMatch.objects.create(
        start_datetime=datetime.datetime(year=1990, month=10, day=20, tzinfo=pytz.UTC),
        white_player=chess_player,
        black_player=other_chess_player
    )


@pytest.fixture
def other_chess_match(db, chess_player, other_chess_player):
    return ChessMatch.objects.create(
        start_datetime=datetime.datetime(year=1990, month=10, day=20, tzinfo=pytz.UTC),
        white_player=chess_player,
        black_player=other_chess_player
    )


@pytest.fixture
def chess_player(db):
    return ChessPlayer.objects.create(
        email='test-player@mailinator.com',
        birth_date=datetime.date(year=1990, month=10, day=20),
        pesel='123456789',
        first_name='John',
        rodo_accepted=True
    )


@pytest.fixture
def other_chess_player(db):
    return ChessPlayer.objects.create(
        email='test-player@mailinator.com',
        birth_date=datetime.date(year=1990, month=10, day=20),
        pesel='123456789',
        first_name='Marry',
        rodo_accepted=True
    )


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='test-user',
        email='test-user@mailinator.com',
        first_name='Test-User',
        password='test-password'
    )
