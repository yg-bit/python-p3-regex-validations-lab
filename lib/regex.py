import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# These patterns aim to satisfy the provided tests (not a fully general validator).

# Name rules (from tests):
# - Each name part must start with an uppercase letter
# - Following letters are lowercase only (no digits)
# - Parts may include a single apostrophe or hyphen followed by an uppercase letter
# - Parts separated by a single space only
name = r"^[A-Z][a-z]*(?:[\'-][A-Z][a-z]*)?(?: [A-Z][a-z]*(?:[\'-][A-Z][a-z]*)?)*$"
name_regex = re.compile(name)

# Phone number: allow 10 digits, or 3-3-4 with dashes, or (3) 3-4 with space
phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# Email address: from tests
# - must start with a letter
# - allow letters, digits and single dots in local part (no special chars like $)
# - require an @ and a domain with a dot and a TLD
email_address = r"^[A-Za-z](?:[A-Za-z0-9]|\.(?!\.))*@[A-Za-z0-9]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)
