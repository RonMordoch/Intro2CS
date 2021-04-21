from hangman import update_word_pattern


def check_update_word_pattern():
    if update_word_pattern('compsci', '_______', 'q') == '_______':
        if update_word_pattern('code', '____', 'd') == '__d_':
            if update_word_pattern('pattern', '__tt___', 't') == '__tt___':
                if update_word_pattern('pattern', '__tt___', 'c') == '__tt___':
                    print('Function “update_word_pattern” test success!')
                    return True
                else:
                    print('Function “update_word_pattern” test fail!')
                    return False
            else:
                print('Function “update_word_pattern” test fail!')
                return False
        else:
            print('Function “update_word_pattern” test fail!')
            return False
    else:
        print('Function “update_word_pattern” test fail!')
        return False


if __name__ == "__main__":
    check_update_word_pattern()