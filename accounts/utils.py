import re

def validate_ghanaian_phone_number(phone_number):
    # Remove any spaces or special characters from the phone number
    cleaned_phone_number = re.sub(r'[^\d]', '', phone_number)

    # Check if the phone number matches the Ghanaian phone number pattern
    pattern = r'^0(?:20|24|55|54|26|27|57|23)\d{7}$'
    if not re.match(pattern, cleaned_phone_number):
        return False

    return True





