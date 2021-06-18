from tkinter import Tk, Frame, Canvas, BOTH

def main():
    width = 800
    height = 500

    root = Tk()
    root.geometry(f"{width}x{height}")

    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
   
    draw_sky(canvas, 0, 0)
    draw_moon(canvas, 200, 450)
    draw_planet1(canvas, 302, 12)
    draw_planet1(canvas, 620, 142)
    draw_planet1(canvas, 154, 310)
    draw_planet2(canvas, 550, 260)
    draw_planet2(canvas, 310, 260)
    draw_planet2(canvas, 200, 200)
    draw_planet3(canvas, 389, 400)
    draw_planet3(canvas, 752, 300)
    draw_planet3(canvas, 120, 121)
    draw_planet4(canvas, 80, 25)
    draw_planet4(canvas, 500, 150)
    draw_rocket(canvas, 400,120,210)
    draw_sun(canvas, 600, 20)
    draw_window(canvas,386,180)
    draw_crater(canvas,50, 460)
    draw_crater(canvas,250, 470)
    draw_crater(canvas,400, 465)
    draw_crater(canvas,565, 465)
    draw_crater(canvas,710, 470)
    draw_fire_orange(canvas,387,325)
    draw_fire_orange(canvas,392,325)
    draw_fire_orange(canvas,397,325)
    draw_fire_orange(canvas,402,325)
    draw_fire_orange(canvas,407,325)
    draw_fire_orange(canvas,387,330)
    draw_fire_orange(canvas,392,330)
    draw_fire_orange(canvas,397,330)
    draw_fire_orange(canvas,402,330)
    draw_fire_orange(canvas,407,330)
    draw_fire_orange(canvas,387,335)
    draw_fire_orange(canvas,392,335)
    draw_fire_orange(canvas,397,335)
    draw_fire_orange(canvas,402,335)
    draw_fire_orange(canvas,407,335)
    draw_fire_orange(canvas,389,340)
    draw_fire_orange(canvas,391,340)
    draw_fire_orange(canvas,393,340)
    draw_fire_orange(canvas,395,340)
    draw_fire_orange(canvas,397,340)
    draw_fire_orange(canvas,399,340)
    draw_fire_orange(canvas,401,340)
    draw_fire_orange(canvas,403,340)
    draw_fire_orange(canvas,391,345)
    draw_fire_orange(canvas,393,345)
    draw_fire_orange(canvas,395,345)
    draw_fire_orange(canvas,397,345)
    draw_fire_orange(canvas,399,345)
    draw_fire_orange(canvas,401,345)
    draw_fire_orange(canvas,403,345)
    draw_fire_orange(canvas,405,345)
    draw_fire_orange(canvas,393,350)
    draw_fire_orange(canvas,395,350)
    draw_fire_orange(canvas,397,350)
    draw_fire_orange(canvas,399,350)
    draw_fire_orange(canvas,401,350)
    draw_fire_orange(canvas,403,350)

    
def draw_sky(canvas, screen_left, screen_top):
    screen_top = 0
    screen_left = 0
    screen_right = 801
    sky_bottom = 450
    canvas.create_rectangle(screen_left, screen_top, screen_right, sky_bottom, fill="gray1", width=False)

def draw_moon(canvas, moon_left, moon_top):
    moon_left = -650
    moon_top = 450
    moon_right = 2000
    moon_bottom = 500
    canvas.create_oval(moon_left, moon_top, moon_right, moon_bottom, fill= "seashell4", width=False)

def draw_planet1(canvas, planet1_left, planet1_top):
    planet1_width = 20
    planet1_height = 20
    planet1_right = planet1_left + planet1_width
    planet1_bottom = planet1_top + planet1_height
    canvas.create_oval(planet1_left, planet1_top, planet1_right, planet1_bottom, fill="springgreen2", width=False)

def draw_planet2(canvas, planet2_left, planet2_top):
    planet2_width = 10
    planet2_height = 10
    planet2_right = planet2_left + planet2_width
    planet2_bottom = planet2_top + planet2_height
    canvas.create_oval(planet2_left, planet2_top, planet2_right, planet2_bottom, fill="cyan", width=False)

def draw_planet3(canvas, planet3_left, planet3_top):
    planet3_width = 22
    planet3_height = 22
    planet3_right = planet3_left + planet3_width
    planet3_bottom = planet3_top + planet3_height
    canvas.create_oval(planet3_left, planet3_top, planet3_right, planet3_bottom, fill="maroon2", width=False)

def draw_planet4(canvas, planet4_left, planet4_top):
    planet4_width = 34
    planet4_height = 34
    planet4_right = planet4_left + planet4_width
    planet4_bottom = planet4_top + planet4_height
    canvas.create_oval(planet4_left, planet4_top, planet4_right, planet4_bottom, fill="red2", width=False)


def draw_smoke(canvas, smoke_left, smoke_top, scale = 1):
    smoke_width = 150 * scale
    smoke_height = 90 * scale
    smoke_right = smoke_left + smoke_width * scale
    smoke_bottom = smoke_top + smoke_height * scale
    canvas.create_oval(smoke_left, smoke_top, smoke_right, smoke_bottom, fill="seashell4", width=False)

def draw_sun(canvas, sun_left, sun_top):
    sun_width = 80
    sun_height = 80
    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="gold2", width=False)

def draw_rocket(canvas, peak_x, peak_y, height):
 
    rocket_width = 35
    rocket_height = 85
    rocket_left = peak_x - rocket_width / 2
    rocket_right = peak_x + rocket_width / 2
    rocket_bottom = peak_y + height

    rocket_top_width = 38
    rocket_top_height = 35
    rocket_top_left = peak_x - rocket_top_width / 2
    rocket_top_right = peak_x + rocket_top_width / 2
    rocket_top_bottom = peak_y + rocket_top_height

    canvas.create_rectangle(rocket_left, rocket_top_bottom,
            rocket_right, rocket_bottom,
            outline="gray20", width=1, fill="gray38")

    canvas.create_polygon(peak_x, peak_y,
            rocket_top_right, rocket_top_bottom,
            rocket_top_left, rocket_top_bottom,
            outline="gray20", width=1, fill="Slateblue2")

def draw_window(canvas, window_left, window_top):
    window_width = 30
    window_height = 30
    window_right = window_left + window_width
    window_bottom = window_top + window_height
    canvas.create_oval(window_left, window_top, window_right, window_bottom, fill="CadetBlue2", width=False)

def draw_crater(canvas, crater_left, crater_top):
    crater_width = 100
    crater_height = 20
    crater_right = crater_left + crater_width
    crater_bottom = crater_top + crater_height
    canvas.create_oval(crater_left, crater_top, crater_right, crater_bottom, fill="gray13", width=False)

def draw_fire_orange(canvas, fire_orange_left, fire_orange_top):
    fire_orange_width = 10
    fire_orange_height = 10
    fire_orange_right = fire_orange_left + fire_orange_width
    fire_orange_bottom = fire_orange_top + fire_orange_height
    canvas.create_oval(fire_orange_left, fire_orange_top, fire_orange_right, fire_orange_bottom, fill="orange red", width=False)


main()