from .context import functions
import os
import pytest
import sqlite3
import time


DB_TESTING_PATH = './tests/data.db'

@pytest.mark.skip("This will reset the db, meaning you have to re-run init_test_db.py to re-load data")
def test_create_db(mocker):
    mocker.patch('sample.functions.DB_PATH', DB_TESTING_PATH)
    os.remove(DB_TESTING_PATH)
    time.sleep(3)
    functions.create_db()

    with sqlite3.connect(DB_TESTING_PATH) as db:
        cur = db.cursor()
        cur.execute("PRAGMA table_info(inventory)")
        assert cur.fetchall() == [(0, 'uuid', 'TEXT', 0, None, 0), (1, 'item_name', 'TEXT', 0, None, 0), (2, 'container', 'TEXT', 0, None, 0), (3, 'tags', 'TEXT', 0, None, 0)]

@pytest.mark.skip()
def test_get_items_in_container(mocker):
    mocker.patch('sample.functions.DB_PATH', DB_TESTING_PATH)
    items_in_container = functions.get_items_in_container("CN")
    assert items_in_container[:3] == ['dove, ring', 'great horned owl', 'macaw, red and blue']

@pytest.mark.skip()
def test_find_item_by_exact_match(mocker):
    mocker.patch('sample.functions.DB_PATH', DB_TESTING_PATH)
    results = functions.find_item("dingo")
    assert results == ('dingo', 'ua')

@pytest.mark.skip()
def test_find_items_that_match_through_search_that_needs_splitting_found_in_tags(mocker):
    mocker.patch('sample.functions.DB_PATH', DB_TESTING_PATH)
    results = functions.find_item('123-reg.co.uk')
    assert results == [('crab (unidentified)', 'ar'), ('pigeon, feral rock', 'th'), ('langur, gray', 'ph')]

@pytest.mark.skip()
def test_find_items_that_match_through_search_no_splitting_found_in_item_name(mocker):
    mocker.patch('sample.functions.DB_PATH', DB_TESTING_PATH)
    results = functions.find_item('grey')
    assert results == [('greylag goose', 'pe'), ('grey fox', 'th'), ('lemur, grey mouse', 'cn')]

@pytest.mark.skip()
def test_find_items_that_match_through_search_needs_splitting_second_partial_name(mocker):
    mocker.patch('sample.functions.DB_PATH', DB_TESTING_PATH)
    results = functions.find_item('doesntexist-reg.co.uk')
    assert results == [('crab (unidentified)', 'ar'), ('langur, gray', 'ph'), ('heron, green-backed', 'ws')]