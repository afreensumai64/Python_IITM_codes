def extract_email_username(email: str) -> str:
    '''
    Given an email address string of the form "username@domain.com", 
    return just the username part (everything before the @ symbol).

    Examples:
    >>> extract_email_username("ananya.sharma@iitd.ac.in")
    "ananya.sharma"
    >>> extract_email_username("rahul123@gmail.com")
    "rahul123"
    >>> extract_email_username("priya_r@company.in")
    "priya_r"
    >>> extract_email_username("v.kumar@institute.edu")
    "v.kumar"

    Args:
        email (str): A valid email address

    Returns:
        str: The username part of the email (before the @)
    '''
    ...
    return email.split('@')[0]
