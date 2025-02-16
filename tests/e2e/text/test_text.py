import re

from playwright.sync_api import Page, expect


def test_read_text(page: Page):
  page.goto('http://localhost:5173/')

  button = page.get_by_test_id('read-text-button')
  button.click()

  server_response = page.get_by_test_id('server-response')
  expect(server_response).to_have_text(re.compile(r'^Text from server'))

  # Pause execution to allow us to inspect
  # page.pause()


def test_write_text(page: Page):
  page.goto('http://localhost:5173/')

  sample_input = 'Hello, world!'
  expected_server_response = f'Wrote: {sample_input}'

  input_field = page.get_by_test_id('write-text-input')
  input_field.fill(sample_input)

  button = page.get_by_test_id('write-text-button')
  button.click()

  server_response = page.get_by_test_id('server-response')
  expect(server_response).to_have_text(expected_server_response)

  # Pause execution to allow us to inspect
  # page.pause()
