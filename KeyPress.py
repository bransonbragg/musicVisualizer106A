"""
KeyPress.py
Branson Bragg

This is a class for my music.py project. Essentially just a sub-class of Midi

--When this class is called for the interactive piano, it returns a MIDI file
    containing the applicable note to be played.

--When this class is called for the music displayer, it returns the
    precise x-location for the applicable note.
"""
note_midis = ['Midi Notes/Midi Notes/a3.mid', 'Midi Notes/Midi Notes/a-3.mid', 'Midi Notes/Midi Notes/b3.mid', 'Midi Notes/Midi Notes/c3.mid',
              'Midi Notes/Midi Notes/c-3.mid', 'Midi Notes/Midi Notes/d3.mid', 'Midi Notes/Midi Notes/d-3.mid','Midi Notes/Midi Notes/e3.mid',
              'Midi Notes/Midi Notes/f3.mid', 'Midi Notes/Midi Notes/f-3.mid', 'Midi Notes/Midi Notes/g3.mid', 'Midi Notes/Midi Notes/g-3.mid',
              'Midi Notes/Midi Notes/a4.mid', 'Midi Notes/Midi Notes/a-4.mid', 'Midi Notes/Midi Notes/b4.mid', 'Midi Notes/Midi Notes/c4.mid',
              'Midi Notes/Midi Notes/c-4.mid', 'Midi Notes/Midi Notes/d4.mid', 'Midi Notes/Midi Notes/d-4.mid','Midi Notes/Midi Notes/e4.mid',
              'Midi Notes/Midi Notes/f4.mid', 'Midi Notes/Midi Notes/f-4.mid', 'Midi Notes/Midi Notes/g4.mid', 'Midi Notes/Midi Notes/g-4.mid',
              'Midi Notes/Midi Notes/a5.mid', 'Midi Notes/Midi Notes/a-5.mid', 'Midi Notes/Midi Notes/b5.mid', 'Midi Notes/Midi Notes/c5.mid',
              'Midi Notes/Midi Notes/c-5.mid', 'Midi Notes/Midi Notes/d5.mid', 'Midi Notes/Midi Notes/d-5.mid','Midi Notes/Midi Notes/e5.mid',
              'Midi Notes/Midi Notes/f5.mid', 'Midi Notes/Midi Notes/f-5.mid', 'Midi Notes/Midi Notes/g5.mid', 'Midi Notes/Midi Notes/g-5.mid']

CANVAS_WIDTH = 1150
CANVAS_HEIGHT = 700

INTERACTIVE_WHITE_KEYS = 21
TOP_OF_KEYS = CANVAS_HEIGHT * 3 // 4

PIANO_WHITE_KEYS = 52

white_key_locations = [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 27, 29, 31, 32, 34,
                       36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67,
                       68, 70, 72, 74, 75, 77, 79, 80, 82, 84, 86, 87]


class KeyPress:
    def __init__(self, x_location, y_location):
        self.x_location = x_location
        self.y_location = y_location

    def play_note(self):
        """
        Input:
            Mouse x_location
        Output:
            Corresponding MIDI file of note
        """
        sections = CANVAS_WIDTH / INTERACTIVE_WHITE_KEYS
        if self.y_location >= CANVAS_HEIGHT * 29 / 32:  # White keys -- Starts at low A
            if self.x_location <= sections:
                return note_midis[0]
            elif self.x_location <= sections * 2:
                return note_midis[2]
            elif self.x_location <= sections * 3:
                return note_midis[3]
            elif self.x_location <= sections * 4:
                return note_midis[5]
            elif self.x_location <= sections * 5:
                return note_midis[7]
            elif self.x_location <= sections * 6:
                return note_midis[8]
            elif self.x_location <= sections * 7:
                return note_midis[10]
            elif self.x_location <= sections * 8:
                return note_midis[12]
            elif self.x_location <= sections * 9:
                return note_midis[14]
            elif self.x_location <= sections * 10:
                return note_midis[15]
            elif self.x_location <= sections * 11:
                return note_midis[17]
            elif self.x_location <= sections * 12:
                return note_midis[19]
            elif self.x_location <= sections * 13:
                return note_midis[20]
            elif self.x_location <= sections * 14:
                return note_midis[22]
            elif self.x_location <= sections * 15:
                return note_midis[24]
            elif self.x_location <= sections * 16:
                return note_midis[26]
            elif self.x_location <= sections * 17:
                return note_midis[27]
            elif self.x_location <= sections * 18:
                return note_midis[29]
            elif self.x_location <= sections * 19:
                return note_midis[31]
            elif self.x_location <= sections * 20:
                return note_midis[32]
            elif self.x_location <= sections * 21:
                return note_midis[34]
        elif self.y_location >= TOP_OF_KEYS:  # Black keys
            if sections - 20 <= self.x_location <= sections + 30:
                return note_midis[1]
            elif sections * 3 - 20 <= self.x_location <= sections * 3 + 30:
                return note_midis[4]
            elif sections * 4 - 20 <= self.x_location <= sections * 4 + 30:
                return note_midis[6]
            elif sections * 6 - 20 <= self.x_location <= sections * 6 + 30:
                return note_midis[9]
            elif sections * 7 - 20 <= self.x_location <= sections * 7 + 30:
                return note_midis[11]
            elif sections * 8 - 20 <= self.x_location <= sections * 8 + 30:
                return note_midis[13]
            elif sections * 10 - 20 <= self.x_location <= sections * 10 + 30:
                return note_midis[16]
            elif sections * 11 - 20 <= self.x_location <= sections * 11 + 30:
                return note_midis[18]
            elif sections * 13 - 20 <= self.x_location <= sections * 13 + 30:
                return note_midis[21]
            elif sections * 14 - 20 <= self.x_location <= sections * 14 + 30:
                return note_midis[23]
            elif sections * 15 - 20 <= self.x_location <= sections * 15 + 30:
                return note_midis[25]
            elif sections * 17 - 20 <= self.x_location <= sections * 17 + 30:
                return note_midis[28]
            elif sections * 18 - 20 <= self.x_location <= sections * 18 + 30:
                return note_midis[30]
            elif sections * 20 - 20 <= self.x_location <= sections * 20 + 30:
                return note_midis[33]
            elif sections * 21 - 20 <= self.x_location <= sections * 21 + 30:
                return note_midis[35]

    @staticmethod
    def get_location_x(location):
        """
        Given:
            location: 0-88 key location
        Output:
            Scaled x-component which corresponds to the exact key on the display

        Process:
            If location is in white keys list, subtract however many black keys come before it and scale

            If location is not in white keys list, subtract number of black keys including itself! and scale off
                of the white key before it
        """
        if location in white_key_locations:
            if location == 2 or location == 3:
                location = int(location) - 1
            elif location == 5:
                location = int(location) - 2
            elif location == 7 or location == 8:
                location = int(location) - 3
            elif location == 10:
                location = int(location) - 4
            elif location == 12:
                location = int(location) - 5
            elif location == 14 or location == 15:
                location = int(location) - 6
            elif location == 17:
                location = int(location) - 7
            elif location == 19 or location == 20:
                location = int(location) - 8
            elif location == 22:
                location = int(location) - 9
            elif location == 24:
                location = int(location) - 10
            elif location == 26 or location == 27:
                location = int(location) - 11
            elif location == 29:
                location = int(location) - 12
            elif location == 31 or location == 32:
                location = int(location) - 13
            elif location == 34:
                location = int(location) - 14
            elif location == 36:
                location = int(location) - 15
            elif location == 38 or location == 39:
                location = int(location) - 16
            elif location == 41:
                location = int(location) - 17
            elif location == 43 or location == 44:
                location = int(location) - 18
            elif location == 46:
                location = int(location) - 19
            elif location == 48:
                location = int(location) - 20
            elif location == 50 or location == 51:
                location = int(location) - 21
            elif location == 53:
                location = int(location) - 22
            elif location == 55 or location == 56:
                location = int(location) - 23
            elif location == 58:
                location = int(location) - 24
            elif location == 60:
                location = int(location) - 25
            elif location == 62 or location == 63:
                location = int(location) - 26
            elif location == 65:
                location = int(location) - 27
            elif location == 67 or location == 68:
                location = int(location) - 28
            elif location == 70:
                location = int(location) - 29
            elif location == 72:
                location = int(location) - 30
            elif location == 74 or location == 75:
                location = int(location) - 31
            elif location == 77:
                location = int(location) - 32
            elif location == 79 or location == 80:
                location = int(location) - 33
            elif location == 82:
                location = int(location) - 34
            elif location == 84:
                location = int(location) - 35
            elif location == 86 or location == 87:
                location = int(location) - 36
            return int((CANVAS_WIDTH / PIANO_WHITE_KEYS) * int(location) + (CANVAS_WIDTH / PIANO_WHITE_KEYS / 3))
        else:
            if location == 1:
                location = int(location) - 1
            elif location == 4:
                location = int(location) - 2
            elif location == 6:
                location = int(location) - 3
            elif location == 9:
                location = int(location) - 4
            elif location == 11:
                location = int(location) - 5
            elif location == 13:
                location = int(location) - 6
            elif location == 16:
                location = int(location) - 7
            elif location == 18:
                location = int(location) - 8
            elif location == 21:
                location = int(location) - 9
            elif location == 23:
                location = int(location) - 10
            elif location == 25:
                location = int(location) - 11
            elif location == 28:
                location = int(location) - 12
            elif location == 30:
                location = int(location) - 13
            elif location == 33:
                location = int(location) - 14
            elif location == 35:
                location = int(location) - 15
            elif location == 37:
                location = int(location) - 16
            elif location == 40:
                location = int(location) - 17
            elif location == 42:
                location = int(location) - 18
            elif location == 45:
                location = int(location) - 19
            elif location == 47:
                location = int(location) - 20
            elif location == 49:
                location = int(location) - 21
            elif location == 52:
                location = int(location) - 22
            elif location == 54:
                location = int(location) - 23
            elif location == 57:
                location = int(location) - 24
            elif location == 59:
                location = int(location) - 25
            elif location == 61:
                location = int(location) - 26
            elif location == 64:
                location = int(location) - 27
            elif location == 66:
                location = int(location) - 28
            elif location == 69:
                location = int(location) - 29
            elif location == 71:
                location = int(location) - 30
            elif location == 73:
                location = int(location) - 31
            elif location == 76:
                location = int(location) - 32
            elif location == 78:
                location = int(location) - 33
            elif location == 81:
                location = int(location) - 34
            elif location == 83:
                location = int(location) - 35
            elif location == 85:
                location = int(location) - 36
            elif location == 88:
                location = int(location) - 37
            return int((CANVAS_WIDTH / PIANO_WHITE_KEYS) * int(location) + (CANVAS_WIDTH / PIANO_WHITE_KEYS * 2 / 3))

