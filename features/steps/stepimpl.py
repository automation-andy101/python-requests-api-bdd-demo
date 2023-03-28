import requests
from behave import *
from payload.payLoad import addBookPayload
from utilities.configurations import *
from utilities.resources import *


@given('I have a book payload')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookPayload('99921-58-10-7', '999')


@when('I send a POST request containing the book payload to the add book endpoint')
def step_impl(context):
    context.addBook_response = requests.post(context.url, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    print(type(response_json))
    bookId = response_json['ID']
    print(bookId)
    assert context.addBook_response.status_code == 200
    assert response_json['Msg'] == 'successfully added'
