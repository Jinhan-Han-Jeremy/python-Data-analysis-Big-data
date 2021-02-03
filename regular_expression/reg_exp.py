
import re

def grammar0 (x):
    """Captalize the first word of the paragraph and indent it with 2 spaces."""
    # xxx in the code here
    y = x.group('uppercase')

    return "  " + y[-1].capitalize() # The capitalized last char
    # .group() returns the part of the string where there was a match

x = """   she saw a orange in the tree.
 i ate a apple today, didn't i?
 he saw a orange in the tree.
   i have an book, don't i?"""


# xxx fill in the regular expression (re) below in the same line line
# \s+ consume spaces and \w consume first character
p0 = r"(?P<uppercase>^\s+\w)"

"""
    \s Matches any whitespace character; 
    \w Matches any alphanumeric character;
    ^ start matching inside string
    ?p<format> capture "foramt"group
    """

x = re.sub (p0, grammar0, x )


answer = """  She saw a orange in the tree.
 i ate a apple today, didn't i?
 he saw a orange in the tree.
   i have an book, don't i?"""

try:
    assert str(x )==str(answer),  "fail!"
    print ("The testcase passes!\n\n")
except AssertionError as e:
    print( e )
finally:
    print (x)
def grammar1 (x):
    """Captalize the first word of each sentence."""
    y = x.group('uppercase')
    # xxx fill in the missing codes
    return y[0] + "\n" + y[-1].capitalize()

# xxx fill in the regular expression (re) below in the same line line
p1 = r"(?P<uppercase>[?.!]\s+\w)"
    #[?.!]$ must end with ? or ! or .


x = re.sub (p1, grammar1, x )

answer = """  She saw a orange in the tree.
I ate a apple today, didn't i?
He saw a orange in the tree.
I have an book, don't i?"""

try:
    assert str(x)==str(answer),  "fail!"
    print ("The testcase passes!\n\n")
except AssertionError as e:
    print( e )
finally:
    print (x)

def grammar2 (x):
    """Uppercase each little i"""
    y =x.group('I')
    # xxx fill in the missing codes
    return y[0] + y[1].capitalize() + y[2]
    #0, 1, 2 character in string y

# xxx fill in the regular expression (re) below in the same line line
p2 = r"(?P<I>\si\s|\si[?.!])"
#if P<i>

x = re.sub(p2, grammar2, x)
answer = """  She saw a orange in the tree.
I ate a apple today, didn't I?
He saw a orange in the tree.
I have an book, don't I?"""

try:
    assert str(x)==str(answer),  "fail!"
    print ("The testcase passes!\n\n")
except AssertionError as e:
    print( e )
finally:
    print (x)


def grammar3(x):
    """Correct the usage of indefinite article """
    y = x.group('indefinite')
    # xxx fill in the missing codes
    if (y[2] == 'n'):  # If we change an to a
        y = " a" + y[3:]

    else:
        y = " an" + y[2:]

    return y


# xxx fill in the regular expression (re) below in one line
p3 = r"(?P<indefinite>\sa\s+[aeiou]|\san\s+[bcdfghjklmnpqrstvwxyz])"
x = re.sub(p3, grammar3, x)

answer = """  She saw an orange in the tree.
I ate an apple today, didn't I?
He saw an orange in the tree.
I have a book, don't I?"""

try:
    assert str(x) == str(answer), "fail!"
    print ("The testcase passes!\n\n")
except AssertionError as e:
    print(e)
finally:
    print (x)