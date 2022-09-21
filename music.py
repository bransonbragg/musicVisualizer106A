"""
Interactive Piano Display and MIDI File Reader

Branson Bragg

This program contains an interactive piano and a music player/displayer GUI.

MIDI files were taken from vgmusic.com and jacobspiano.com/midi-files
"""
import KeyPress
import mido
import pygame
import random
import time

midi_files = ['Music Midis/smbt.mid', 'Music Midis/bloody.mid',  'Music Midis/Gravity-Falls-MIDI.mid', 'Music Midis/wheel.mid', 'Music Midis/Pianotris.mid']

CANVAS_WIDTH = 1150
CANVAS_HEIGHT = 700

IMAGE_HEIGHT = CANVAS_HEIGHT * 2 // 3

PIANO_WHITE_KEYS = 52
TOTAL_PIANO_KEYS = 88
TOP_OF_KEYS = CANVAS_HEIGHT * 3 // 4

INTERACTIVE_WHITE_KEYS = 21
TOTAL_INTERACTIVE_KEYS = 36

# Below are the color schemes for each song, background color for each note is chosen randomly from the applicable list
mario_note_colors = [(248, 222, 126), (255, 0, 0), (0, 255, 0), (0, 0, 255), (101, 67, 33)]
bloody_note_colors = [(255, 90, 54), (178, 34, 34), (220, 220, 220), (100, 100, 100), (200, 200, 200), (255, 255, 0)]
tetris_note_colors = [(255, 50, 19), (3, 65, 174), (114, 203, 59), (255, 213, 0), (255, 151, 28)]
wheel_note_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 105, 180), (255, 69, 0), (255, 255, 0)]
gravity_note_colors = [(0, 128, 128), (255, 42, 4), (0, 0, 200), (0, 255, 0), (0, 128, 128), (255, 42, 4), (0, 0, 200), (0, 255, 0), (0, 128, 128), (255, 42, 4)]
interactive_piano_colors = [(255, 255, 255)]


preview_images = ['Images/mario_preview.jpeg', 'Images/castlevania_preview.png', 'Images/gravity_preview.jpeg', 'Images/wheel_preview.jpg', 'Images/tetris_preview.jpg']


class Midi:
    """
    Any time the below code dictates that a note be pressed or released, this class is instantiated.

    This Midi class also communicates with the KeyPress class to get x locations (to save code clutter on this page)
    """
    def __init__(self, note_location, delay_time, midi_file):
        if type(note_location) == str:
            note_location = note_location.split('note=')
            self.note_location = KeyPress.KeyPress.get_location_x(int(note_location[1]) - 21)  # Gets location number of note 0-88
        elif note_location is not None:
            self.note_location = self.get_interactive_x(note_location, False)
        if type(delay_time) == str:
            delay_time = delay_time.split('time=')
            self.delay_time = float(delay_time[1])  # Amount of "wait time" before the next note
        self.midi_file = midi_file

    def create_surface(self, screen, note_locations):  # Given a list of note locations, draw arrows at those locations
        surface_width = CANVAS_WIDTH // TOTAL_PIANO_KEYS
        if type(note_locations) == list:
            for note_location_x in note_locations:
                triangle_point1 = surface_width // 2, TOP_OF_KEYS - IMAGE_HEIGHT
                triangle_point2 = 0, TOP_OF_KEYS - 20 - IMAGE_HEIGHT,
                triangle_point3 = surface_width, TOP_OF_KEYS - 20 - IMAGE_HEIGHT

                surface = (pygame.Surface([surface_width, TOP_OF_KEYS - IMAGE_HEIGHT]))
                surface.fill(random.choice(Midi.get_color_set(self.midi_file)))
                pygame.draw.polygon(surface, (0, 0, 0), (triangle_point1, triangle_point2, triangle_point3))
                screen.blit(surface, (note_location_x, IMAGE_HEIGHT))

    @staticmethod
    def erase_surface(screen, note_locations):
        surface_width = CANVAS_WIDTH // TOTAL_PIANO_KEYS
        for note_location_x in note_locations:
            surface = (pygame.Surface([surface_width, TOP_OF_KEYS - IMAGE_HEIGHT]))
            surface.fill((255, 255, 255))
            screen.blit(surface, (note_location_x, IMAGE_HEIGHT))

    def get_interactive_x(self, location, black_key_option):
        typical_formula = (CANVAS_WIDTH / PIANO_WHITE_KEYS) * int(location)

        if black_key_option != "yes":
            if (location - 4) % 7 == 0 or (location - 6) % 7 == 0 or location % 7 == 0:  # Note is E, G, A
                return typical_formula - 3
            return typical_formula
        else:
            if (location - 1) % 7 != 0 or (location - 4) % 7 != 0:  # 2, 3, 5, 6, 7
                return typical_formula + 30

    @staticmethod
    def get_color_set(midi_file):
        if midi_file == 'Music Midis/smbt.mid':
            return mario_note_colors
        elif midi_file == 'Music Midis/bloody.mid':
            return bloody_note_colors
        elif midi_file == 'Music Midis/Pianotris.mid':
            return tetris_note_colors
        elif midi_file == "Music Midis/wheel.mid":
            return wheel_note_colors
        elif midi_file == "Music Midis/Gravity-Falls-MIDI.mid":
            return gravity_note_colors
        else:
            return interactive_piano_colors


def main():
    pygame.init()
    create_starting_canvas()
    pygame.display.update()

    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():  # Event loop required to keep PyGame window open on Mac
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_position[0] <= CANVAS_WIDTH * 0.2 and mouse_position[1] >= CANVAS_HEIGHT * 0.75:
                    start_song(midi_files[0])  # Super Mario Bros
                    main()
                elif mouse_position[0] <= CANVAS_WIDTH * 0.4 and mouse_position[1] >= CANVAS_HEIGHT * 0.75:
                    start_song(midi_files[1])  # Castlevania
                    main()
                elif mouse_position[0] <= CANVAS_WIDTH * 0.6 and mouse_position[1] >= CANVAS_HEIGHT * 0.75:
                    start_song(midi_files[2])  # Gravity Falls
                    main()
                elif mouse_position[0] <= CANVAS_WIDTH * 0.8 and mouse_position[1] >= CANVAS_HEIGHT * 0.75:
                    start_song(midi_files[3])  # Wheel of Fortune
                    main()
                elif mouse_position[0] > CANVAS_WIDTH * 0.8 and mouse_position[1] >= CANVAS_HEIGHT * 0.75:
                    start_song(midi_files[4])  # Tetris
                    main()
                elif CANVAS_WIDTH * 2 // 5 <= mouse_position[0] <= CANVAS_WIDTH * 3 // 5 and CANVAS_HEIGHT // 4 >= mouse_position[1]:
                    interactive()  # Interactive piano
                    main()
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                break


def create_starting_canvas():
    """
    This function creates the start screen canvas
    """
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("MIDI Home Page")
    screen.fill((255, 255, 0))
    for i in range(len(preview_images)):
        image_preview = pygame.image.load(preview_images[i]).convert()
        scaled_preview = pygame.transform.scale(image_preview,
                                                (CANVAS_WIDTH // len(preview_images), CANVAS_HEIGHT // 4))
        screen.blit(scaled_preview, (int((CANVAS_WIDTH / len(preview_images)) * i), CANVAS_HEIGHT * 3 // 4))
    background_setup = pygame.image.load('Images/start_screen_new.png')
    scaled_background = pygame.transform.scale(background_setup, (CANVAS_WIDTH, CANVAS_HEIGHT * 3 // 4))
    screen.blit(scaled_background, (0, 0))
    interactive_preview = pygame.image.load('Images/piano_preview.jpg').convert()
    interactive_background = pygame.transform.scale(interactive_preview,
                                                    (CANVAS_WIDTH // 4, (CANVAS_HEIGHT // 5)))
    screen.blit(interactive_background, (int(CANVAS_WIDTH * 0.375), 0))
    return screen


def start_song(midi_file):
    """
    This function orchestrates the entire secondary display, and is run if the user chooses a song
    """
    music = mido.MidiFile(midi_file)  # creates human-readable file from MIDI for line-by-line classification
    screen = create_music_canvas(midi_file)
    draw_piano_keys(screen)
    pygame.display.flip()
    music_playing = False
    while True:
        for event in pygame.event.get():  # Event loop required to keep window open on Mac
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                break
        notes = []  # This holds the notes contained in each chord (notes added when time delay == 0)
        for line in music:
            read_music_line = str(line)
            read_music_line = read_music_line.strip()
            if "note=" in read_music_line and len(read_music_line) >= 5:  # Denotes a note being played or released
                read_music_line = read_music_line.split(" ")
                if read_music_line[4] != "time=0>":
                    note_press = Midi(read_music_line[2], read_music_line[4], midi_file)
                    if read_music_line[0] == "note_on" and read_music_line[3] != "velocity=0":
                        if float(note_press.delay_time) == 0:  # Gets the notes to be played simultaneously
                            notes.append(note_press.note_location)
                        else:
                            if music_playing is False:
                                play_music(midi_file)
                                music_playing = True
                            notes.append(note_press.note_location)
                            note_press.create_surface(screen, notes)
                            pygame.display.update()
                            staggered_sleep_time(midi_file, note_press)
                    elif read_music_line[0] == "note_on" and read_music_line[3] == "velocity=0" or read_music_line[0] == "note_off":  # A note is released
                        if float(note_press.delay_time) == 0:  # Get the notes to be removed simultaneously and erases them all at once
                            notes.append(note_press.note_location)
                        else:
                            notes.append(note_press.note_location)
                            Midi.erase_surface(screen, notes)
                            keep_notes_visual = staggered_sleep_time(midi_file, note_press)
                            pygame.display.update()
                            notes = []
            elif "control_change" in read_music_line:
                read_music_line = str(line)
                read_music_line = read_music_line.strip()
                read_music_line = read_music_line.split(" ")
                note_press = Midi(None, read_music_line[4], midi_file)
                staggered_sleep_time(midi_file, note_press)
        break


def create_music_canvas(midi_file):
    """
    This function creates the canvas template that is used throughout the entire program
    """
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("MIDI Reader and Piano")
    screen.fill((255, 255, 255))
    if midi_file is not None:
        set_background_image(screen, midi_file)
    pygame.display.update()
    return screen


def draw_piano_keys(screen):
    """
    This function makes the piano key layout on the display
    """
    for i in range(PIANO_WHITE_KEYS + 1):
        white_key_left = i * CANVAS_WIDTH // PIANO_WHITE_KEYS
        white_key_top = TOP_OF_KEYS
        white_key_width = CANVAS_WIDTH // PIANO_WHITE_KEYS
        white_key_height = CANVAS_HEIGHT // 4

        pygame.draw.line(screen, (0, 0, 0), (0, white_key_top), (CANVAS_WIDTH, white_key_top))
        pygame.draw.rect(screen, (255, 255, 255), (white_key_left, white_key_top, white_key_width, white_key_height))
        pygame.draw.line(screen, (0, 0, 0), (white_key_left, white_key_top), (white_key_left, CANVAS_HEIGHT))
        pygame.display.flip()  # updating the display every loop iteration produces a cool drawing effect

    for i in range(PIANO_WHITE_KEYS + 1):
        white_key_left = i * CANVAS_WIDTH // PIANO_WHITE_KEYS
        white_key_top = TOP_OF_KEYS
        white_key_width = CANVAS_WIDTH // PIANO_WHITE_KEYS
        white_key_height = CANVAS_HEIGHT // 4

        black_key_width = int(white_key_width * (1 / 2))
        black_key_height = int(white_key_height * 2 / 3)
        black_key_left = (white_key_left + white_key_width - (black_key_width // 3))
        black_key_top = white_key_top

        if i == 0:  # Draw black keys
            pygame.draw.rect(screen, (0, 0, 0), (black_key_left, black_key_top, black_key_width, black_key_height))
        elif (i - 2) % 7 == 0:
            for j in range(2):
                pygame.draw.rect(screen, (0, 0, 0), (black_key_left + (white_key_width * j), black_key_top, black_key_width, black_key_height))
                pygame.display.flip()
            for j in range(3):
                pygame.draw.rect(screen, (0, 0, 0), (black_key_left + (white_key_width * (j + 3)), black_key_top, black_key_width, black_key_height))
                pygame.display.flip()


def interactive():
    screen = create_music_canvas(None)
    draw_interactive_keys(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not pygame.mixer.get_busy():
                mouse_position = pygame.mouse.get_pos()
                note = KeyPress.KeyPress(mouse_position[0], mouse_position[1])
                sound = note.play_note()
                if sound is not None:
                    pygame.mixer.music.load(sound)
                    pygame.mixer.music.play()
                elif mouse_position[1] <= CANVAS_HEIGHT * 3 // 4:
                    main()
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                break


def draw_interactive_keys(screen):
    """
    This function makes the interactive piano key layout on the display
    """

    background_interactive = pygame.image.load('Images/interactive_background.png')
    scaled_interactive = pygame.transform.scale(background_interactive, (CANVAS_WIDTH, TOP_OF_KEYS))
    screen.blit(scaled_interactive, (0, 0))

    for i in range(INTERACTIVE_WHITE_KEYS + 1):  # Draw white keys
        white_key_left = i * CANVAS_WIDTH // INTERACTIVE_WHITE_KEYS
        white_key_top = TOP_OF_KEYS
        white_key_width = CANVAS_WIDTH // INTERACTIVE_WHITE_KEYS
        white_key_height = CANVAS_HEIGHT // 4

        pygame.draw.line(screen, (0, 0, 0), (0, white_key_top), (CANVAS_WIDTH, white_key_top))
        pygame.draw.rect(screen, (255, 255, 255), (white_key_left, white_key_top, white_key_width, white_key_height))
        pygame.draw.line(screen, (0, 0, 0), (white_key_left, white_key_top), (white_key_left, CANVAS_HEIGHT))

    for i in range(INTERACTIVE_WHITE_KEYS + 1):  # Draw black keys
        white_key_left = i * CANVAS_WIDTH // INTERACTIVE_WHITE_KEYS
        white_key_top = TOP_OF_KEYS
        white_key_width = CANVAS_WIDTH // INTERACTIVE_WHITE_KEYS
        white_key_height = CANVAS_HEIGHT // 4

        black_key_width = int(white_key_width * (1 / 2))
        black_key_height = int(white_key_height * 2 / 3)
        black_key_left = (white_key_left + white_key_width - (black_key_width // 3))
        black_key_top = white_key_top
        if i == 0:
            pygame.draw.rect(screen, (0, 0, 0), (black_key_left, black_key_top, black_key_width, black_key_height))
        elif (i - 2) % 7 == 0 and i < 20:
            for j in range(2):
                pygame.draw.rect(screen, (0, 0, 0), (
                black_key_left + (white_key_width * j), black_key_top, black_key_width, black_key_height))
            for j in range(3):
                pygame.draw.rect(screen, (0, 0, 0), (
                black_key_left + (white_key_width * (j + 3)), black_key_top, black_key_width, black_key_height))


def staggered_sleep_time(midi_file, note_press):
    """
    Each song has a slightly different time delay when python loops over the lines of the file,
    so these time delay optimizations keep each song in sync throughout its entire run time.
    """

    if midi_file == 'Music Midis/smbt.mid':
        if float(note_press.delay_time) >= .0028:
            time.sleep(float(note_press.delay_time) - .0028)
            return float(note_press.delay_time) - .0028
        else:
            time.sleep(float(note_press.delay_time))
            return float(note_press.delay_time)

    elif midi_file == 'Music Midis/bloody.mid':
        if float(note_press.delay_time) >= .0026:
            time.sleep(float(note_press.delay_time) - .0026)
            return float(note_press.delay_time) - .0026
        else:
            time.sleep(float(note_press.delay_time))
            return float(note_press.delay_time)

    elif midi_file == 'Music Midis/wheel.mid':
        if float(note_press.delay_time) >= .0046:
            time.sleep(float(note_press.delay_time) - .0046)
            return float(note_press.delay_time) - .0046
        else:
            time.sleep(float(note_press.delay_time))
            return float(note_press.delay_time)

    elif midi_file == 'Music Midis/Pianotris.mid':
        if float(note_press.delay_time) >= .002:
            time.sleep(float(note_press.delay_time) - .002)
        else:
            time.sleep(float(note_press.delay_time))

    elif midi_file == 'Music Midis/Gravity-Falls-MIDI.mid':
        if float(note_press.delay_time) >= .0045:
            time.sleep(float(note_press.delay_time) - .0045)
        else:
            time.sleep(float(note_press.delay_time))



def set_background_image(screen, midi_file):
    """
    This function sets the specific image to be displayed above the piano when the chosen song begins
    """
    if midi_file == "Music Midis/smbt.mid":
        mario_image = pygame.image.load('Images/mario_project2.jpg')
        scaled_mario = pygame.transform.scale(mario_image, (CANVAS_WIDTH, IMAGE_HEIGHT))
        screen.blit(scaled_mario, (0, 0))
    elif midi_file == "Music Midis/bloody.mid":
        bloody_image = pygame.image.load('Images/bloody_image.jpg')
        scaled_bloody = pygame.transform.scale(bloody_image, (CANVAS_WIDTH, IMAGE_HEIGHT))
        screen.blit(scaled_bloody, (0, 0))
    elif midi_file == "Music Midis/Pianotris.mid":
        tetris_image = pygame.image.load('Images/tetris_contest.jpeg')
        scaled_tetris = pygame.transform.scale(tetris_image, (CANVAS_WIDTH, IMAGE_HEIGHT))
        screen.blit(scaled_tetris, (0, 0))
    elif midi_file == "Music Midis/wheel.mid":
        wheel_image = pygame.image.load('Images/wheel_image.jpg')
        scaled_wheel = pygame.transform.scale(wheel_image, (CANVAS_WIDTH, IMAGE_HEIGHT))
        screen.blit(scaled_wheel, (0, 0))
    elif midi_file == "Music Midis/Gravity-Falls-MIDI.mid":
        gravity_image = pygame.image.load('Images/gravity_background.jpeg')
        scaled_gravity = pygame.transform.scale(gravity_image, (CANVAS_WIDTH, IMAGE_HEIGHT))
        screen.blit(scaled_gravity, (0, 0))
    return screen


def play_music(file):
    """
    This function plays the chosen song
    """
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


if __name__ == "__main__":
    main()
