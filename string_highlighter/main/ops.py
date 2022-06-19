from . import consts

def highlight_string(string):
    return "<mark>"+string+"</mark>"

def prepare_error(error_string):
    return "<p> ERROR: " + error_string + "</p>"

def html_string_with_highlight(string, start, end):
    is_empty_check = validate_string_start_end_is_empty(string, start, end)
    if is_empty_check is not True:
        return prepare_error(is_empty_check)

    start = int(start)
    end = int(end)
    
    validity_check = validate_scenario(start, end, string)
    if validity_check is not True:
        return prepare_error(validity_check)

    return "<p>Output: " + string[:start] + highlight_string(string[start:end])  + string[end:] + "</p>"

def validate_scenario(start, end, string):
    if validate_start_le_end(start,end) is False:
        return consts.MESSAGES['START_GT_END']
    if validate_start_end_not_negetive(start, end) is False:
        return consts.MESSAGES['START_END_NEGETIVE']
    if validate_end_gt_len_string(string, end) is False:
        return consts.MESSAGES['END_GT_LEN_STRING']
    return True

def validate_string_start_end_is_empty(string, start, end):
    if start =='' or end =='' or string == '':
        return consts.MESSAGES['STRING_START_END_IS_EMPTY']
    return True

def validate_start_le_end(start, end):
    if start >= end:
        return False
    return True

def validate_start_end_not_negetive(start,end):
    if start < 0 or end < 0:
        return False
    return True

def validate_end_gt_len_string(string, end):
    if end > len(string):
        return False
    return True