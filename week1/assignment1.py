import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    return re.findall("[A-Z]+[a-zA-Z]*",simple_string)
    
print(names())


print(len(names()) == 4)


assert len(names()) == 4, "There are four names in the simple_string"


def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
    
#     print(grades)
    w = '([A-Z][a-z]+ [A-Z][a-z]+): B'
#     ([A-Z][a-z]+ [A-Z][a-z]+): B
    grades = re.findall(w , grades)
    return grades

    # YOUR CODE HERE

print(grades)

assert len(grades()) == 16


# ## Part C
# 
# Consider the standard web log file in [assets/logdata.txt](assets/logdata.txt). This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
# * a host (e.g., '146.204.224.152') 
# * a user_name (e.g., 'feest6811' **note: sometimes the user name is missing! In this case, use '-' as the value for the username.**)
# * the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# * the post request type (e.g., 'POST /incentivize HTTP/1.1' **note: not everything is a POST!**)

def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    reg_pattern="""
        (?P<host>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)(\ - \ )
        (?P<user_name>(\w*)(\S))(\  \S)
        (?P<time>\d+\S\w*\S\d+\S\d+\S\d+\S\d+\s\S\d+)(\S\s\S)
        (?P<request>\w*\s\S*\s\w*\S\d.\d*)
    """
    final_data=[]
    for iter_data in re.finditer(reg_pattern,logdata,re.VERBOSE):
        val = iter_data.groupdict()
        final_data.append(val)
    return final_data


assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"

