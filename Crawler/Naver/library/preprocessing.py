def remove_quot(letter):
    quot_list = ['"', "'", "&quot", ";", ",", "...", "..", "…", '‘', '’', '“', '”']
    for tmp in quot_list:
        letter = letter.replace(tmp, '')
    return letter
