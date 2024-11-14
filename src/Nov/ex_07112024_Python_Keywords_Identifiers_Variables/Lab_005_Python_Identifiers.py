# Rules for the Identifier (Name of the Variable)
#  They should always start with a letter (A-Z or a-z)
#  An underscore(_) followed by zero or more letters.
#  Underscores and digits(0-9)
a = 10 # Valid
_ = 55 # Valid
_ = _+2 # Valid
# 123 = 23 # Invalid
# 12abc = 34 # Invalid
# @123 = 73 # Invalid


print (type(_))

