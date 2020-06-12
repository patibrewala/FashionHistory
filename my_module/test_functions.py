from functions import print_decade_info, print_apparel_info

def test_print_decade_info():
    """
    Asserts if function 'print_decade_info()' is working properly
    """

    info_2020 = """
It is currently 2020, a new decade where people are in lockdown. 
No fashion history available for current year.
"""
    info_out = "Fashion history could not be found. Please try again!"
    info_err = "Year not entered correctly. Please try again!"

    # test for a correct year
    assert print_decade_info("2020") == info_2020

    # test for a year whose history is not available
    assert print_decade_info("1722") == info_out

    # test for invalid input i.e integer that is not a year.
    assert print_decade_info("19") == info_err

    # test to check return value is a string
    assert isinstance(print_decade_info("1983"), str)

def test_print_apparel_info(): 
    """
    Asserts if function 'print_apparel_info()' is working properly
    """

    info_shorts = """
Shorts are a garment worn over the pelvic area, circling the waist and splitting 
to cover the upper part of the legs, sometimes extending down to the knees but 
not covering the entire length of the leg. They are called "shorts" because they 
are a shortened version of trousers, which cover the entire leg, but not the 
foot. Shorts are typically worn in warm weather or in an environment where 
comfort and air flow are more important than the protection of the legs. 

In much of Europe and the Americas during the 19th and early 20th centuries, 
shorts were worn as outerwear only by young boys until they reached a certain 
height or maturity. The 1950s decade was the first that embraced women wearing 
shorts for more than just beach wear or for pinup girls. Women’s 1950s shorts 
came in several lengths and styles to fit a variety of leisure activities women 
enjoyed. Today shorts have become a staple for all women and multiple pairs came 
be found in their closets. They are of many different lengths and made of many 
different fabrics. 
"""
    info_return = """
No article of clothing with that name was found! 
Please check your spelling and try again.
"""

    # test to check correct output is returned for a valid input
    assert print_apparel_info("shorts") == info_shorts

    # test to check for clothing items whose history is not available
    assert print_apparel_info("bandana") == info_return

    # test to check for strings which are not apparel
    assert print_apparel_info("hello") == info_return

    # test to check return value is a string
    assert isinstance(print_apparel_info("bikini"), str)

	#just to see
	#assert print_apparel_info("sssss") == info_shorts





