def colisao(ret1,ret2):
    rect1_x = ret1[:1]
    rect1_y = ret1[2:3]
    rect1_width = ret1[4:5]
    rect1_height = ret1[6:7]

    rect2_x = ret2[:1]
    rect2_y = ret2[2:3]
    rect2_width = ret2[4:5]
    rect2_height = ret2[6:7]

    if (rect1_x < rect2_x + rect2_width and
            rect1_x + rect1_width > rect2_x and
            rect1_y < rect2_y + rect2_height and
            rect1_y + rect1_height > rect2_y):

        return True

    else:

        return False



print(colisao('6,5,3,7','3,2,6,8'))