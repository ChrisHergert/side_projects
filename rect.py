from pprint import pprint

## Define the test case coordinate sets as such:
##      "A_left_X, A_upper_Y, A_right_X, A_lower_Y, B_left_X, B_upper_Y, B_right_X, B_lower_Y"
coord_sets=["-3,3,-1,1,1,-1,3,-3",      # A above and left of B
            "-1,1,1,-1,-3,3,3,-3",      # B encompasses A
            "-3,3,-1,1,-1,1,3,-3"]      # Corner Contact

def is_left(A_left, B_left, B_right):
    '''Determines whether the shape demarcated by the B values is entirely to the left of shape A'''
    # if B_left < A_left and B_right < A_left: return True
    if B_right < A_left: return True
    else: return False
def is_right(A_right, B_left, B_right):
    '''Determines whether the shape demarcated by the B values is entirely to the right of shape A'''
    # if B_left>A_right and B_right>A_right: return True
    if B_left>A_right: return True
    else: return False
def is_above(A_top, B_top, B_bot):
    '''Determines whether the shape demarcated by the B values is entirely above shape A'''
    # if B_top > A_top and B_bot > A_top: return True
    if B_bot > A_top: return True
    else: return False
def is_below(A_bot, B_top, B_bot):
    '''Determines whether the shape demarcated by the B values is entirely below shape A'''
    # if B_top < A_bot and B_bot < A_bot: return True
    if B_top < A_bot: return True
    else: return False
def check_boundaries(a, b):
    if a < b: return True
    else: return False

if __name__=="__main__":

    ## Loop through the coordinate sets
    for coords in coord_sets:

        ##Get coordinates breakout
        a_left, a_top, a_right, a_bot, b_left, b_top, b_right, b_bot = [int(pt) for pt in coords.split(',')]

        ## Check for transcription errors on boundaries
        if not (check_boundaries(a_bot, a_top) or check_boundaries(a_left, a_right) or
            check_boundaries(b_bot, b_top) or check_boundaries(b_left, b_right)):
            print("The dimensions are not valid for these rectangles")
            pass

        ## If the boundaries are valid, proceed.
        else:

            ## Run comparisons on the rectangles' opposing boundaries
            comparisons = [ is_left(a_left, b_left, b_right),
                            is_right(a_right, b_left, b_right),
                            is_above(a_top, b_top, b_bot),
                            is_below(a_bot, b_top, b_bot)]

            ## Print outputs
            # pprint(comparisons)
            print("No overlap") if sum(comparisons) >= 2 else print("Overlap")
