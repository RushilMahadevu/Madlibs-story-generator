from random import randint
import copy

timeline = (
    'I was feeling {} one day so I went to the {} game which was located in {}.\n ' +
    'When I got there I wanted to see the {} go against the {}.\n ' +
    'The game was really fun! I ate some {} and drank some {}.\n ' +
    'It was the best thing ever I hope I do it again.\n '
)

word_dict = {
    'adjective':['greedy','abrasive','grubby','groovy','rich','harsh','slow', 'infamous', 'steady', 'verdant', 'puffy', 'berserk', 'quirky', 'aggresive', 'astonishing', 'future'],
    'city_name':['Chicago','New York','Charlotte','Indianapolis','Louisville','Denver', 'Vaduz', 'Stockholm', 'Bamako', 'Singapore', 'Abidjan', 'Manila', 'Guatemala City', 'Warsaw'],
    'food':['apples', 'burgers', 'sandwiches', 'popcorn', 'octopuses', 'cloves', 'rice', 'strawberries', 'ribs', 'fries', 'chips', 'elk', 'ice cream', 'cookies', 'bananas', 'figs'],
    'beverages':['sprite', 'coca-cola', 'water', 'gatorade', 'lemonade', 'sweet tea', 'iced coffee', 'coffee', 'diet-coke', 'tea', 'champagne', 'wine', 'hot tea', 'iced tea'],
    'action':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce', 'drive', 'deliver', 'seperate', 'view', 'pay', 'meet', 'force', 'mark', 'thank', 'persuade'],
    'sports':['volleyball','football','soccer','cricket', 'tennis', 'skiing', 'water polo', 'basketball', 'archery', 'taekwondo', 'rowing', 'table tennis', 'ice skating']
}

def get_word(type, local_dict):
    words = local_dict[type]
    count = len(words) - 1
    index = randint(0, count)
    return local_dict[type].pop(index)

def create_timeline():
    local_dict = copy.deepcopy(word_dict)
    return timeline.format(
        get_word('adjective', local_dict),
        get_word('sports', local_dict),
        get_word('city_name', local_dict),
        get_word('city_name', local_dict),
        get_word('city_name', local_dict),
        get_word('food', local_dict),
        get_word('beverages', local_dict),
    )

print('Story:')
print(create_timeline())
