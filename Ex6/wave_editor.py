import math
import os
from wave_helper import *


WELCOME_MENU_MSG = "The following options are available:\n" \
                  "1. Modify .WAV File\n" \
                  "2. Merge 2 .WAV Files\n" \
                  "3. Compose a tune.\n" \
                  "4. Exit\n " \
                   "Please enter the number of the option to proceed:"

WELCOME_MENU_ERROR_MSG = "You have entered an invalid choice.\n" \
                         "Please enter a valid option: 1, 2, 3 or 4."

MODIFICATION_FILE_REQUEST_MSG = "Please enter the filename you would " \
                                "like to modify:"
WAV_MODIFICATION_MSG = "You have six possible modifications to perform:\n" \
                       "1. Reverse\n" \
                       "2. Increase playback speed\n" \
                       "3. Decrease playback speed\n" \
                       "4. Increase volume\n" \
                       "5. Decrease volume\n" \
                       "6. Low pass filter\n" \
                       "Please pick a single option:"
WAV_MODIFICATION_ERROR_MSG = "You have entered a wrong choice.\n" \
                             "Please enter a valid choice."
WAV_MERGE_MSG = "Please enter the name of the files you would like to merge:"
TRANSITION_MENU_MSG = "You have two options:\n" \
                      "1. Save the .wav file\n" \
                      "2. Edit the .wav file\n" \
                      "Please select a valid option:"
SAVE_FILE_MSG = "You have chosen to save the file.\n" \
                "Please enter a file name:"
COMPOSE_TUNE_MSG = "Please enter a valid text filename to compose:"
FILE_ERROR = "File not found or invalid."

frequency_dic = {"A": 440, "B": 494, "C": 523, "D": 587, "E": 659, "F": 698,
                 "G": 784, "Q": 0}

CONSTANT_FRAME_RATE = 2000
SIXTEENTH_SAMPLE = 125
MIN_VOLUME = -32768
MAX_VOLUME = 32767
MULTIPLY_CONSTANT = 1.2

##############################################################################
#                           MODIFY WAV FILES                                 #


def modify_wav_file():
    """
    Receives filename as input from user and loads the file.
    if the file is invalid, runs again.
    If the file is valid, runs the modify function on the audio data and
    frame rate of the file.
    """
    filename = input(MODIFICATION_FILE_REQUEST_MSG)
    if load_wave(filename) == -1:  # invalid file
        print(FILE_ERROR)
        modify_wav_file()
    else:  # valid file
        frame_rate, audio_data = load_wave(filename)
        valid_file_modify(audio_data, frame_rate)


def valid_file_modify(audio_data, frame_rate):
    """
    Asks user for input and then changes the audio data according to the user
    choice
    :param audio_data: nested lists from load_wave
    :param frame_rate: single integer from load_wave
    :return: sends to transition_menu with the changed audio data
    """
    modify_menu_choice = input(WAV_MODIFICATION_MSG)
    if modify_menu_choice == "1":
        transition_menu(reverse_wav(audio_data), frame_rate)
    if modify_menu_choice == "2":
        transition_menu(speed_wav(audio_data), frame_rate)
    if modify_menu_choice == "3":
        transition_menu(slow_wav(audio_data), frame_rate)
    if modify_menu_choice == "4":
        transition_menu(change_volume(audio_data, 4), frame_rate)
    if modify_menu_choice == "5":
        transition_menu(change_volume(audio_data, 5), frame_rate)
    if modify_menu_choice == "6":
        transition_menu(low_pass_filter(audio_data), frame_rate)
    else:  # invalid choice
        print(WAV_MODIFICATION_ERROR_MSG)
        valid_file_modify(audio_data, frame_rate)


def reverse_wav(lst):
    """
    :param lst: nested list representing audio data
    :return: reversed list
    """
    reverse_lst = lst[::-1]
    return reverse_lst


def speed_wav(lst):
    """
    :param lst: nested list representing audio data
    :return: list with only the items in even indexes starting from 0
    """
    speed_lst = []
    i = 0
    while i < len(lst):
        speed_lst.append(lst[i])
        i += 2
    return speed_lst


def slow_wav(lst):
    """
    :param lst: nested list representing audio data
    :return: a changed list, between every 2 elements a new list in inserted,
    its first index is the averages of the first index of the lists to its
    right and left,its second index is the averages of the second index of the
    lists to its right and left
    """
    for i in range(len(lst) - 1, 0, -1):
        avg_0 = int((lst[i][0] + lst[i-1][0]) / 2)
        avg_1 = int((lst[i][1] + lst[i-1][1]) / 2)
        avg = [avg_0, avg_1]
        lst.insert(i, avg)
    return lst


def change_volume(lst, choice):
    """
    :param lst: nested list representing audio data
    :param choice:
    :return: if choice is "4", a list with every value multiplied by 1.2,
    if choice is "5", a list with every value divided by 1.2
    """
    for pair in lst:
        for i in range(len(pair)):
            if choice == "4":  # multiply
                pair[i] = int(pair[i] * MULTIPLY_CONSTANT)
            elif choice == "5":  # divide
                pair[i] = int(pair[i] / MULTIPLY_CONSTANT)
            if pair[i] > MAX_VOLUME:
                pair[i] = MAX_VOLUME  # highest volume possible
            if pair[i] < MIN_VOLUME:
                pair[i] = MIN_VOLUME  # lowest volume possible
    return lst


def low_pass_filter(lst):  # try to find a solution without deep copy!
    """
    :param lst: nested list representing audio data
    :return: a changed lst with each item in nested list replaced by the the
    average of the item in list to its left, item in list to its right, with
    the matching indexes, and itself.
    for the first list, average is item itself and in the list to its right.
    for the second list, average is item itself and in the list to its left.
    """
    lpf_lst = []
    for i in range(len(lst)):
        if i == 0:
            group = lst[i:i+2]
            averaged = [int((group[0][0] + group[1][0])/2),
                        int((group[0][1] + group[1][1])/2)]
            lpf_lst.append(averaged)
        elif i == len(lst)-1:
            group = lst[i-1:i+1]
            averaged = [int((group[0][0] + group[1][0])/2),
                        int((group[0][1] + group[1][1])/2)]
            lpf_lst.append(averaged)
        else:
            group = lst[i-1:i+2]
            averaged = [int((group[0][0] + group[1][0] + group[2][0])/3),
                        int((group[0][1] + group[1][1] + group[2][0])/3)]
            lpf_lst.append(averaged)
    return lpf_lst

##############################################################################
#                               MERGE 2 WAV FILES                            #


def gcd(num1, num2):
    """
    Euclid's algorithm to finding the greatest common divisor.
    :param num1: integer
    :param num2: integer
    :return: num1 as greatest common divisor of original num1 and num2
    """
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


def merge_lists_same_frate(lst1, lst2):
    """
    Merge 2 nested lists into a new list containing the average of every
    matching index
    if one list is longer than the other, merge the lists up to the end of the
    shorter list, and add the rest of the items from the longer list.
    :param lst1:
    :param lst2:
    :return: average list of the 2 lists
    """
    i = 0
    avg_lst = []
    while i < len(lst1) and i < len(lst2):
        group = [(int(((lst1[i][0] + lst2[i][0]) / 2))),
                 int(((lst1[i][1] + lst2[i][1]) / 2))]
        avg_lst.append(group)
        i += 1
    if len(lst1) < len(lst2):
        return avg_lst + lst2[len(lst1)::]
    return avg_lst + lst1[len(lst2)::]


def slice_lst(lst, jump, pick):
    """
    Chooce pick-nth items out of every jump-nth items in the lst and returns
    the sliced list.
    :param lst: nested list represting audio data
    :param jump: number to pick items out of
    :param pick: items to pick out of every jump
    :return: sliced list
    """
    sliced_lst = []
    for j in range(0, len(lst), jump):
        sliced_lst += lst[j:j + pick]  # add the picked items to the list
    return sliced_lst


def compare_frame_rates(frame_rate1, frame_rate2):
    """
    :param frame_rate1: integer representing the frame rate of first file
    :param frame_rate2: integer representing the frame rate of second file
    :return: the smallest frame rate and largest frame rate, in this order.
    """
    if frame_rate1 > frame_rate2:
        greater_frame_rate = frame_rate1
        lesser_frame_rate = frame_rate2
    else:  # frame_rate2 > frame_rate1
        greater_frame_rate = frame_rate2
        lesser_frame_rate = frame_rate1
    return lesser_frame_rate, greater_frame_rate


def merge_audio():
    """
    This function asks for user for 2 filenames as input.
    If the file names are invalid, asks again.
    if the files are correct, merge the lists according to their audio data
    and frame rates, and sends user to transition menu
    :return:
    """
    file_names = input(WAV_MERGE_MSG)
    filename1, filename2 = file_names.split(" ")
    file1, file2 = load_wave(filename1), load_wave(filename2)

    while file1 == -1 and file2 == -1:  # while files invalid
        file_names = input(FILE_ERROR)  # ask again for input
        filename1, filename2 = file_names.split(" ")
        file1, file2 = load_wave(filename1), load_wave(filename2)

    frame_rate1, audio_data1 = file1[0], file1[1]
    frame_rate2, audio_data2 = file2[0], file2[1]

    if frame_rate1 == frame_rate2:
        merged_lst = merge_lists_same_frate(audio_data1, audio_data2)
        transition_menu(merged_lst, frame_rate1)
    else:  # if frame_rate1 != frame_rate2:
        less_frame_rate, great_frame_rate = \
            compare_frame_rates(frame_rate1, frame_rate2)

        gc = gcd(frame_rate1, frame_rate2)  # greatest common of the two
        pick = less_frame_rate / gc  # number of items to pick
        jump = great_frame_rate / gc  # number of items to pick out from

        if len(audio_data1) > len(audio_data2):
            sliced_lst = slice_lst(audio_data1, jump, pick)
            merged_lst = merge_lists_same_frate(audio_data2, sliced_lst)
            # merge the second list with the sliced list
        else:  # len(audio_data2) > len(audio_data1)
            sliced_lst = slice_lst(audio_data2, jump, pick)
            merged_lst = merge_lists_same_frate(audio_data1, sliced_lst)
        transition_menu(merged_lst, less_frame_rate)

##############################################################################
#                               COMPOSE TUNE                                 #


def samples_p_cycle(frequency):
    """
    :param frequency: frequency of audio wave
    :return: samples per cycle calculated by the given function.
    """
    if frequency == frequency_dic["Q"]:  # silent frequency
        samples_per_cycles = 0  # to avoid dividing by zero
    else:
        samples_per_cycles = CONSTANT_FRAME_RATE / frequency
    return samples_per_cycles


def i_sample_rate_func(i, frequency):
    if frequency == frequency_dic["Q"]:  # silent frequency
        i_sample_rate = 0  # to avoid dividing by zero
    else:
        i_sample_rate = int(MAX_VOLUME * math.sin(math.pi * 2 * i /
                                                  samples_p_cycle(frequency)))
    return i_sample_rate


def compose_tune():
    """
    This function asks the user for a text file to compose a tune out of.
    If no such file exists, the function will keep asking for a valid file.
    If file exists, function with compose a tune using the sample functions.
    :return: The function will send the user to the transition menu
    with the tune's audio data and frame rate.
    """
    audio_data = []
    filename = input(COMPOSE_TUNE_MSG)
    while os.path.isfile(filename) is False:  # no such file exist
        print(FILE_ERROR)
        filename = input(COMPOSE_TUNE_MSG)

    with open(filename, "r") as f:
        text_lst = f.read().split()  # read the tune instructions

    for i in range(0, len(text_lst), 2):
        for num in range(int(text_lst[i+1]) * SIXTEENTH_SAMPLE):
            single_channel_data = \
                i_sample_rate_func(num, frequency_dic[text_lst[i]])
            audio_data.append([single_channel_data, single_channel_data])
    transition_menu(audio_data, CONSTANT_FRAME_RATE)

##############################################################################
#                               TRANSITION MENU                              #


def transition_menu(audio_data, frame_rate):
    """
    This function is called either by modifying file, merging files or
    composing tunes.
    If user input is one, the function will ask for a filename and then
    proceed to save the file.
    If the input is 2, the function will call the modify function with the
    current audio data and frame_rate.
    :param audio_data: nested list of audio data from previous function
    :param frame_rate: integer of frame rate from previous function
    :return: depends on user input, see description above
    """
    transition_menu_choice = input(TRANSITION_MENU_MSG)
    if transition_menu_choice == "1":
        wave_filename = input(SAVE_FILE_MSG)
        save_wave(frame_rate, audio_data, wave_filename)
        main()
    if transition_menu_choice == "2":
        valid_file_modify(audio_data, frame_rate)
    else:
        transition_menu(audio_data, frame_rate)

##############################################################################
#                               MAIN                             #


def main():
    welcome_menu_choice = input(WELCOME_MENU_MSG)
    if welcome_menu_choice == "1":
        modify_wav_file()
    if welcome_menu_choice == "2":
        merge_audio()
    if welcome_menu_choice == "3":
        compose_tune()
    if welcome_menu_choice == "4":
        return
    else:
        print(WELCOME_MENU_ERROR_MSG)
        main()


if __name__ == '__main__':
    main()


