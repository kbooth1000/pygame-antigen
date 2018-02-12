import pygame as pg
import math


def main(canvas_width, canvas_height):
    width = canvas_width
    height = canvas_height
    bg_color = (97, 159, 182)
    line_color = (182,59,247)

    pg.init()
    screen = pg.display.set_mode((1024, 768))
    pg.display.set_caption('Antigen')
    clock = pg.time.Clock()
    screen_w, screen_h = pg.display.get_surface().get_size()
     
    click_coords = []
    polygon_origin = ()
    grid_points = []
    highlight_point = ()

    antigen_list = []

    #class Antibody(python.sprite.Sprite):


    class Antigen(object):
        # def __init__(self, color):
        #     self.color = color
        def create(self, polygon_points_list, polygon_x, polygon_y, polygon_color):
            draw_polygon(polygon_points_list, polygon_x, polygon_y, polygon_color)

    def create_grid(grid_w, grid_h):
        for i in range(50, grid_h):
            if i % 50 == 0:
                for j in range(50, grid_w):
                    if j % 50 == 0:
                        pg.draw.circle(screen, (0,0,0), (j, i), 5, 1)
                        grid_points.append((j,i))

    def create_relative_polygon_list(coords_list):
        relative_polygon_points = []
        for r_point in coords_list:
            relative_polygon_points.append( ((r_point[0]-coords_list[0][0]), (r_point[1]-coords_list[0][1])) )
        return relative_polygon_points
        
    def draw_polygon(polygon_points_list, polygon_x, polygon_y, polygon_color):
        click_coords = []
        polygon_points = []
        for point in polygon_points_list:
            relative_point = ( (point[0]+polygon_x), (point[1]+polygon_y) )
            polygon_points.append(relative_point)
            

            if len(polygon_points) > 2:
                pg.draw.polygon(screen, polygon_color, polygon_points, 0)

    # Game initialization
    stop_game = False
    draw_shape = True
    grid_created = False
    draw_shape = False
    just_print_once = 0
    ####### GAME LOOP
    while not stop_game:

        

        
        for event in pg.event.get():   #####   EVENTS  ##########
            # Event handling

            
            
            if event.type == pg.MOUSEBUTTONUP:  #####  CLICK  ###########
                adjusted_click = ()
                mouse_pos = pg.mouse.get_pos()
                for point in grid_points:
                    distance_from_point = math.hypot(mouse_pos[0] - point[0], mouse_pos[1] - point[1])
                    if distance_from_point <= 9:
                        highlight_point = point
                        adjusted_click = point
                        click_coords.append(adjusted_click)
                        just_print_once = 0
                        break   

            # if event.type == pg.KEYUP:       ####  SPACEBAR  ###########
            #     if event.key == pg.K_SPACE:
            #         just_print_once = 0 # for testing
            #         print '---'
            #         print click_coords[len(click_coords)-1]
            #         draw_shape = True

            if len(click_coords) > 1:         ###  CLOSED SHAPE DRAWING  ##########
                if click_coords[len(click_coords)-1] == click_coords[0] and just_print_once == 0:
                    draw_shape = True
                    just_print_once = 0

            if event.type == pg.QUIT:
                stop_game = True


        # Game logic

        ####### DRAW BACKGROUND
        screen.fill(bg_color)

        create_grid(300, 300)
        
        if len(click_coords) >=1: 
                pg.draw.lines(screen, line_color, False, ( click_coords[len(click_coords)-1], pg.mouse.get_pos()  ), 4)

        
        if draw_shape:                  ####  CREATE ANTIGEN  ############
            antibody1 = Antigen()
            antibody1.create(
                    create_relative_polygon_list(click_coords),
                    500,
                    300, 
                    (255, 22, 22) 
                    )
            if just_print_once == 0: # ft
                print '##'
                print create_relative_polygon_list(click_coords) # ft
                just_print_once = 1 # ft
                click_coords = []
            draw_shape = False

        highlight_point_delay = 0
        if highlight_point != ():
            #while highlight_point_delay < 10000:
            highlight_point_delay += 1
            pg.draw.circle(screen, (222,0,255), highlight_point, 5, 0)
            

        if len(click_coords) > 1:
            pg.draw.lines(screen, line_color, False, click_coords, 4)

        # Game display

        pg.display.update()
        clock.tick(60)

    pg.quit()
    
    

# Create and print polygon coor point list

if __name__ == '__main__':
    main(800, 600)
