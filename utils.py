def wait_and_type(page, selector, text):
    element = page.wait_for_selector(selector)
    element.type(text)

