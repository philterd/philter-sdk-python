import philter

if __name__ == '__main__':
    filtered = philter.explain("https://10.0.2.217:8080", "George Washington was president.", verify=False)
    print(filtered)
