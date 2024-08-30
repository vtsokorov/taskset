# input file:
# 5,5,0
# 5
# 1,1
# 1,1
# 3
# 4,4,5,4
# 444

#output file:
15
4
20
444

def test(input_file, output_file):
    data = []

    with open(input_file) as file:
        data = [
            list(
                map(int, item.strip().split(','))
            ) for item in file
        ]

    result = [
       sum(
           sum(
               data[index: index + 2], []
            )
        ) for index in range(0, len(data), 2)
    ]

    with open(output_file, 'w') as file:
        for item in result:
            file.write(f"{item}\n")

test('input.txt', 'output.txt')