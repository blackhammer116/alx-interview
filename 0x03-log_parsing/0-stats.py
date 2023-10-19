#!/usr/bin/python3
"""
"""


#value  = input('')

#input_format = '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'
def get_log():
    """
    """
    value = []
    line = 0
    while True:
        try:
            let_val = input('')
            value.append(let_val)
            line += 1
            if line % 10 == 0:
                status_counts = {}
                tot_size = 0
                for i in value:
                    tot_size += int(i.split(' ')[-1])
                print(f'File size: {tot_size}')
                for i in value:
                    status_code = int(i.split(' ')[-2])
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1

                for code in sorted(status_counts):
                    print(f"{code}: {status_counts[code]}")

        except KeyboardInterrupt:
            print(f'File size: {tot_size}')
            for code in sorted(status_counts):
                print(f"{code}: {status_counts[code]}")
            break

if __name__ == '__main__':
    get_log()
