from src.room import *
from src.song import *
from src.guest import *
from src.bar import *
import unittest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("1", 0, 6, 100)
        self.guest_1 = Guest("Hansel", 20, 50, "Can't take my eyes off you")
        self.guest_2 = Guest("Abdul", 24, 350, "Runaway")
        self.guest_3 = Guest("Bryan", 21, 56, "Unwell")
        self.guest_4 = Guest("Charles", 28, 150, "Ghost")
        self.guest_5 = Guest("David", 29, 20, "Candy")
        self.guest_6 = Guest("Emily", 24, 40, "I Miss You")
        self.guest_7 = Guest("Frankie", 30, 60, "Someday")
        self.guest_group = [self.guest_1,
                            self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6]
        self.song1 = Song("Can't take my eyes off you", "Frankie Valli")
        self.bar = Bar("bar_caraoke")
        self.drink = Drink("Beer", 5)

    def test_find_room_number(self):
        self.assertEqual("1", self.room1.room_num)

    def test_empty_room(self):
        self.assertEqual(0, self.room1.time)

    def test_guest_check_in_number(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual(1, len(self.room1.people_list))

    def test_checked_in_guest_name(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual("Hansel", self.room1.people_list[0].name)

    def test_checked_in_guest_age(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual(20, self.room1.people_list[0].age)

    def test_guest_check_out(self):
        self.room1.guest_check_in(self.guest_1)
        self.room1.guest_check_out(self.guest_1)
        self.assertEqual(0, len(self.room1.people_list))

    def test_add_song_to_room_by_title(self):
        self.room1.add_song_to_list(self.song1)
        self.assertEqual("Can't take my eyes off you",
                         self.room1.songs_list[0].title)

    def test_add_song_to_room_by_artist(self):
        self.room1.add_song_to_list(self.song1)
        self.assertEqual("Frankie Valli", self.room1.songs_list[0].artist)

    def test_count_song_list(self):
        add_song = self.room1.add_song_to_list(self.song1)
        self.assertEqual(1, self.room1.count_song_list())

    def test_if_the_room_is_full(self):
        for people in self.guest_group:
            self.room1.guest_check_in(people)
        self.assertEqual(
            "Room is full", self.room1.guest_check_in(self.guest_7))

    def test_servcie_caraoke(self):
        self.guest_1.pay_fee(self.room1.entrance_fee)
        self.room1.guest_check_in(self.guest_1)
        self.guest_1.buy_drink(self.drink)
        self.guest_1.fav_song_play(self.guest_1)
        self.room1.guest_check_out(self.guest_1)
        self.assertEqual(
            "Wooohooo!", self.guest_1.fav_song_play(self.guest_1.fav_song))
        self.assertEqual(40, self.guest_1.budget)
