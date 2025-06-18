from src.database.db import TransactionalDB


def create_db():
    db: TransactionalDB = TransactionalDB()
    return db


def test_create_db():
    db = create_db()
    res = db.get("A")
    assert res == "NULL"


def test_full_workflow():
    db = create_db()

    # SET/GET
    db.set("A", "10")
    assert db.get("A") == "10"

    # UNSET
    db.unset("A")
    assert db.get("A") == "NULL"

    # COUNTS
    db.set("A", "10")
    db.set("B", "10")
    assert db.count("10") == 2

    # FIND
    assert sorted(db.find("10")) == ["A", "B"]


def test_transactions():
    db = create_db()
    db.set("A", "1")

    db.begin()
    db.set("A", "2")
    assert db.get("A") == "2"

    db.rollback()
    assert db.get("A") == "1"

    db.begin()
    db.set("A", "3")
    db.commit()
    assert db.get("A") == "3"
