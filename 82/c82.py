keys = {
 "1": "0,4", "2": "1,4", "3": "2,4", "4": "3,4", "5": "4,4", "6": "5,4", "7": "6,4", "8": "7,4", "9": "8,4", "0": "9,4",
 "q": "0,3", "w": "1,3", "e": "2,3", "r": "3,3", "t": "4,3", "y": "5,3", "u": "6,3", "i": "7,3", "o": "8,3", "p": "9,3",
 "C": "0,2", "a": "1,2", "s": "2,2", "d": "3,2", "f": "4,2", "g": "5,2", "h": "6,2", "j": "7,2", "k": "8,2", "l": "9,2",
                         "z": "2,1", "x": "3,1", "c": "4,1", "v": "5,1", "b": "6,1", "n": "7,1", "m": "8,1",
                                     "S": "3,0", "P": "4,0", "B": "5,0", "A": "6,0", "R": "7,0"
}
space_bar_keyset = ('S', 'P', 'B', 'A', 'R')

def get_key_pos(key):
 return (*map(int, keys.get(key, "0,0").split(',')),)

def get_distance(pos, key):
 key_pos = get_key_pos(key)
 return abs(pos[0]-key_pos[0])+abs(pos[1]-key_pos[1])

def get_min_distance_key(pos, keyset):
 min_distance_key = (keyset[0], get_distance(pos, keyset[0]))
 for i in range (1, len(keyset)):
  i_distance = get_distance(pos, keyset[i])
  if i_distance < min_distance_key[1]:
   min_distance_key = (keyset[i], i_distance)
 return min_distance_key
 
def solve():
 text = input()
 current_pos = None
 speed = int(input())
 index = 0
 total_distance = 0
 caps_lock = False
 while index < len(text):
  char = text[index]
  if char.isalpha() and char.isupper() is not caps_lock:
   target_key = "C"
   caps_lock = not(caps_lock)
  else:
   target_key = text[index].lower()
   index += 1
  current_pos = get_key_pos(target_key) if not current_pos else current_pos
  if current_pos == (0, 0) and target_key != " ":
   min_distance_key = get_min_distance_key(get_key_pos(target_key), space_bar_keyset)
   total_distance += min_distance_key[1]
   current_pos = get_key_pos(target_key)
  elif current_pos != (0, 0) and target_key != " ":
   total_distance += get_distance(current_pos, target_key)
   current_pos = get_key_pos(target_key)
  elif current_pos not in ((0, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)):
   min_distance_key = get_min_distance_key(current_pos, space_bar_keyset)
   total_distance += min_distance_key[1]
   current_pos = get_key_pos(min_distance_key[0])
 return total_distance//speed

testcases = int(input())
while testcases:
 testcases -= 1
 print(solve())

