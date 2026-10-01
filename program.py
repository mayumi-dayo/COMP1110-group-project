#import package manager modules

#import local modules
import modules.testmodule as test
import modules.conf as conf

# main program
if __name__ == "__main__":
    print(test.add(1,2))
    conf.wah()
