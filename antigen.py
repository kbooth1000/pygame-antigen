import pygame



def main(canvas_width, canvas_height):
    width = canvas_width
    height = canvas_height
    bg_color = (97, 159, 182)
    line_color = (182,159,97)

    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Squirreler')
    clock = pygame.time.Clock()
    screen_w, screen_h = pygame.display.get_surface().get_size()
     
    click_coords = []
    polygon_origin = ()

    def create_grid(grid_w, grid_h):
        for i in range(50, grid_h):
            if i % 50 == 0:
                for j in range(50, grid_w):
                    if j % 50 == 0:
                        pygame.draw.circle(screen, (0,0,0), (j, i), 5, 1)

    def create_relative_polygon_list(coords_list):
        relative_polygon_points = []
        for point in click_coords:
            relative_polygon_points.append( ((point[0]-coords_list[0][0]), (point[1]-coords_list[0][1])) )
        return relative_polygon_points
        
    def draw_polygon(polygon_points_list, polygon_x, polygon_y, polygon_color):
        polygon_points = []
        for point in polygon_points_list:
            relative_point = ( (point[0]+polygon_x), (point[1]+polygon_y) )
            polygon_points.append(relative_point)
            
            if len(polygon_points) > 2:
                pygame.draw.polygon(screen, polygon_color, polygon_points, 0)

    

    # Game initialization
    stop_game = False
    draw = False
    while not stop_game:
        
        for event in pygame.event.get():
            # Event handling
            
            if event.type == pygame.MOUSEBUTTONUP:
                print pygame.mouse.get_pos()
                click_coords.append(pygame.mouse.get_pos())
                draw = False

            
            if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
                draw = True

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(bg_color)

        create_grid(300, 300)

        if draw:
            draw_polygon(
                    create_relative_polygon_list(click_coords),
                    500,
                    100, 
                    (255, 22, 22) 
                    )


        if len(click_coords) > 1:
            pygame.draw.lines(screen, line_color, True, click_coords, 2)

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    
    

# Create and print polygon coor point list

    

    print create_relative_polygon_list(click_coords)


    print click_coords
if __name__ == '__main__':
    main(800, 600)
