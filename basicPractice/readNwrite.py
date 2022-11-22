
class readWrite:
    def rw(self):
        with open('git.txt', 'r') as reader:
            content = reader.readlines()
            print(content)
            rc = reversed(content)
            with open('git.txt', 'w') as writer:
                for line in rc:
                    writer.write(line)


    def content(self):
        with open('git.txt', 'r') as reader1:
            content1 = reader1.readlines()
            print(content1)