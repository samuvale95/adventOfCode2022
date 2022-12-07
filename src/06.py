from utils.api import get_input

input_str = get_input(6)
input_str_trivial="mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def execute_first(input_str):
	i,j=1,5
	while(len(set(input_str[i:j]))!=4):
		i+=1
		j+=1
	return j

def execute_second(input_str):
	i,j=1,15
	while(len(set(input_str[i:j]))!=14):
		i+=1
		j+=1
	return j

def test_easy_input_first():
	assert execute_first("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
	assert execute_first("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
	assert execute_first("nppdvjthqldpwncqszvftbrmjlhg") == 6
	assert execute_first("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
	assert execute_first("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

def test_easy_input_second():
	assert execute_second("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
	assert execute_second("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
	assert execute_second("nppdvjthqldpwncqszvftbrmjlhg") == 23
	assert execute_second("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
	assert execute_second("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26

if __name__ == '__main__':
	test_easy_input_first()
	test_easy_input_second()

	print(execute_first(input_str))
	print(execute_second(input_str))